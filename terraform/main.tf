provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "currency_bucket" {
<<<<<<< HEAD
<<<<<<< HEAD
  bucket = "capstone-currency-data-2026-saud"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.currency_bucket.id
}
=======
  bucket = "capstone-currency-data-saud-2026"
}
>>>>>>> 3f4bde50189bdebe84496db1c44f78c052987af8
=======
  bucket = "capstone-currency-data-saud-2026"
}
>>>>>>> fd711e00b6991d8c07c8896ba470bbfa271be207
