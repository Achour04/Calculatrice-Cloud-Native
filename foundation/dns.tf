resource "scaleway_domain_record" "production" {
  dns_zone = "polytech-dijon.kiowy.net"
  name     = "calculatrice-${var.student_name}"
  type     = "A"
  data     = scaleway_lb_ip.prod_ip.ip_address
  ttl      = 300
}

resource "scaleway_domain_record" "development" {
  dns_zone = "polytech-dijon.kiowy.net"
  name     = "calculatrice-dev-${var.student_name}"
  type     = "A"
  data     = scaleway_lb_ip.dev_ip.ip_address
  ttl      = 300
}