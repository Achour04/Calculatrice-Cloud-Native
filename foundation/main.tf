# Initialisation des ressources et variables
module "calculatrice" {
  source = "./resources"
}

output "prod_dns" {
  value = module.calculatrice.prod_dns
}

output "dev_dns" {
  value = module.calculatrice.dev_dns
}
