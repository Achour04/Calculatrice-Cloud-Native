resource "scaleway_rdb_instance" "production" {
  name           = "${var.project_name}-db-prod"
  node_type      = "DB-DEV-S"
  engine         = "redis"
  is_ha_cluster  = true
  disable_backup = false
}

resource "scaleway_rdb_instance" "development" {
  name           = "${var.project_name}-db-dev"
  node_type      = "DB-DEV-S"
  engine         = "redis"
  is_ha_cluster  = false
  disable_backup = true
}