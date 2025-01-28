resource "aws_ecr_repository" "app_repository" {
  name = "ml-app"
}

output "ecr_repository_url" {
  value = aws_ecr_repository.app_repository.repository_url
}
