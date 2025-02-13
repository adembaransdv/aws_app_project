from flask import Flask, request, jsonify
import boto3
import os
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET_NAME
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://ec2-44-211-225-249.compute-1.amazonaws.com"])

# Connexion à S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

@app.route("/upload", methods=["POST"])
def upload_file():
    print("testupload")
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier trouvé"}), 400

    file = request.files["file"]
    file_name = file.filename

    try:
        s3.upload_fileobj(file, S3_BUCKET_NAME, file_name, ExtraArgs={"ACL": "public-read"})
        file_url = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{file_name}"
        return jsonify({"message": "Fichier uploadé avec succès", "url": file_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)