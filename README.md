Python Calculator CI/CD Project
Using GitHub, Jenkins & Docker

📌 Project Overview
This is a beginner DevOps mini project where a Python calculator web application is automatically built and deployed using Jenkins and Docker whenever code is pushed to GitHub.
The calculator runs in a browser and supports:
Addition
Subtraction
Multiplication
Division

🛠 Tools & Technologies Used
Python (Flask) – Web application
GitHub – Source code repository
Jenkins – CI/CD automation
Docker – Containerization
Ubuntu 22.04 – Server OS

🖥 Infrastructure Requirement
Component	Count
Server (EC2 / VM)	1 (Free Instance)
Installed on same server:
Jenkins
Docker
Application container


🔌 Required Open Ports
Port	Purpose
8080	Jenkins UI
5000	Calculator App


📂 Project Structure
calculator-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── Jenkinsfile


🚀 Step 1: Install Docker
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
Verify:
docker --version



🚀 Step 2: Install Jenkins
Install Java
sudo apt update
sudo apt install -y openjdk-17-jdk
Add Jenkins Repository
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
Install Jenkins
sudo apt update
sudo apt install -y jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
Allow Jenkins to Run Docker
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
Jenkins Access
http://SERVER_IP:8080
Get admin password:
sudo cat /var/lib/jenkins/secrets/initialAdminPassword





🧑‍💻 Step 3: Python Calculator Application
app.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Simple Calculator</h2>
    <form method="post" action="/calculate">
        <input name="num1" type="number" required>
        <input name="num2" type="number" required><br><br>
        <select name="operation">
            <option value="add">Add</option>
            <option value="sub">Subtract</option>
            <option value="mul">Multiply</option>
            <option value="div">Divide</option>
        </select><br><br>
        <button type="submit">Calculate</button>
    </form>
    '''
    
@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['num1'])
    b = float(request.form['num2'])
    op = request.form['operation']

    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        result = a / b if b != 0 else "Error"

    return f"<h3>Result: {result}</h3><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



requirements.txt
flask




🐳 Step 4: Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]





🔄 Step 5: Jenkins Pipeline
Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/calculator-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker rm -f calculator || true
                docker run -d -p 5000:5000 --name calculator calculator-app
                '''
            }
        }
    }
}




📤 Step 6: Push Code to GitHub
git init
git add .
git commit -m "Python calculator CI/CD project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/calculator-app.git
git push -u origin main
🧪 Step 7: Configure Jenkins Job
Jenkins → New Item
Name: calculator-pipeline
Type: Pipeline
Pipeline Definition: Pipeline script from SCM
SCM: Git
Repository URL: GitHub repo URL
Save → Build Now
🌐 Step 8: Access the Application
http://SERVER_IP:5000
