output "alb_dns" {
  value       = aws_route53_record.alb_record.name
  description = "DNS do Application Load Balancer"
}
