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
