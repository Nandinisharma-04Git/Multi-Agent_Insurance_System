variable "project_name" {
  type        = string
  description = "Prefix for resource names (security group, instance tag)."
  default     = "insurance-app"
}

variable "aws_region" {
  type        = string
  description = "AWS region for the EC2 instance."
  default     = "us-east-1"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance size (e.g. t3.micro for Free Tier)."
  default     = "t3.micro"
}

variable "key_name" {
  type        = string
  description = "Optional: name of an existing EC2 Key Pair for SSH. Leave empty to launch without SSH key."
  default     = ""
}

variable "app_repository_url" {
  type        = string
  description = "Public Git URL to clone (HTTPS). The repo must contain this project (Dockerfile at root)."
}

variable "app_repository_branch" {
  type        = string
  description = "Branch to checkout after clone."
  default     = "main"
}

variable "app_port" {
  type        = number
  description = "Host and container port for the Flask app."
  default     = 5000
}

variable "ssh_cidr" {
  type        = string
  description = "CIDR allowed to SSH (port 22). Use your public IP /32 for tighter access."
  default     = "0.0.0.0/0"
}

variable "app_cidr" {
  type        = string
  description = "CIDR allowed to reach the web UI (app port)."
  default     = "0.0.0.0/0"
}
