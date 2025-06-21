import boto3
import uuid

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name=AWS_REGION
)

def upload_file_to_s3(file, filename):
    extension = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{extension}"

    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            unique_filename,
            ExtraArgs={"ContentType": file.content_type}
        )
        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{unique_filename}"
        return {"success": True, "url": url}
    except Exception as e:
        return {"success": False, "error": str(e)}
