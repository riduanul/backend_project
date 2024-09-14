# Product API

This project is a simple Product API built using Django REST Framework (DRF). The API allows users to register, log in, and view products. Additionally, admin users have the ability to create, update, and delete products. JWT (JSON Web Token) is used for authentication, and custom role-based permissions control access to certain actions.

## Features

- User registration and login via JWT.
- Role-based access control (Admin and User roles).
- Only authenticated users can view products.
- Admin users can create, update, and delete products.

## Project Structure

- **users app**: Handles user registration, login, and authentication using JWT.
- **products app**: Manages the products API, including product creation, viewing, updating, and deletion.
- **permissions**: Custom permissions that restrict access based on user roles (admin and user).



## API Design and Structure

### **Design Overview**
The API follows a clear separation of concerns, with models representing the database schema, serializers handling data conversion, and views managing business logic and interactions between the client and the database. Authentication is handled via JWT, while custom permissions enforce role-based access to different API operations.

- **User App**: Responsible for user authentication, JWT token generation, and role management (admin and user).
- **Product App**: Manages products in the system, including their creation, retrieval, update, and deletion, with permission checks based on user roles.
  
### **Authentication**:
Users must log in using the `/api/user/login/` endpoint to receive a JWT token. The token must be passed in the Authorization header (`Authorization: Bearer <your-token>`) to authenticate subsequent requests.

### **Permissions**:
Custom permissions control access to product actions:
- **IsAuthenticated**: Ensures only authenticated users can access the API.
- **IsAdmin**: Restricts the creation, updating, and deletion of products to admin users only.

### **Product Management**:
- **Admin users** can create, update, and delete products.
- **Authenticated users** can retrieve the list of products.

## API Endpoints

### Product Endpoints

- **GET** `api/products/` : Retrieve a list of all products (only for authenticated users).
- **POST** `api/products/` : Create a new product (only for admin users).
- **PUT** `api/products/<id>/` : Update an existing product (only for admin users).
- **DELETE** `api/products/<id>/` : Delete a product (only for admin users).

## Models

### Product Model

The `Product` model represents the items managed in the API. It contains the following fields:

- **name** (`CharField`): A string field that stores the name of the product, limited to 255 characters.
- **description** (`TextField`): A text field for a detailed description of the product.
- **price** (`DecimalField`): Stores the product's price with up to 10 digits in total and 2 decimal places for precision.
- **quantity** (`IntegerField`): An integer field that tracks how many units of the product are available in stock.

Each field is essential for managing and displaying product information via the API, ensuring that each product has a name, description, price, and available quantity.


## Serializers

### ProductSerializer

This serializer automatically converts the `Product` model to JSON format and vice versa:

## Views

### ProductViewSet

The `ProductViewSet` handles all CRUD operations for products. Permissions are set to allow only authenticated users to view products, and admin users to create, update, and delete products.




