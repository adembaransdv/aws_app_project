import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables d'environnement

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = "us-east-1"
S3_BUCKET_NAME = "myfriedbucket"