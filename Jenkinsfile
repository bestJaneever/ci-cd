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
                git branch: 'feature/f1', url: 'https://github.com/bestJaneever/ci-cd.git'
            }
        }

        stage('Python version') {
            steps {
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
                pytest testfile.py
                '''
            }
        }
        stage('Copy + push to another branch') {
            steps {
                sh 'git branch -D release'
                sh 'git checkout feature/f1'
                sh 'git switch -c release'
                sh 'git add .'
                sh 'git config --global user.name "bestJaneever"'
                sh 'git config --global user.email "eugeniagrebenko@gmail.com"'
                sh 'git config --global url.https://${TOKEN}@github.com/bestJaneever/ci-cd.git'
                sh 'git commit -m "Release commit"'
                sh 'git push -u origin release'
            }
        }
    }
}
