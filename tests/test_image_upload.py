import io
import pytest
from unittest.mock import patch
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_images_success(client):
    mock_url = "https://fake-bucket.s3.amazonaws.com/fakefile.jpg"

    with patch("app.routes.image_routes.upload_file_to_s3") as mock_upload:
        mock_upload.return_value = {"success": True, "url": mock_url}

        data = {
            'images': (io.BytesIO(b"fake image content"), 'test.jpg')
        }

        response = client.post('/pets/images/upload', content_type='multipart/form-data', data=data)

        assert response.status_code == 201
        assert response.json['success'] is True
        assert mock_url in response.json['data']['imageUrls']

