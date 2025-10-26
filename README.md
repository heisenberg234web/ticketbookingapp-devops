# DevOps Assignment 2 – Ticket Booking Platform with CI/CD Pipeline

![Python](https://img.shields.io/badge/python-3.10+-blue)  
![Flask](https://img.shields.io/badge/flask-2.x-green)  
![Docker](https://img.shields.io/badge/docker-latest-blue)  
![Jenkins](https://img.shields.io/badge/jenkins-latest-orange)  
![Kubernetes](https://img.shields.io/badge/kubernetes-latest-lightblue)  
![CI/CD](https://img.shields.io/badge/CI%2FCD-pipeline-red)

A production-ready Flask web application for movie ticket booking, with a complete DevOps workflow including Docker, Jenkins, and Kubernetes deployment.

---

## Overview

This project demonstrates a full DevOps workflow for a Flask web application, including:

- Containerization using Docker  
- Automated CI/CD pipeline with Jenkins  
- Orchestration using Kubernetes  
- Automated testing and deployment stages  

---

## About the Web Application

The Movie Ticket Booking Platform allows users to:

- Browse currently playing movies  
- Check showtimes and seat availability  
- Select preferred seats  
- Complete bookings with secure payment options (or simulated payment flow)  

It offers a responsive UI with real-time seat selection, intuitive navigation, and a seamless booking experience.

---

## ✨ Features

- **Flask Web Application**: Lightweight Python web server  
- **Docker Containerization**: Multi-stage Docker builds for optimized image sizes  
- **Kubernetes Deployment**: Production-ready manifests (deployments, services, load balancing)  
- **Jenkins Pipeline**: Automates build, test, push, and deployment  
- **Docker Hub Integration**: Automated image push to registry  
- **Health Checks**: Application health monitoring  
- **Load Balancing**: Kubernetes Service (LoadBalancer type) for external access  

---

## Architecture
          ┌──────────────────────────┐
          │     GitHub Repo          │
          │ heisenberg234web/ticketbookingapp-devops │
          └───────────┬──────────────┘
                      │
                      ▼
          ┌──────────────────────────┐
          │        Jenkins           │
          │   CI/CD Pipeline         │
          └───────────┬──────────────┘
                      │
                      ▼
          ┌──────────────────────────┐
          │       Docker Hub         │
          │  (TicketBookingApp Image)│
          └───────────┬──────────────┘
                      │
                      ▼
          ┌──────────────────────────┐
          │   Kubernetes Cluster     │
          │ (App Pods, Service, Ingress) │
          └───────────┬──────────────┘
                      │
                      ▼
          ┌──────────────────────────┐
          │     End Users / Clients  │
          │ (Access via LoadBalancer │
          │     or NodePort URL)     │
          └──────────────────────────┘

This shows how code flows: from GitHub → CI/CD → image registry → Kubernetes → end-users.

---

## 📌 Prerequisites
```

Make sure the following are installed before running locally:

- **[Python 3.10+](https://www.python.org/downloads/)** – Required to run the Flask application
- [**Docker**](https://docs.docker.com/get-docker/) – For containerizing the app
- [**Kubernetes CLI (`kubectl`)**](https://kubernetes.io/docs/tasks/tools/) – To manage Kubernetes clusters
- [**Minikube (optional)**](https://minikube.sigs.k8s.io/docs/start/) – For running a local Kubernetes cluster
- [**Jenkins**](https://www.jenkins.io/download/) – For setting up the CI/CD pipeline
- [**Git**](https://git-scm.com/downloads) – Version control and cloning the repository
```


---

## 📁 Project Structure
```
ticketbookingapp-devops/
│
├── app/ # Flask web application code
│ ├── static/ # CSS / JS / images
│ ├── templates/ # HTML templates
│ ├── app.py # Main Flask entry point
│ └── requirements.txt # Python dependencies
│
├── Dockerfile # Docker build instructions
├── Jenkinsfile # CI/CD pipeline definition
├── .gitignore # Files to ignore
│
├── k8s/ # Kubernetes deployment files
│ ├── deployment.yaml
│ └── service.yaml
│
├── screenshots/ # Screenshots for documentation
└── README.md # This documentation file
```
...

## 📁 Screenshots
```
├── 1. Jenkins Pipeline Configuration  
│   └── Jenkins job configuration showing Git repository integration and build triggers  
│
├── 2. Docker Hub Repository  
│   └── Docker Hub repository showing the successfully pushed container image  
│
├── 3. GitHub Repository Structure  
│   └── Source code structure on GitHub showing the Flask application and configuration files  
│
├── 4. Kubernetes Deployment  
│   └── Kubernetes service deployment using Minikube with accessible service URL  
│
├── 5. Jenkins Pipeline Execution  
│   └── Successful Jenkins pipeline execution with all stages completed  
│
└── 6. Application Website  
    └── CineBook application homepage showing available movies and booking options
```



## 📁 Docker Deployment
```

├── 🧱 Build the Docker Image  
│   └── `docker build -t heisenberg234web/ticketbookingapp-devops:latest .`  
│
└── 🚀 Run the Container Locally  
    └── `docker run -d -p 5000:5000 heisenberg234web/ticketbookingapp-devops:latest`
```



## 📁 Push to Docker Hub
```

├── 🏷️ Tag Docker Image  
│   └── `docker tag heisenberg234web/ticketbookingapp-devops:latest <your-dockerhub-username>/ticketbookingapp-devops:latest`  
│
├── 🔑 Login to Docker Hub  
│   └── `docker login`  
│
└── 📤 Push Docker Image  
    └── `docker push <your-dockerhub-username>/ticketbookingapp-devops:latest`
```


## 📁 Kubernetes Deployment
```

├── 🟢 Start Minikube (local testing)  
│   └── `minikube start`  
│
├── 📄 Apply Kubernetes Manifests  
│   └── `kubectl apply -f k8s/`  
│
├── 🔍 Check Deployment Status  
│   ├── `kubectl get pods`  
│   └── `kubectl get services`  
│
├── 📈 Scale Deployment (optional)  
│   └── `kubectl scale deployment ticket-booking-app --replicas=3`  
│
└── 🗑️ Clean Up  
    └── `kubectl delete -f k8s/`
```

## 📁 CI/CD Pipeline
```

├── 1️⃣ Checkout Code  
│   └── Clone the latest code from GitHub repository  
│
├── 2️⃣ Build Docker Image  
│   └── Build using Dockerfile  
│
├── 3️⃣ Run Tests  
│   └── Run automated tests or health-check scripts  
│
├── 4️⃣ Push to Docker Registry  
│   └── Push built image to Docker Hub  
│
└── 5️⃣ Deploy to Kubernetes  
    └── Apply manifests to update application deployment
```

## 📁 Jenkins Setup
```

├── ⚙️ Install Jenkins and Required Plugins  
│   └── Docker Pipeline, Kubernetes CLI, Git  
│
├── 🔑 Configure Credentials  
│   ├── Docker registry credentials  
│   └── Kubernetes config (if required)  
│
├── 🏗️ Create Pipeline Job  
│   └── Point to GitHub repository + Jenkinsfile  
│
└── ▶️ Run Pipeline  
    └── Monitor stages and logs for build, test, push, deployment
```
👤 Author & Contributions
```
├── Author: Maheshwaram Sai Ruthwik
├── GitHub: https://github.com/heisenberg234web
├── Docker Hub: https://hub.docker.com/u/heisenberg123
│
├── Contributions:
│   ├── Developed the Flask web application
│   ├── Created Dockerfile and containerized the application
│   ├── Set up Jenkins CI/CD pipeline
│   ├── Wrote Kubernetes manifests for deployment and service
│   ├── Added documentation and screenshots for README
│   └── Ensured end-to-end DevOps workflow from code to deployment
```




