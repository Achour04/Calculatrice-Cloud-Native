resource "scaleway_k8s_cluster" "main" {
  name    = "${var.project_name}-cluster"
  version = "1.26.0"
  cni     = "cilium"
}
resource "scaleway_k8s_pool" "main" {
  cluster_id = scaleway_k8s_cluster.main.id
  name       = "${var.project_name}-pool"
  node_type  = "DEV1-M"
  size       = 3
}