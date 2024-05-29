# Product Service API

## Overview
This is a RESTful API for managing products, including creating, listing, retrieving, updating, and deleting products.

## Endpoints
1. **Add Product**: POST `/products`
2. **List Products**: GET `/products`
3. **Get Product by ID**: GET `/products/<product_id>`
4. **Update Product by ID**: PUT `/products/<product_id>`
5. **Delete Product by ID**: DELETE `/products/<product_id>`

## Setup and Deployment

### Prerequisites
- Docker
- Docker Compose

### Local Development
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/product_service.git
    cd product_service
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    flask run
    ```

### Using Docker
1. Build the Docker image:
    ```bash
    docker build -t product_service .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 product_service
    ```

### Database Migrations
1. Initialize the migration directory:
    ```bash
    flask db init
    ```

2. Create a migration:
    ```bash
    flask db migrate -m "Initial migration."
    ```

3. Apply the migration:
    ```bash
    flask db upgrade
    ```

## Testing
1. Run the tests:
    ```bash
    pytest
    ```

## API Documentation
Use a tool like Postman to interact with the API or any other API client. 

For more information, refer to the code and the inline comments.

---

Happy Testing!
