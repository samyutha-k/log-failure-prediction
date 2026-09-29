pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t log-failure-prediction .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop log-failure-api || exit 0'
                bat 'docker rm log-failure-api || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d --name log-failure-api -p 8000:8000 log-failure-prediction'
            }
        }

        stage('Test API') {
            steps {
                bat 'curl http://localhost:8000'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}