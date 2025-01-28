resource "aws_lb_target_group" "ml_tg" {
  name        = "ml-tg"
  port        = 8000
  protocol    = "HTTP"
  vpc_id      = var.vpc_id
  target_type = "ip"
}
