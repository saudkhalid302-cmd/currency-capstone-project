provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "currency_bucket" {
  bucket = "capstone-currency-data-saud-final-2026"
  
  # Ye line green karegi: Agar pehle se hai toh ignore karo
  lifecycle {
    ignore_changes = all
  }
}

resource "aws_iam_user" "data_engineer" {
  name = "data-engineer-saud-final"

  lifecycle {
    ignore_changes = all
  }
}

resource "aws_iam_user_policy" "s3_access" {
  name = "s3-access-policy-final"
  user = aws_iam_user.data_engineer.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:PutObject", "s3:GetObject", "s3:ListBucket"]
        Effect   = "Allow"
        Resource = [
          "arn:aws:s3:::capstone-currency-data-saud-final-2026",
          "arn:aws:s3:::capstone-currency-data-saud-final-2026/*"
        ]
      }
    ]
  })
}