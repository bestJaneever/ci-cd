pipeline {
    agent any

    environment {
        VENV = 'venv' // Python virtual environment folder
    }

    tools {
        python 'Python-3.11' // Name matching the Python version installed in the Dockerfile
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your Python project's repository
                git 'https://github.com/bestJaneever/ci-cd.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment and install dependencies
                sh '''
                python3 -m venv ${VENV}
                source ${VENV}/bin/activate
                pip install --upgrade pip --break-system-packages
                pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python tests with pytest
                sh '''
                source ${VENV}/bin/activate
                pytest testfile.py --html=report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            cleanWs() // Clean-up workspace
        }

        success {
            archiveArtifacts artifacts: 'reports/test-results.xml', fingerprint: true
            echo 'Build succeeded!'
        }

        failure {
            echo 'Build failed!'
        }
    }
}