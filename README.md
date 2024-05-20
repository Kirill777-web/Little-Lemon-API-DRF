# Little Lemon API Project
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
The Little Lemon API is a RESTful web service built with Django and Django REST Framework. This API serves as the backend for the Little Lemon application, providing endpoints for managing menu items, categories, orders, and user roles. It is designed to support various user roles including admins, managers, delivery crew, and customers, each with specific functionalities and permissions.

## Key Features
- **User Management**: Admins can assign users to manager and delivery crew roles.
- **Menu Management**: Admins can add menu items and categories.
- **Order Management**: Managers can update the item of the day, assign orders to delivery crew members, and manage the status of orders.
- **Customer Functionality**: Customers can browse categories, menu items, add items to their cart, place orders, and view their orders.
- **Authentication**: Secure authentication using tokens.

## Link Heroku

Accessing the Little Lemon API visit link deployed application [Heroku]()
## Screenrecorder [Screencastify](https://drive.google.com/file/d/1b5ujTiECupMP5RAByAd7didqq6yd4Fui/view)


## Table of Contents
- [Description](#description)
- [Key Features](#key-features)
- [Overview](#overview)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Credits](#credits)

## Overview
The Little Lemon API provides a comprehensive solution for managing a restaurant's menu, orders, and user roles. It supports different user roles, ensuring that each user has access to the functionalities relevant to their role. The API is secured with token-based authentication, ensuring that only authorized users can access and modify the data.

## Usage
### Endpoints and Functionality
#### Admin Functions
1. **Assign Users to Manager Group**
   - **Endpoint**: `POST /api/groups/manager/users/`
   - **Headers**: Authorization: Token admin_token, Content-Type: application/json
   - **Body**:
     ```json
     {
         "username": "user_to_assign"
     }
     ```

2. **Add Menu Items**
   - **Endpoint**: `POST /menu-items/`
   - **Headers**: Authorization: Token admin_token, Content-Type: application/json
   - **Body**:
     ```json
     {
         "title": "New Item",
         "price": "9.99",
         "category": 1,
         "featured": true
     }
     ```

3. **Add Categories**
   - **Endpoint**: `POST /categories/`
   - **Headers**: Authorization: Token admin_token, Content-Type: application/json
   - **Body**:
     ```json
     {
         "title": "New Category",
         "slug": "new-category"
     }
     ```

#### Manager Functions
1. **Update Item of the Day**
   - **Endpoint**: `PUT /menu-items/{item_id}/`
   - **Headers**: Authorization: Token manager_token, Content-Type: application/json
   - **Body**:
     ```json
     {
         "title": "Updated Item",
         "price": "9.99",
         "category": 1,
         "featured": true
     }
     ```

2. **Assign Orders to Delivery Crew**
   - **Endpoint**: `PUT /orders/{order_id}/`
   - **Headers**: Authorization: Token manager_token, Content-Type: application/json
   - **Body**:
     ```json
     {
         "delivery_crew": 3
     }
     ```

#### Delivery Crew Functions
1. **Access Assigned Orders**
   - **Endpoint**: `GET /orders/`
   - **Headers**: Authorization: Token delivery_crew_token

2. **Update Order as Delivered**
   - **Endpoint**: `PUT /orders/{order_id}/`
   - **Headers**: Authorization: Token delivery_crew_token, Content-Type: application/json
   - **Body**:
     ```json
     {
         "status": true
     }
     ```

#### Customer Functions
1. **Register**
   - **Endpoint**: `POST /auth/users/`
   - **Headers**: Content-Type: application/json
   - **Body**:
     ```json
     {
         "username": "new_customer",
         "password": "customer_password",
         "email": "customer@example.com"
     }
     ```

2. **Log In**
   - **Endpoint**: `POST /auth/token/login/`
   - **Headers**: Content-Type: application/json
   - **Body**:
     ```json
     {
         "username": "customer_username",
         "password": "customer_password"
     }
     ```

3. **Browse All Categories**
   - **Endpoint**: `GET /categories/`
   - **Headers**: Authorization: Token customer_token

4. **Browse All Menu Items**
   - **Endpoint**: `GET /menu-items/`
   - **Headers**: Authorization: Token customer_token

5. **Browse Menu Items by Category**
   - **Endpoint**: `GET /menu-items/?category={category_id}`
   - **Headers**: Authorization: Token customer_token

6. **Paginate Menu Items**
   - **Endpoint**: `GET /menu-items/?page={page_number}`
   - **Headers**: Authorization: Token customer_token

7. **Sort Menu Items by Price**
   - **Endpoint**: `GET /menu-items/?ordering=price`
   - **Headers**: Authorization: Token customer_token

8. **Add Menu Items to Cart**
   - **Endpoint**: `POST /cart/menu-items/`
   - **Headers**: Authorization: Token customer_token, Content-Type: application/json
   - **Body**:
     ```json
     {
         "menuitem": 1,
         "quantity": 2,
         "unit_price": "9.99",
         "price": "19.98"
     }
     ```

9. **Access Previously Added Items in Cart**
   - **Endpoint**: `GET /cart/menu-items/`
   - **Headers**: Authorization: Token customer_token

10. **Place Orders**
    - **Endpoint**: `POST /orders/`
    - **Headers**: Authorization: Token customer_token, Content-Type: application/json
    - **Body**:
      ```json
      {
          "date": "2024-05-20",
          "status": false
      }
      ```

11. **Browse Own Orders**
    - **Endpoint**: `GET /orders/`
    - **Headers**: Authorization: Token customer_token

## Technologies Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.
- **Djoser**: A REST implementation of Django authentication system.
- **SQLite**: Small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- **Heroku**: Deployment platform for making the application accessible over the web.

## Credits
This project was developed as part of the Coursera Course API.
