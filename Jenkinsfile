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
                bat '"C:\\Users\\samyu\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t log-failure-prediction .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat '"C:\\Users\\samyu\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" stop log-failure-api || exit 0'
                bat '"C:\\Users\\samyu\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm log-failure-api || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '"C:\\Users\\samyu\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name log-failure-api -p 8000:8000 log-failure-prediction'
            }
        }

        stage('Wait for API') {
            steps {
                bat 'timeout /t 10 /nobreak'
            }
        }

        stage('Test API') {
            steps {
                bat 'curl --fail http://localhost:8000'
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