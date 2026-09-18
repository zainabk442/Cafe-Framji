

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

In V1, I built the Café Framji web application using Flask, with HTML, CSS, and JavaScript for the frontend and SQLite for storing booking data. I created multiple customer-facing pages including Home, Menu, Gallery, Our Story, and Table Booking, and used Flask routes to serve these pages through the backend. I also implemented the table booking system, where customers can submit their name, phone number, date, time, number of guests, and an optional message through a booking form. The submitted data is sent to the Flask backend using a POST request and stored in the SQLite database. 

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

Customers can submit a reservation through the booking form. The form collects the following information :
- Name
- Phone number
- Date
- Time
- Number of guests
- Optional message
The submitted information is sent to the Flask backend using a `POST` request and stored in the SQLite database.

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

## 🔐 Admin Login & Booking Management 
The application also includes a secure Admin Login system that allows authorized administrators to access the booking management page. After logging in, the admin can view all customer table reservations submitted through the website, including details such as the customer name, contact information, booking date, time, number of guests, and any additional message. This provides a simple interface for the café to manage and monitor table bookings from one place.



----------------------------------------
# 🐳 V2 — Docker Containerization
## 📦 Containerized it + protected database with a persistent Docker volume

I containerized the Café Framji Flask application using Docker. I created a Dockerfile to define the Python environment, install the application's dependencies, copy the project files, and configure the Flask application to run on port 5000. I then built the Docker image and used it to create and run the Café Framji container. Since the application uses SQLite for storing booking data, I also implemented a Docker named volume called cafe-framji-db-data and mounted it at /app/data. I moved the working SQLite database into this volume and verified that both the database file and existing booking records were available from the volume. This ensures that the booking data remains persistent even if the application container is deleted and recreated.

The Docker implementation includes :
- Dockerfile
- Docker Image
- Docker Container
- Docker Volume
- Environment Variables
- Port Mapping

Through V2, the following Docker concepts were implemented and practiced :
Dockerfile : 
Defines how the application environment and Docker image are built.

Docker Image :
A packaged version of the Café Framji application and its dependencies.

Docker Container : 
A running instance of the Docker image.

Port Mapping : 
Connects the Flask application's container port to the host machine.

Docker Volume :
Provides persistent storage that exists independently from the container lifecycle.

Persistent Database : 
The SQLite database is stored in the Docker named volume so that booking data remains available when the application container is removed and recreated.

Temporary Containers : 
Temporary Alpine and Python containers were used to perform database copying and verification without modifying the main Café Framji application container.

V2 Outcome : By completing V2, Café Framji was transformed from a locally running Flask application into a Dockerized application with persistent database storage.

The final Docker architecture is :

                    Café Framji
                         │
                         ↓
                    Dockerfile
                         │
                         ↓
                   Docker Image
                         │
                         ↓
              cafe-framji-container
                         │
            ┌────────────┴────────────┐
            │                         │
            ↓                         ↓
      Flask Application          /app/data
            │                         │
            ↓                         ↓
        Port 5000             cafe-framji-db-data
                                      │
                                      ↓
                               cafe_framji.db
                                      │
                                      ↓
                                Booking Data

The most important outcome of this stage is that the application container can be removed and recreated without losing the SQLite booking database, because the database is stored separately in the persistent Docker volume.



----------------------------------------
# ⚙️ V3 — Docker Compose
## 🧩 Simplified Container Management + Persistent Database

In V3, I introduced **Docker Compose** to simplify the management of the Café Framji Flask application and its persistent SQLite database. I created a `compose.yaml` file that defines the application service, builds the Docker image using the existing Dockerfile, maps port 5000 between the container and host machine, loads environment variables from the `.env` file, and connects the application to the existing `cafe-framji-db-data` Docker named volume. This allows the complete Docker configuration to be managed from a single Compose file instead of running multiple Docker commands manually. I also tested starting, stopping, rebuilding, and recreating the application using Docker Compose and verified that the existing SQLite database and booking records remained available through the persistent volume.

The Docker Compose implementation includes :
* `compose.yaml`
* Application Service
* Docker Image Build
* Container Management
* Port Mapping
* Environment Variables
* Docker Named Volume
* Persistent SQLite Database
* Container Recreation

Through V3, the following Docker Compose concepts were implemented and practiced :
Docker Compose :
Used to define and manage the Café Framji application and its Docker configuration from a single `compose.yaml` file.

Compose Service :
Defines the Café Framji application container, including its build configuration, ports, environment variables, and volume.

Build Configuration :
Docker Compose uses the existing `Dockerfile` to build the Café Framji application image.

Port Mapping :
Maps the Flask application's container port `5000` to port `5000` on the host machine, allowing the application to be accessed through the browser.

Environment Variables :
The `.env` file is loaded through Docker Compose so that application configuration is kept separate from the Compose configuration.

Named Volume :
The existing `cafe-framji-db-data` Docker volume is attached to the application so that the SQLite database remains outside the container's writable layer.

Persistent Database :
The SQLite database and booking records remain stored in the Docker named volume, allowing the data to survive container removal and recreation.

Container Lifecycle :
Docker Compose was used to start, stop, rebuild, and recreate the Café Framji application without manually repeating individual Docker commands.

V3 Outcome :
By completing V3, the Café Framji Docker setup was converted from manually managed Docker commands into a Docker Compose-based application configuration. The application, environment variables, port mapping, and persistent database volume can now be managed from a single `compose.yaml` file. The existing booking data was also verified after rebuilding and recreating the application container.

The final V3 Docker Compose architecture is :

                         Café Framji
                              │
                              ↓
                       compose.yaml
                              │
                              ↓
                    Docker Compose Service
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ↓                         ↓
          Dockerfile Build            Environment
                 │                    Variables (.env)
                 ↓
             Docker Image
                 │
                 ↓
       cafe-framji-container
                 │
        ┌────────┴────────┐
        │                 │
        ↓                 ↓
 Flask Application    /app/data
        │                 │
        ↓                 ↓
    Port 5000      cafe-framji-db-data
                          │
                          ↓
                    cafe_framji.db
                          │
                          ↓
                     Booking Data

The most important outcome of this stage is that Docker Compose now manages the Café Framji application configuration while the SQLite database remains persistent through the Docker named volume. This provides a cleaner and more reproducible Docker setup and creates the foundation for the GitHub Actions CI/CD stage in V4.




----------------------------------------
# 🚀 V4 — GitHub Actions
## ⚙️ Automated CI + Docker Build + Docker Hub

