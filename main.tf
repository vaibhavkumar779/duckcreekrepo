module "duck_creek" {
  source       = "./modules/duck-creek"
  name         = var.duck_creek_dev.porpeties["name"]
  namespace    = var.duck_creek_dev.porpeties["namespace"]
  image        = var.duck_creek_dev.porpeties["image"]
  env          = var.duck_creek_dev.porpeties["env"]
  host_aliases = var.host_aliases
}

