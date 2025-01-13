resource "scaleway_lb_ip" "prod_ip" {}
resource "scaleway_lb_ip" "dev_ip" {}

resource "scaleway_lb" "production" {
  ip_id = scaleway_lb_ip.prod_ip.id
  name  = "${var.project_name}-lb-prod"
  type  = "LB-S"
}

resource "scaleway_lb" "development" {
  ip_id = scaleway_lb_ip.dev_ip.id
  name  = "${var.project_name}-lb-dev"
  type  = "LB-S"
}