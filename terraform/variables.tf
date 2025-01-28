variable "subnets" {
  type        = list(string)
  description = "Subnets para o ALB e ECS."
  default     = ["subnet-0522f692a71b93afa", "subnet-05f058473e31031e2", "subnet-0e6fcadc1e484717b", "subnet-01a3b68c5b08053e0", "subnet-099e91ac697f2c4f7", "subnet-06d4b5cee3e9e8977"]
}

variable "vpc_id" {
  type        = string
  description = "ID da VPC onde os recursos serão criados."
  default     = "vpc-06d92fe8a8a2338f0"
}
