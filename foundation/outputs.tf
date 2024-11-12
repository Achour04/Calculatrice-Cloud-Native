output "prod_lb_ip" {
  description = "Adresse IP du LoadBalancer de production"
  value       = scaleway_lb.prod_lb.ip
}

output "dev_lb_ip" {
  description = "Adresse IP du LoadBalancer de développement"
  value       = scaleway_lb.dev_lb.ip
}

output "prod_db_ip" {
  description = "Adresse IP de la base de données de production"
  value       = scaleway_db_instance.prod_db.address
}

output "dev_db_ip" {
  description = "Adresse IP de la base de données de développement"
  value       = scaleway_db_instance.dev_db.address
}
