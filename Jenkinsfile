pipeline{
    agent any
    stages {
        stage('GIT Checkout'){
            steps {
                git url: 'https://github.com/bestJaneever/ci-cd.git'
            }
        }
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test'){
            steps {
                sh 'pytest testfile.py --html=report.html --self-contained-html'
            }
        }
    }
}
