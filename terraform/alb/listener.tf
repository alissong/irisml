resource "aws_lb_listener" "https" {
  load_balancer_arn = aws_lb.ml_alb.arn
  port              = 443
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-2016-08"

  certificate_arn = "arn:aws:acm:us-east-1:338846672827:certificate/5591839b-8804-4ca9-a133-4203d80aa6eb"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ml_tg.arn
  }
}
