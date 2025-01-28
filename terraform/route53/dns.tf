resource "aws_route53_zone" "paladindevs" {
  name = "paladindevs.com"
}

resource "aws_route53_record" "alb_record" {
  zone_id = aws_route53_zone.paladindevs.zone_id
  name    = "paladindevs.com"
  type    = "A"
  alias {
    name                   = aws_lb.ml_alb.dns_name
    zone_id                = aws_lb.ml_alb.zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "www_record" {
  zone_id = aws_route53_zone.paladindevs.zone_id
  name    = "www.paladindevs.com"
  type    = "CNAME"
  ttl     = 300
  records = ["paladindevs.com"]
}
