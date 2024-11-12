# 1. Création d'un registre de conteneur
resource "scaleway_container_registry" "example" {
  name = "calculatrice-registry"
}

# 2. Création d'un cluster Kubernetes
resource "scaleway_kubernetes_cluster" "example" {
  name            = "calculatrice-cluster"
  commercial_type = "DEV1-S"  # Type de machine pour le cluster
  version         = "1.21.5"
  tags            = ["calculatrice", "polytech-dijon"]

  node_pool {
    name      = "node-pool-dev"
    size      = "DEV1-S"  # Taille des nœuds
    image     = "ubuntu_bionic"
    min_count = 1
    max_count = 3
  }
}

# 3. Création des bases de données de développement et de production
resource "scaleway_db_instance" "dev_db" {
  name            = "calculatrice-dev-db"
  engine          = "postgresql"
  commercial_type = "DEV1-M"
  tags            = ["dev", "calculatrice"]
}

resource "scaleway_db_instance" "prod_db" {
  name            = "calculatrice-prod-db"
  engine          = "postgresql"
  commercial_type = "DEV1-M"
  tags            = ["prod", "calculatrice"]
}

# 4. Entrée DNS pour la production
resource "scaleway_dns_record" "prod_dns" {
  domain = "kiowy.net"
  type   = "A"
  name   = "calculatrice-${var.nombinome1}-${var.nombinome2}-polytech-dijon"
  value  = scaleway_lb.prod_lb.ip
}

# 5. Entrée DNS pour le développement
resource "scaleway_dns_record" "dev_dns" {
  domain = "kiowy.net"
  type   = "A"
  name   = "calculatrice-dev-${var.nombinome1}-${var.nombinome2}-polytech-dijon"
  value  = scaleway_lb.dev_lb.ip
}

# 6. LoadBalancer de production
resource "scaleway_lb" "prod_lb" {
  name              = "calculatrice-prod-lb"
  type              = "loadbalancer"
  commercial_type   = "LB1"
  tags              = ["prod", "calculatrice"]
}

# 7. LoadBalancer de développement
resource "scaleway_lb" "dev_lb" {
  name              = "calculatrice-dev-lb"
  type              = "loadbalancer"
  commercial_type   = "LB1"
  tags              = ["dev", "calculatrice"]
}

# 8. Stockage Object Storage
resource "scaleway_object_storage" "foundation_bucket" {
  name = "foundation"
  acl  = "private"
}
