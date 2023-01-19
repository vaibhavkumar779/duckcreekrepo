
locals {
  duck_creek_configs     = "${var.env}-duck-creek-config"
}

resource "kubernetes_config_map" "duck_creek_configs" {
  metadata {
    name      = "duck-creek-configs"
    namespace = var.namespace
  }

  data = {
    for f in fileset("${path.module}/${var.env}-duck-creek-config", "*") :
    f => file(join("/", ["${path.module}/${var.env}-duck-creek-config", f]))
  }
  }
  

resource "kubernetes_service" "service" {
  metadata {
    name = var.name
    labels = {
      "io.kompose.service" : "duck-creek"
    }
    annotations = {
      "service.beta.kubernetes.io/azure-load-balancer-internal" : "true"
    }
    namespace = var.namespace
  } //metadata
  spec {
    selector = {
      app = "duck-creek-${var.env}"
    } //selector
    session_affinity = "ClientIP"
    port {
      port        = 8434
      target_port = 8434
    } //port
    type = "LoadBalancer"
  } //spec
}   //resource


resource kubernetes_deployment deployment {
  metadata {
    namespace = var.namespace
    name      = var.name
    labels = {
      "app" : "duck-creek-${var.env}"
    }

  }
  spec {
    replicas = var.replicas
    selector {
      match_labels = {
        app = "duck-creek-${var.env}"
      }
    }
    strategy {
      type = "RollingUpdate"
      rolling_update {
        max_surge       = 1
        max_unavailable = 0
      }
    }
    template {
      metadata {
        labels = {
          app = "duck-creek-${var.env}"
        }
      }

      spec {
        dynamic "host_aliases" {

          for_each = var.host_aliases

          content {

            hostnames = host_aliases.value

            ip = host_aliases.key

          }

        }
        container {
          name  = "duck-creek-${var.env}"
          image = var.image
          security_context {
            privileged = true
          }
          command = ["/bin/sh"]
          args    = ["-c", " while true; do /opt/og-install/bin/startOAAgent.sh;tail -f /dev/null;done;"]

          volume_mount {
            mount_path = "/opt/duck_creek_configs/conf"
            name       = "duck-creek-configs"
          }
        }
        volume {
          name = "duck-creek-configs"
          config_map {
            name = "duck-creek-configs"
          }
        }

        volume {
          name = "rest-api-gateway-configs"
          config_map {
            name = "rest-api-gateway-configs"
          }
        }
        restart_policy = "Always"

      }

    }

  }

}