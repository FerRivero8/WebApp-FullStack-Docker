# WebApp-FullStack-Docker

WebApp-Containerized is an innovative project designed to streamline the development, deployment, and scaling of web applications using Docker and Python. The project structure includes a backend service, a PostgreSQL database, and an Nginx web server, all containerized with Docker for easy setup and scalability.

## Application Overview

This application is designed to launch a web interface featuring a login system. Upon entering the correct credentials, which are verified against a PostgreSQL database, users are granted access to a welcome screen. This initial authentication step ensures secure access and a personalized user experience.

## Getting Started

To get the application up and running on your system, follow these simple steps:

1. **Build the Docker Containers**  
   Navigate to the directory containing the `docker-compose.yml` file and run the following command to build the Docker containers:
   
   ```bash
   docker compose build

This command builds all the necessary Docker images as defined in your `docker-compose.yml`.

2. **Launch the Containers**  
Once the build process is complete, start up the containers using:

     ```bash
      docker compose up

This command starts all the services defined in your `docker-compose.yml`, including the web application, database, and any other services your application depends on.



