## Multi-Agent Insurance System Deployment on Kubernetes

### Project Description

his project implements a small **web-based Multi-Agent Insurance System** that helps users find suitable insurance policies. Multiple agents are simulated in the backend using Python Flask logic:

- An **Input Agent** validates user data such as age, income, and risk preference.
- A **Recommendation Agent** scores and selects the best matching policies from a predefined JSON dataset.
- A **Comparison Agent** presents the top policies side-by-side in a clear comparison table.
- A **Query Agent** powers a simple chat assistant using rule-based responses to common insurance questions.

  The application is containerized using **Docker** to create an image and run it inside a container, making it easy to deploy and run consistently across different environments.


### Project Overview

Users interact with a modern, responsive web UI to:

- Enter personal and financial details.
- Choose the desired insurance type and coverage.
- Receive top 3 recommended policies along with a comparison table.
- Chat with a simple assistant about coverage, hospitalization, accident benefits, and claims.

On the backend, Flask exposes REST APIs (`/recommend`, `/compare`, `/chat`) that implement the simulated agent logic on top of a JSON-based policy dataset. Docker is used only for **containerizing the Flask application**—building an image and running a container—without any Kubernetes or advanced orchestration.

### Objectives

- **Deploy** a containerized Insurance Rust application on a Kubernetes cluster.
- **Implement** Kubernetes `Deployment` and `Service` manifests for application management.
- **Ensure** high availability and scalability of the application.
- **Implement** rolling update strategy to achieve zero-downtime updates.
- **Demonstrate** container orchestration using Minikube for local development and testing.

### Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, vanilla JavaScript
- **Data store**: `policies.json`
- **Containerization**
  - Docker
- **Version Control**
  - Git
  - GitHub


### Features

- **Landing page** explaining the multi-agent concept.
- **User input form** for age, income, family members, insurance type, coverage amount, and risk preference.
- **Agents (simulated)**:
  - **Input Agent**: validates input.
  - **Recommendation Agent**: scores and picks the top 3 matching policies.
  - **Comparison Agent**: renders a comparison table.
  - **Query Agent**: answers questions with rule-based responses.
- **Chat assistant** with predefined, rule-based answers.

### Project Structure

```text
project/
  app.py
  policies.json
  requirements.txt
  templates/
      index.html
      form.html
      result.html
  static/
      style.css
      script.js
```


### Team Members

| # | Name               | Enrollment No   |
|---|--------------------|-----------------|
| 1 | Naman Mehta        | EN22CS301629    |
| 2 | Naman Raghuvanshi  | EN22CS301632    |
| 3 | Nishkarsh Sharma   | EN22CS301659    |
| 4 | Mustafa Shaikh     | EN22CS301624    |
| 5 | Nandini Sharma     | EN22CS301635    |

### Conclusion

This project demonstrates how a multi-agent insurance recommendation concept can be built using a simple Flask backend, a JSON dataset, and a clean HTML/CSS/JavaScript frontend. The agents are simulated with rule-based and heuristic logic, providing a clear educational example without requiring real AI models.

Docker is used to package the entire application into an image and run it inside a container, ensuring consistent deployment on any machine with Docker Desktop installed. This showcases practical containerization of a small web app without adding the complexity of Kubernetes or other orchestration platforms.


