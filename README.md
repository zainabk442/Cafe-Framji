

----------------------------------------
# ☕ Café Framji
Café Framji is a Python Flask-based café booking web application that I am developing as a practical Cloud and DevOps project. The project began as a simple Flask application focused on providing basic café-related functionality and has gradually evolved into an opportunity to apply real-world software development, infrastructure, security, containerization, automation, and cloud deployment practices.

The main idea behind the project is to take a working web application and understand what it takes to move it beyond a basic local development setup toward a more production-oriented application. Instead of building the application only from a development perspective, I am using Café Framji to explore how modern applications are developed, packaged, secured, deployed, monitored, and maintained in a cloud environment.

Throughout the development process, I am working with technologies and practices such as Python, Flask, Linux, Docker, Docker Compose, Git/GitHub, CI/CD, AWS, and infrastructure automation. The project also provides hands-on experience with areas such as application configuration, environment variables, database connectivity, containerization, networking, security considerations, deployment workflows, and troubleshooting.
A major focus of Café Framji is the progressive improvement of the application. Rather than trying to implement every technology at once, I am gradually introducing DevOps and cloud practices as the application develops. This allows me to understand not only how individual tools work, but also why they are used and how they fit together in a real application lifecycle.

The overall development journey can be viewed as :
Flask Application → Database & Backend → Security Improvements → Docker Containerization → CI/CD Automation → AWS Infrastructure → Cloud Deployment → Monitoring & Continuous Improvement

The project is intended to demonstrate my ability to combine application development with Cloud and DevOps practices, while also giving me practical experience in troubleshooting and managing the different components involved in deploying an application.
Ultimately, Café Framji is more than just a café booking application. It is a hands-on learning project where I am continuously transforming a simple web application into a production-style Cloud/DevOps project, while documenting the technologies, challenges, solutions, and improvements along the way.
----------------------------------------
## 🚀 Project Overview

Café Framji is a café website with a table reservation system and an authenticated administrative dashboard. Customers can submit table booking requests through the website, while an administrator can securely access a dashboard to view and manage those bookings.

The application currently demonstrates :
- Flask backend development
- SQLite database integration
- Form handling
- CRUD operations
- Admin authentication
- Session-based login using Flask-Login
- Environment variable management
- Basic application security practices
- Git/GitHub version control
The project is being developed incrementally, with Docker, CI/CD, AWS and Terraform planned as the next stages.

----------------------------------------
# ✨ Current Features — V1
## 🌐 Customer Website

The application includes multiple frontend pages :
- Home
- Menu
- Gallery
- Our Story
- Table Booking

The frontend is built using :
- HTML
- CSS
- JavaScript

Flask routes are used to serve the different pages instead of directly linking HTML files.

----------------------------------------
## 📅 Table Booking System

Customers can submit a reservation through the booking form.
The form collects :
- Name
- Phone number
- Date
- Time
- Number of guests
- Optional message
The submitted information is sent to the Flask backend using a `POST` request.

Example request flow :
Customer
   ↓
Booking Form
   ↓
POST /booking
   ↓
Flask Backend
   ↓
SQLite Database
   ↓
Booking Stored