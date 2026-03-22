#!/bin/bash
set -euo pipefail
exec > >(tee /var/log/user-data.log)
exec 2>&1

dnf update -y
dnf install -y docker git
systemctl enable docker
systemctl start docker

APP_DIR="/opt/insurance-app"
rm -rf "$APP_DIR"
git clone --branch "${app_repository_branch}" --depth 1 "${app_repository_url}" "$APP_DIR"
cd "$APP_DIR"

docker build -t insurance-app .
docker rm -f insurance-app 2>/dev/null || true
docker run -d \
  --name insurance-app \
  --restart unless-stopped \
  -p ${app_port}:5000 \
  insurance-app

echo "User data finished at $(date -u)"
