provider "aws" {
  region = "us-east-1"
}

# Sirf S3 Bucket rakhein kyunke IAM User humne manually bana liya hai
resource "aws_s3_bucket" "currency_bucket" {
  bucket = "capstone-currency-data-saud-final-2026"

  # Ye line isliye hai taake agar bucket khali na bhi ho toh Terraform usay manage kar sakay
  force_destroy = true 
}