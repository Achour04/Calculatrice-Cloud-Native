output "cluster_kubeconfig" {
  value     = scaleway_k8s_cluster.main.kubeconfig
  sensitive = true
}

output "registry_endpoint" {
  value = scaleway_registry_namespace.main.endpoint
}