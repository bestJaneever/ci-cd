pipeline {
    agent any

    environment {
        VENV = 'venv' // Python virtual environment folder
    }

    stages {
        stage('Clean Workspace') {
            steps {
                sh 'rm -rf ci-cd || true'  // Remove directory if it exists
            }
        }
        stage('Clone Repository') {
            steps {
                // Clone your Python project's repository
                sh 'git clone -b feature/f1 https://github.com/bestJaneever/ci-cd.git'
            }
        }

        stage('Python version'){
            steps{
                sh 'python3 --version'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment and install dependencies
                sh '''
                python3 -m venv ${VENV}
                . ${VENV}/bin/activate
                pip install --upgrade pip --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python tests with pytest
                sh '''
                . ${VENV}/bin/activate
                realpath "$0"
                pytest /var/jenkins_home/workspace/Task/ci-cd/testfile.py
                '''
            }
        }
    }
}