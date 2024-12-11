# Library Management System

## Overview
This is a Flask-based REST API for managing a library system. It allows you to perform CRUD operations on books and members, and includes a basic token-based authentication mechanism. The project is designed to be simple and extendable.

---

## Features
1. **Books Management:**
   - Add new books.
   - View a list of all books.
   - Update book details.
   - Delete a book.

2. **Members Management:**
   - Add new members.
   - View a list of all members.
   - Update member details.
   - Delete a member.

3. **Authentication:**
   - Basic token-based authentication (dummy implementation).

---

## Setup Instructions

### Prerequisites
1. Python 3.7+ installed on your system.
2. Git installed on your system.
3. Postman installed for API testing.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dharmesh-kashyap/CURD_api.git
   cd CURD_api
   ```

2. Create and activate a virtual environment:
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```
   The application will start at `http://127.0.0.1:5000`.

![image](https://github.com/user-attachments/assets/08d0fb81-df05-4831-aa2c-e67516c3550f)


---

## Testing Instructions

### Using Postman
To test the API, follow the steps below:

#### 1. **GET /api/books** - Retrieve all books
   - Method: **GET**
   - URL: `http://127.0.0.1:5000/api/books`
   - Expected Response:
     ```json
     []
     ```

   **Screenshot:**
   ![image](https://github.com/user-attachments/assets/edf3d604-f6a5-4fb1-9e92-8158d0cd3078)


---

#### 2. **POST /api/books** - Add a new book
   - Method: **POST**
   - URL: `http://127.0.0.1:5000/api/books`
   - Body (JSON):
     ```json
     {
         "title": "Marathi pustak 2001",
         "author": "pathak sir",
         "isbn": "1234567890",
         "available_copies": 5
     }
     ```
   - Expected Response:
     ```json
     {
         "message": "Book added successfully"
     }
     ```

   **Screenshot:**
   ![image](https://github.com/user-attachments/assets/448e1bd1-8afa-43ef-a9f1-1dfe47cd879e)


---

#### 3. **PUT /api/books/<book_id>** - Update a book
   - Method: **PUT**
   - URL: `http://127.0.0.1:5000/api/books/1`
   - Body (JSON):
     ```json
     {
         "title": "Marathi Pustak 2001 (Updated)",
         "author": "pathak sir",
         "isbn": "1234567890",
         "available_copies": 10
     }
     ```
   - Expected Response:
     ```json
     {
         "message": "Book updated successfully"
     }
     ```

   **Screenshot:**
   ![image](https://github.com/user-attachments/assets/007ccefb-976f-48a9-8e33-0688f13af1b9)


---

#### 4. **DELETE /api/books/<book_id>** - Delete a book
   - Method: **DELETE**
   - URL: `http://127.0.0.1:5000/api/books/1`
   - Expected Response:
     ```json
     {
         "message": "Book deleted successfully"
     }
     ```

   **Screenshot:**
   ![image](https://github.com/user-attachments/assets/7fe714dc-791d-485b-8d41-0cfded25dac0)


---

#### 5. **GET /api/members** - Retrieve all members
   - Method: **GET**
   - URL: `http://127.0.0.1:5000/api/members`
   - Expected Response:
     ```json
     []
     ```

   **Screenshot:**
   ![image](https://github.com/user-attachments/assets/0a0b5117-3626-469b-b254-f8e842a8f135)

---

#### 6. **POST /api/members** - Add a new member
   - Method: **POST**
   - URL: `http://127.0.0.1:5000/api/members`
   - Body (JSON):
     ```json
     {
         "name": "Dharmesh Kashyap",
         "email": "dharmeshkashyap46@gmail.com",
         "joined_date": "2024-12-12"
     }
     ```
   - Expected Response:
     ```json
     {
         "message": "Member added successfully"
     }
     ```

   **Screenshot:**
   ![image](https://github.com/user-attachments/assets/320d6997-f30f-41db-8b58-276a68a08399)


---

#### 7. **POST /auth/login** - Authenticate user
   - Method: **POST**
   - URL: `http://127.0.0.1:5000/auth/login`
   - Body (JSON):
     ```json
     {
         "username": "admin",
         "password": "secretPass"
     }
     ```
   - Expected Response:
     ```json
     {
         "token": "<your_token>"
     }
     ```

   **Screenshot:**
   ![image](https://github.com/user-attachments/assets/0065fa97-06e9-4670-95f2-fc157ab1b75f)


---

### Using the Authentication Token
To access secured endpoints, include the token in the **Authorization** header:
1. Add a new header in Postman:
   - Key: `Authorization`
   - Value: `Bearer <your_token>`
2. Use the secured endpoints as described above.

---

## Screenshots
![image](https://github.com/user-attachments/assets/dd133626-2d55-4336-949e-5e1d357bcb35)


---


