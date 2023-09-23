<h1>To-Do List App</h1>
<h3>Table of Contents:</h3> 

 
Description

Installation 

Project Overview

Screenshots preview

Technologies used 

Contributing 

Creation process 

License

---
<h3>Description:</h3> 

Welcome to the CRM (Customer Relationship Management) App, a straightforward yet effective customer management application designed to assist you in organizing and maintaining customer data.


 ---


<h3>Installation:</h3> 

 

To run gym management system, follow these steps: 

 

Clone the repository on your machine: 

 
	git clone https://github.com/pavle0402/CRM-django-app.git

 

Navigate to the project directory: 

cd your-path-to-gymmanagementsystem 

 

3. Create a virtual environment (optional but recommended) and activate it: 

python –m venv venv 

 

 

4. Activate your virtual environment: 

On windows: 

venv/Scripts/activate 

 

On macOS/Linux: 

Source venv/bin/activate 

 

5. Install project dependencies: 
	pip install –r requirements.txt 

 

6. Configure database connections in settings.py. 

 

7. Apply database migrations: 

py manage.py migrate 

 

8. Create superuser(staff) account: 

py manage.py createsuperuser(then you will be asked to provide 	username, email and password) - creating staff user


9. Start a development server: 

py manage.py runserver 

 

Application should now be running on: http://localhost:8000. 

 

 
---
<h3>Project overview</h3>

This CRM App was created as one of my initial Django projects, with a primary focus on fundamental web development concepts. 
It encompasses essential features such as user authentication, user registration, and user logout, providing a secure environment for managing customer information.

---
  
<h3>Key Features:</h3> 

### User Authentication

- **Registration**: Users can create an account by providing necessary details.
- **Login**: Securely access the CRM system with your registered credentials.
- **Logout**: Log out of your account when your CRM tasks are complete.

### Customer Management

- **Customer Table**: The heart of the application, displaying a tabular view of all your customers and their relevant information.
- **Add Customer**: Easily expand your customer database by adding new customer entries.

 ---

<h3>Technologies used</h3> 

- Frontend: HTML, CSS
- Backend: Django
- Database: SQLite(django's default)

  ---


<h3>Contributing</h3> 

Contributions to the project are welcome! If you would like to contribute, please follow these guidelines: 

Fork the repository. 

Create a new branch for your feature or bug fix. 

Make your changes and commit them with descriptive messages. 

Push your branch to your fork. 

Submit a pull request with a clear explanation of your changes. 

 
 ---

<h3>Creation Process:</h3>

This was one of my first apps i made with django, and at the time i was still learning fundamental web concepts and CRUD basically. 
It is not advanced at all, but as i said in my previous projects, it represents my journey toward becoming web developer.

---

## License

This project operates under the [MIT License](LICENSE).

---

Thank you for checking out the To-Do List App. Feel free to explore and use it for your task management needs.

For any questions or inquiries, contact me at your.email@example.com.

