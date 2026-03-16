provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "currency_bucket" {
  bucket = "capstone-currency-data-saud-2026"
}
