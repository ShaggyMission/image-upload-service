# 📸 Image Upload Service - Shaggy Mission

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/AWS%20S3-232F3E?style=for-the-badge&logo=amazon-s3&logoColor=white" alt="AWS S3" />
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" alt="Swagger" />
  <img src="https://img.shields.io/badge/CORS-Enabled-green?style=for-the-badge" alt="CORS" />
</div>

<div align="center">
  <h3>🚀 Secure Image Upload Microservice for Pet Rescue Platform</h3>
  <p><em>Part of the Shaggy Mission ecosystem - Helping pets find homes through beautiful photos! 🐾</em></p>
</div>

---

## 🌟 Overview

The **Image Upload Service** is a secure file management microservice in the Shaggy Mission platform that handles pet image uploads to AWS S3. This service enables volunteers, shelters, and administrators to upload high-quality photos of rescue animals, making them more adoptable through visual storytelling.

## 🎯 What This Service Does

- **Multi-Image Upload**: Supports uploading multiple pet images simultaneously
- **AWS S3 Integration**: Securely stores images in cloud storage with public access
- **File Security**: Sanitizes filenames and validates file types for security
- **CORS Support**: Enables cross-origin requests for frontend integration
- **Batch Processing**: Handles multiple file uploads in a single request
- **Error Handling**: Comprehensive error management for upload failures

## 🛠️ Tech Stack

- **Language**: Python with Flask web framework
- **Cloud Storage**: AWS S3 for scalable image storage
- **Documentation**: Swagger UI with Flasgger integration
- **Security**: Werkzeug secure filename handling
- **CORS**: Flask-CORS for cross-origin resource sharing
- **Environment**: Python-dotenv for configuration management

## 📡 API Endpoints

### Image Upload Endpoint
**`POST /pets/images/upload`**
- Uploads one or more pet images to AWS S3
- Supports multipart/form-data content type
- Returns array of uploaded image URLs
- Handles batch uploads with individual error tracking

**Request Format:**
```
Content-Type: multipart/form-data

Form Data:
- images: file[] (required) - One or more image files
```

**Success Response (201):**
```json
{
  "success": true,
  "data": {
    "imageUrls": [
      "https://s3.amazonaws.com/bucket/pet-image-1.jpg",
      "https://s3.amazonaws.com/bucket/pet-image-2.jpg"
    ]
  }
}
```

**Error Responses:**
```json
// No files provided (400)
{
  "success": false,
  "error": "No image files provided"
}

// Upload failure (500)
{
  "success": false,
  "error": "S3 upload failed: [error details]"
}
```

### API Documentation Endpoint
**`GET /pets/imagesUpload-docs`**
- Interactive Swagger UI documentation
- Complete API specification with request/response examples
- Built-in testing interface for upload operations

## 🔧 Core Functionality

### Multi-Image Upload Process
The service handles secure image uploads through a streamlined process that validates incoming multipart form data, extracts multiple files from the request, sanitizes each filename using Werkzeug's secure_filename function, uploads each file individually to AWS S3, collects successful upload URLs, and returns a comprehensive response with all uploaded image locations.

### AWS S3 Integration
The service leverages AWS S3 for reliable, scalable image storage with built-in CDN capabilities. Images are stored with public read access, enabling direct embedding in web applications and mobile apps. The S3 integration handles authentication, bucket management, and generates publicly accessible URLs for each uploaded image.

### Security & Validation
Comprehensive security measures include filename sanitization to prevent path traversal attacks, file type validation through the S3 service layer, secure multipart form handling, and error isolation to prevent sensitive information exposure in error responses.

## 🌐 Service Integration

This microservice serves as the image management component for the entire Shaggy Mission platform, providing image upload capabilities for pet profiles, adoption listings, and rescue documentation. The service integrates seamlessly with frontend applications through CORS-enabled endpoints.

## 🔒 Security Features

- **Filename Sanitization**: Uses Werkzeug's secure_filename for safe file handling
- **File Validation**: Validates file types and sizes through S3 service integration
- **CORS Configuration**: Controlled cross-origin access for authorized domains
- **Error Handling**: Sanitized error responses without sensitive information
- **Environment Variables**: Secure configuration management for AWS credentials

## ☁️ Cloud Storage Operations

The service performs cloud storage operations through the integrated S3 service module, handling AWS authentication, bucket operations, file uploads with proper content types, public URL generation, and error handling for cloud storage failures. All uploaded images are immediately accessible via their returned URLs.

## 🚀 Development & Deployment

The service is configured for both development and production environments with debug mode for local development, environment variable configuration for AWS credentials, modular blueprint architecture for scalable routing, and comprehensive error logging for operational monitoring.

---

<div align="center">
  <p><strong>Built with ❤️ for street dogs and cats everywhere 🐕🐱</strong></p>
  <p><em>Every photo uploaded helps a pet find their forever home!</em></p>
</div>