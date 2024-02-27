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

3. **Access the Web Application**  
After the containers are up and running, open a web browser and navigate to `http://localhost:80`. You should now be able to see the web application's login page. Enter the credentials to access the welcome screen, verifying that the application has been set up correctly and is connected to the PostgreSQL database.

Following these steps will ensure your application is running and accessible via your local machine.

4. **Stopping the Application**  
   To stop and remove all the running containers associated with your application, open a terminal, navigate to the directory containing your `docker-compose.yml` file, and execute the following command:
   
      ```bash
   docker compose down

## Prerequisites

Before building and launching the Docker containers, create a `.env` file in the root directory of your project with the following content, replacing `your_database`, `your_user`, and `your_password` with your actual PostgreSQL database name, user, and password:

```plaintext
POSTGRES_DB=your_database
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password


