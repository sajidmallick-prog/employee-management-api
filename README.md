🏢 Employee Management REST API
This is a simple backend system for managing employees in a company, built using Django, Django REST Framework, and JWT-based authentication. The project focuses on RESTful CRUD operations, authentication, testing, and clean API design.

📦 Features
* User authentication using JWT (SimpleJWT)
* Employee CRUD operations (Create, Read, Update, Delete)
* Protected APIs (only authenticated users can access)
* Validation for unique fields (like email)
* Proper HTTP status codes and error handling
* Unit tests for all endpoints and edge cases
* Environment variable support using .env

🛠️ Tech Stack
* Python 3.x
* Django 5.x
* Django REST Framework
* SQLite / PostgreSQL
* djangorestframework-simplejwt
* python-decouple
* Postman (for API testing)

🚀 How to Run This Project
1️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Setup Environment Variables
Create a .env file in the project root (same level as manage.py)

SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=employee_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
⚠️ For SQLite, database config is optional.

4️⃣ Run Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (Optional)

python manage.py createsuperuser

6️⃣ Run the Server

python manage.py runserver
Server will start at: 👉 http://127.0.0.1:8000/

📮 API Endpoints
🔐 Authentication (JWT)
Method	Endpoint	Description
POST	/api/token/	Login & get access + refresh token
POST	/api/token/refresh/	Refresh access token
👨‍💼 Employees API
Method	Endpoint	Description
POST	/api/employees/	Create employee
GET	/api/employees/	List all employees
GET	/api/employees/<id>/	Retrieve single employee
PUT	/api/employees/<id>/	Update employee
DELETE	/api/employees/<id>/	Delete employee
🔐 Authorization
All employee endpoints are protected.
Add this header in Postman:

Authorization: Bearer <your_access_token>

🧪 Testing
✅ Run Tests

python manage.py test
🔍 Covered Test Cases
* Create employee successfully
* Prevent duplicate email creation
* Retrieve employee list
* Retrieve single employee
* Update employee
* Delete employee
* Unauthorized access without token

📧 Contact If you want to suggest improvements or have any issues, feel free to reach out to me 

📩 Email:sajidmallick204@gmail.com

💼 LinkedIn: www.linkedin.com/in/sajid-mallick-444215248 📱 Phone: +91-9749371880
