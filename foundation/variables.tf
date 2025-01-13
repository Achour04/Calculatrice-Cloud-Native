variable "project_name" {
  description = "Project name used for resource naming"
  default     = "calculatrice"
}

variable "binome_names" {
  description = "Names for DNS entries"
  type = object({
    nom1 = string
    nom2 = string
  })
}