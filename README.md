# Python FastAPI Super Simple Dev Environment

This is a super simple dev environment intended for Python FastAPI development. It uses Docker Compose to build and run the FastAPI application. I use this for quick prototyping and scaffolding of potential API projects.

## Necessary Installations

- Install Docker on your local machine: https://www.docker.com/get-started/
- Install Docker compose on your local machine: https://docs.docker.com/compose/install/
- Make sure to have your favorite IDE installed. I use VS Code: https://code.visualstudio.com/download

## Getting Started

- Clone this repo to your local machine
- Open a terminal and navigate to the directory where you cloned the repo
- Run `docker-compose up --build -d` to build and run the FastAPI application in detached mode
- Open a browser and navigate to http://0.0.0.0:80 to see the app running
- Open the repo in your favorite IDE and begin coding!