# DevOps Metrics Monitoring Tool 
📌 DevOps Metrics Monitoring Tool
🚀 A Kubernetes-based monitoring system using Prometheus, Grafana, Jenkins, and ArgoCD for automated CI/CD deployment.
📂 Project Structure
📂 devops-metrics/
│── 📂 k8s/                 # Kubernetes YAML Manifests
│   ├── postgres-deployment.yaml
│   ├── flask-app-deployment.yaml
│   ├── prometheus-deployment.yaml
│   ├── grafana-deployment.yaml
│   ├── argocd-app.yaml
│── 📂 app/                 # Flask API (Backend)
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│── 📂 jenkins/             # Jenkins CI/CD
│   ├── Jenkinsfile
│── 📂 dashboards/          # Grafana Dashboards
│   ├── kubernetes-dashboard.json
│── 📜 .gitignore           # Ignore unnecessary files
│── 📜 README.md            # Project Documentation
🚀 Features
✅ Metrics Collection - Captures system performance data using Prometheus.
✅ Real-time Monitoring - Visualizes data with Grafana dashboards.
✅ Automated CI/CD - Uses Jenkins & ArgoCD for continuous deployment.
✅ Containerized App - Built with Flask & deployed in Kubernetes.
✅ Database Integration - Uses PostgreSQL for persistent storage.

🔧 Prerequisites
AWS EC2 Instance (Ubuntu 20.04+)
Docker & Kubernetes (K3s or Minikube)
Jenkins
ArgoCD
Helm & kubectl
📦 Installation & Deployment
1️⃣ Clone Repository
git clone https://github.com/your-username/devops-metrics.git
cd devops-metrics
2️⃣ Deploy PostgreSQL, Flask API, Prometheus, & Grafana
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/flask-app-deployment.yaml
kubectl apply -f k8s/prometheus-deployment.yaml
kubectl apply -f k8s/grafana-deployment.yaml
3️⃣ Deploy ArgoCD & CI/CD Pipeline
kubectl apply -f k8s/argocd-app.yaml
Access ArgoCD UI: http://your-ec2-public-ip:3000
Login Credentials:
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
4️⃣ Set Up Jenkins Pipeline
Add repository to Jenkins Pipeline.
Run the Jenkinsfile pipeline for automatic deployments.
📊 Monitoring with Grafana
Access Grafana: http://your-ec2-public-ip:3000
Default Login:
Username: admin
Password: admin
Import Dashboard ID: 3119 (Kubernetes Monitoring)
📜 License
This project is MIT Licensed.

🚀 Need Help?
If you encounter issues, feel free to open an issue or reach out. 🚀🔥
Here's a Bash script to automate the setup of your DevOps Metrics Monitoring Tool on an AWS EC2 instance.
📜 setup-devops-metrics.sh
#!/bin/bash
# Stop execution on any error
set -e  
echo "🚀 Starting DevOps Metrics Monitoring Tool Setup..."
# Update and install necessary packages
echo "🔹 Updating system packages..."
sudo apt update -y && sudo apt upgrade -y
echo "🔹 Installing dependencies (Docker, Kubernetes, Jenkins, ArgoCD)..."
sudo apt install -y docker.io git curl wget unzip jq
# Enable Docker service
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
# Install Minikube (For Kubernetes Cluster)
echo "🔹 Installing Minikube..."
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube
sudo mv minikube /usr/local/bin/
# Start Minikube
echo "🔹 Starting Minikube..."
minikube start --driver=docker
# Install kubectl
echo "🔹 Installing kubectl..."
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
# Install Jenkins
echo "🔹 Installing Jenkins..."
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update && sudo apt install -y openjdk-11-jdk jenkins
sudo systemctl enable --now jenkins
# Install Helm
echo "🔹 Installing Helm..."
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt install -y apt-transport-https
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt update && sudo apt install -y helm
# Install ArgoCD
echo "🔹 Installing ArgoCD..."
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
# Deploy DevOps Monitoring Components
echo "🔹 Deploying PostgreSQL, Flask API, Prometheus, and Grafana..."
git clone https://github.com/your-username/devops-metrics.git
cd devops-metrics
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/flask-app-deployment.yaml
kubectl apply -f k8s/prometheus-deployment.yaml
kubectl apply -f k8s/grafana-deployment.yaml
kubectl apply -f k8s/argocd-app.yaml

echo "🎉 Setup complete! Access ArgoCD at http://your-ec2-public-ip:3000"

echo "🔑 Retrieve ArgoCD password using: "

echo "kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath=\"{.data.password}\" | base64 -d"

💡 How to Use?

1️⃣ Copy & Save the script as setup-devops-metrics.sh.

2️⃣ Make it executable:
chmod +x setup-devops-metrics.sh

3️⃣ Run the script:
./setup-devops-metrics.sh

4️⃣ Wait for completion, then access:

ArgoCD: http://your-ec2-public-ip:3000

Grafana: http://your-ec2-public-ip:3000

Jenkins: http://your-ec2-public-ip:8080

This script automates AWS EC2 setup, Kubernetes deployment, Jenkins installation, and ArgoCD integration! 🚀🔥
