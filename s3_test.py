import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Replace these with your own AWS credentials and bucket details
AWS_ACCESS_KEY_ID = "AKIA4T4OB6JRU5B5RLOM"
AWS_SECRET_ACCESS_KEY = "i9qlqGJU/Fl3T1X6W7eL9Edpfe5YclVD8Vf9vDO+"
AWS_REGION = "ap-northeast-2"  # e.g., "us-east-1"
BUCKET_NAME = "pdf-basic-app-2025"

os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""


def upload_file_to_s3(file_name, object_name):
    """Upload a file to S3."""
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        s3_client.upload_file(file_name, BUCKET_NAME, object_name)
        print(f"File {file_name} uploaded to {BUCKET_NAME}/{object_name}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")

def read_file_from_s3(object_name, download_path):
    """Download a file from S3."""
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        # Download the file
        s3_client.download_file(BUCKET_NAME, object_name, download_path)
        print(f"File {object_name} downloaded from {BUCKET_NAME} to {download_path}")
    except ClientError as e:
        print(f"An error occurred: {e}")

def delete_file_from_s3(object_name):
    """Delete a file from S3."""
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        s3_client.delete_object(Bucket=BUCKET_NAME, Key=object_name)
        print(f"File {object_name} deleted from {BUCKET_NAME}")
    except ClientError as e:
        print(f"An error occurred: {e}")

# Test the functions
if __name__ == "__main__":
    # File and object details
    test_file_path = "example.txt"  # Replace with your file path
    test_object_name = "test/example.txt"
    download_path = "downloaded_example.txt"

    # Step 1: Create a test file
    with open(test_file_path, "w") as f:
        f.write("This is a test file for S3 upload, read, and delete operations.")

    # Step 2: Upload the file
    #upload_file_to_s3(test_file_path, test_object_name)

    # Step 3: Read (download) the file
    read_file_from_s3(test_object_name, download_path)

    # Step 4: Delete the file
    delete_file_from_s3(test_object_name)
