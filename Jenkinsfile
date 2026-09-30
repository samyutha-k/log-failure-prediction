
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
                bat 'ping 127.0.0.1 -n 11 > nul'
            }
        }

        stage('Test Health API') {
            steps {
                bat 'curl --fail http://localhost:8000'
            }
        }

        stage('Test Prediction API') {
            steps {
                bat '''
                curl --fail -X POST http://localhost:8000/predict ^
                -H "Content-Type: application/json" ^
                -d "{\"E1\":0,\"E2\":1,\"E3\":1,\"E4\":15,\"E5\":3,\"E6\":0,\"E7\":0,\"E8\":0,\"E9\":3,\"E10\":0,\"E11\":3,\"E12\":0,\"E13\":0,\"E14\":0,\"E15\":0,\"E16\":0,\"E17\":0,\"E18\":0,\"E19\":0,\"E20\":0,\"E21\":3,\"E22\":1,\"E23\":3,\"E24\":0,\"E25\":0,\"E26\":3,\"E27\":0,\"E28\":0,\"E29\":0}"
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment and API prediction test successful!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}