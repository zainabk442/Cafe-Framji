

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
## ⚙️ Automated CI + Testing + Docker Build + Docker Hub

In V4, I implemented a GitHub Actions workflow to automate the Docker image build and publishing process for the Café Framji Flask application. I created a workflow file at .github/workflows/docker-build-push.yml, which is triggered whenever code is pushed to the main branch. The workflow checks out the repository, logs in to Docker Hub using GitHub Secrets, builds the Docker image using the project's Dockerfile, and pushes the image to my Docker Hub repository.
I verified that the workflow runs successfully in GitHub Actions and that the latest image is available in Docker Hub. This automation reduces the need to build and publish the image manually whenever the application code is updated. The published image can then be used in a later deployment stage, such as deploying the application to Amazon ECS.

Automated Testing with Pytest : 
As part of the CI process, I added automated tests using pytest to verify the functionality of the Café Framji application.
The test suite currently contains 5 automated tests, and all 5 tests passed successfully during local testing and in the GitHub Actions workflow. The CI pipeline now verifies that the application tests pass before continuing with the Docker image build and publishing process.

The testing flow is:

Code Push
    ↓
GitHub Actions
    ↓
Install Dependencies
    ↓
Run Pytest
    ↓
5 Tests Passed 
    ↓
Docker Build
    ↓
Docker Hub Push

This ensures that the Docker image is built and published only after the automated tests have successfully completed.
I verified that the complete workflow runs successfully in GitHub Actions and that the latest image is available in Docker Hub. This automation reduces the need to build and publish the image manually whenever the application code is updated. The published image can then be used in a later deployment stage, such as deploying the application to Amazon ECS.

The final V4 CI/CD architecture is:

                        Café Framji
                             │
                             ↓
                     GitHub Repository
                             │
                    Code Push / Changes
                             │
                             ↓
                     GitHub Actions
                             │
                             ↓
                    ┌────────┴────────┐
                    │                 │
                    ↓                 ↓
                   CI            Docker Build
                    │                 │
                    ↓                 ↓
             Install Dependencies   Docker Image
                    │                 │
                    ↓                 │
               Run Pytest             │
                    │                 │
                    ↓                 │
              5 Tests Passed          │
                    │                 │
                    └────────┬────────┘
                             │
                             ↓
                     Docker Hub Login
                             │
                      GitHub Secrets
                             │
                             ↓
                        Docker Hub
                             │
                             ↓
                  Café Framji Docker Image

The most important outcome of this stage is that the testing, Docker image build, and publishing process is now automated.
Instead of manually running tests, building and pushing the image after every change, GitHub Actions performs these steps automatically after code is pushed to the repository. This creates a reliable CI/CD workflow and provides a foundation for the AWS deployment stage in V5.

----------------------------------------

# 🚀 V5 — Amazon ECS + AWS Fargate
## ☁️ Containerized Deployment + CloudWatch Monitoring
In V5, I deployed the Café Framji Flask application to Amazon ECS using AWS Fargate. The Docker image created and published during V4 was used as the application container image for the ECS deployment.
The main objective of V5 was to move the application from a local Docker environment to a managed AWS container platform without managing EC2 servers manually.

The deployment uses :
* Amazon ECS
* AWS Fargate
* Docker
* Docker Hub
* Amazon CloudWatch Logs
* ECS Task Definition
* ECS Cluster
* Environment Variables

DOCKER IMAGE DEPLOYMENT : 
The Docker image generated by the V4 GitHub Actions pipeline was used for the V5 ECS deployment.
The image is available in my Docker Hub repository : zainabk10/cafe-framji:latest
Instead of building the application directly inside AWS, ECS retrieves the existing Docker image and uses it to create the running application container. This demonstrates how a CI/CD pipeline can produce a container image that is later consumed by a cloud deployment platform.

AWS ECS CLUSTER : 
I created an Amazon ECS cluster for the Café Framji application :
Cluster Name :
cafe-framji-cluster

Amazon ECS is used to manage the containerized application, while AWS Fargate provides the compute environment required to run the container. The ECS cluster acts as the logical grouping for the application's ECS services and tasks.

AWS FARGATE : 
For the V5 deployment, I used the Fargate launch type. AWS Fargate allows the container to run without manually creating or maintaining EC2 instances.
Instead of managing : 
EC2 Instance> Operating System> Docker Installation> Docker Container

Fargate provides the managed compute layer :
Amazon ECS> AWS Fargate> Docker Container> Café Framji Application
This allowed me to focus on the container, task definition, networking, and application configuration rather than managing the underlying server.

ECS TASK DEFINITION : 
I created an ECS task definition to describe how the Café Framji container should run.
The task definition specifies the container configuration, including :
* Container image
* Container name
* Container port
* CPU and memory configuration
* Environment variables
* CloudWatch logging configuration

The ECS task definition used for the deployment was updated during the V5 setup.
Example task definition revision : cafe-framji-task:3
Each new task definition revision represents a new version of the container configuration.

For example :
cafe-framji-task:1
        ↓
cafe-framji-task:2
        ↓
cafe-framji-task:3

This provides versioning for the ECS application configuration.

Environment Variables : 
The application configuration is passed to the container using environment variables rather than hard-coding configuration directly into the application.This keeps configuration separate from the application code and makes the container easier to deploy in different environments. The `.env` file and local database are not pushed to GitHub.

CLOUDWATCH LOGGING : 
As part of V5, I configured Amazon CloudWatch Logs for the ECS container.
The ECS task sends container output to CloudWatch so that application activity can be monitored from AWS.

The logging flow is :
Café Framji Container
        ↓
Container Logs
        ↓
ECS Logging Configuration
        ↓
Amazon CloudWatch Logs

This allows me to inspect application logs without directly accessing the underlying server.
CloudWatch can be used to investigate application startup messages, requests, errors, and other container output.

Monitoring the ECS Task : 
After deploying the task, I verified the ECS environment through the Amazon ECS console.
The ECS cluster provides visibility into :
* Running tasks
* Task status
* Task definition revision
* Container status
* CPU and memory configuration
* Network configuration
* Container logs

A new ECS task receives a new task ID when it is launched. For example :
Previous Task
795d103.....

        ↓

New ECS Task
New Task ID

The task ID changing is normal because each task represents a running instance of the container.
The task definition revision, such as : cafe-framji-task:3
identifies the configuration used to launch the task.

V5 Deployment Architecture : 
                         Café Framji
                              │
                              ↓
                       GitHub Repository
                              │
                              ↓
                       GitHub Actions
                              │
                              ↓
                        Docker Build
                              │
                              ↓
                         Docker Hub
                              │
                              ↓
                    Café Framji Docker Image
                              │
                              ↓
                    Amazon ECS Task Definition
                              │
                              ↓
                    Amazon ECS Cluster
                    cafe-framji-cluster
                              │
                              ↓
                         AWS Fargate
                              │
                              ↓
                    Café Framji Container
                              │
                              ↓
                    Amazon CloudWatch Logs
                              │
                              ↓
                       Application Logs


Complete V4 → V5 Flow : 
Developer
    │
    ↓
GitHub Repository
    │
    ↓
GitHub Actions
    │
    ├── Install Dependencies
    │
    ├── Run Pytest
    │
    ├── Docker Build
    │
    └── Docker Hub Push
             │
             ↓
        Docker Hub
             │
             ↓
      Docker Image
             │
             ↓
   Amazon ECS Task Definition
             │
             ↓
      ECS Cluster
             │
             ↓
        AWS Fargate
             │
             ↓
     Café Framji Container
             │
             ↓
    Amazon CloudWatch Logs

The main outcomes of this stage are :
* Deployed the Dockerized Café Framji application to Amazon ECS.
* Used AWS Fargate to run the application container.
* Created an ECS cluster for the application.
* Created and configured an ECS task definition.
* Used the Docker image published during V4 as the deployment image.
* Configured container logging with Amazon CloudWatch.
* Verified ECS task and container status through the AWS console.
* Learned how ECS tasks and task definition revisions work.
* Learned how CloudWatch can be used to inspect container logs.

V5 demonstrates the transition from a locally containerized Flask application to a cloud-based container deployment using AWS managed services. The project now follows a more complete DevOps workflow :
Code
 ↓
GitHub
 ↓
CI / Testing
 ↓
Docker Build
 ↓
Docker Hub
 ↓
ECS / Fargate Deployment
 ↓
CloudWatch Monitoring

The V5 deployment provides the foundation for the next stage of the project, where the AWS infrastructure can be managed using Terraform instead of being created manually through the AWS Console.


