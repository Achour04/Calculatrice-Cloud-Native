resource "scaleway_registry_namespace" "main" {
  name = "${var.project_name}-registry"
}