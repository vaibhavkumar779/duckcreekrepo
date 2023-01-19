variable name {
  type = string
}

variable namespace {
  type = string
}

variable image {
  type = string
}

variable args {
  type    = list(string)
  default = []
}

variable replicas {
  type    = number
  default = 1
}

variable labels {
  type    = map(string)
  default = {}
}

variable env {
}

variable host_aliases {

}