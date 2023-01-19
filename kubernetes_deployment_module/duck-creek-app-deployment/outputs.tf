output "name" {
  value = kubernetes_deployment.deployment.metadata[0].name
}

output "labels" {
  value = kubernetes_deployment.deployment.metadata[0].labels
}

output "load_balancer_hostname" {
  value = kubernetes_service.service.status.0.load_balancer.0.ingress.0.hostname
}