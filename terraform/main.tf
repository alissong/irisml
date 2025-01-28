provider "aws" {
  region = "us-east-1"
}

module "ecr" {
  source = "./ecr"
}

module "ecs" {
  source = "./ecs"
}

module "alb" {
  source = "./alb"
}
