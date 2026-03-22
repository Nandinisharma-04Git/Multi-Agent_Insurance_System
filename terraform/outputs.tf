output "instance_public_ip" {
  description = "Public IPv4 of the EC2 instance."
  value       = aws_instance.app.public_ip
}

output "app_url" {
  description = "URL to open the Flask app in a browser."
  value       = "http://${aws_instance.app.public_ip}:${var.app_port}"
}

output "ssh_hint" {
  description = "SSH command if key_name was set (replace with your key path)."
  value       = var.key_name != "" ? "ssh -i <your-key.pem> ec2-user@${aws_instance.app.public_ip}" : "No key_name set — SSH not configured."
}
