provider "aws" {
  region = "us-east-1"
}

# Bucket jise tum use kar rahe ho
resource "aws_s3_bucket" "currency_bucket" {
  bucket = "capstone-currency-data-saud-2026"
}

# Output taake tumhein pata ho bucket ka naam kya hai
output "s3_bucket_name" {
  value = aws_s3_bucket.currency_bucket.id
}

# Yahan par apna naya IAM aur permissions wala code add karo
resource "aws_iam_user" "data_engineer" {
  name = "data-engineer-saud"
}

resource "aws_iam_user_policy" "s3_access" {
  name = "s3-access-policy"
  user = aws_iam_user.data_engineer.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = ["s3:PutObject", "s3:GetObject", "s3:ListBucket"]
        Effect = "Allow"
        Resource = [
          "arn:aws:s3:::capstone-currency-data-saud-2026",
          "arn:aws:s3:::capstone-currency-data-saud-2026/*"
        ]
      }
    ]
  })
}