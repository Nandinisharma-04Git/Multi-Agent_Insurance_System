## Multi-Agent Insurance System Deployment on Kubernetes

### Project Description

This project focuses on orchestrating the deployment of an Insurance Rust-based application onto a Kubernetes cluster using Minikube. The system uses containerized workloads managed through Kubernetes `Deployment` and `Service` manifests to ensure efficient application lifecycle management.

A key feature of the implementation is **zero-downtime rolling updates**, which allows seamless upgrades of application versions without interrupting service availability for end users. This ensures reliability, scalability, and continuous operation of the system during updates.

### Project Overview

The project demonstrates how modern container orchestration platforms like Kubernetes can be used to deploy and manage applications efficiently. The Insurance application is containerized using Docker and deployed to a local Kubernetes cluster (Minikube).

Kubernetes deployment strategies ensure that updates to the application occur gradually without affecting running services. The system also includes service configurations to expose the application and manage network communication between components.

This implementation highlights container orchestration, deployment automation, and high availability practices commonly used in real-world production environments.

### Objectives

- **Deploy** a containerized Insurance Rust application on a Kubernetes cluster.
- **Implement** Kubernetes `Deployment` and `Service` manifests for application management.
- **Ensure** high availability and scalability of the application.
- **Implement** rolling update strategy to achieve zero-downtime updates.
- **Demonstrate** container orchestration using Minikube for local development and testing.

### Tech Stack

- **Programming Language**
  - Rust
- **Containerization**
  - Docker
- **Container Orchestration**
  - Kubernetes
  - Minikube
- **Deployment & Infrastructure**
  - Kubernetes Deployment YAML
  - Kubernetes Service YAML
- **Version Control**
  - Git
  - GitHub

### Key Features

- **Containerized Rust Insurance Application**
- **Kubernetes Deployment and Service Configuration**
- **Zero-downtime rolling updates**
- **Scalable container orchestration**
- **Automated application lifecycle management**
- **Local Kubernetes environment using Minikube**
- **Reliable and consistent deployment strategy**

### Team Members

| # | Name               | Enrollment No   |
|---|--------------------|-----------------|
| 1 | Naman Mehta        | EN22CS301629    |
| 2 | Naman Raghuvanshi  | EN22CS301632    |
| 3 | Nishkarsh Sharma   | EN22CS301659    |
| 4 | Mustafa Shaikh     | EN22CS301624    |
| 5 | Nandini Sharma     | EN22CS301635    |

### Conclusion

This project demonstrates the practical implementation of container orchestration using Kubernetes for deploying and managing a Rust-based application. By implementing rolling updates and service management, the system ensures continuous availability and reliable deployment.

The project highlights how Kubernetes can be used to manage modern applications efficiently while maintaining scalability, reliability, and minimal service disruption during updates.

