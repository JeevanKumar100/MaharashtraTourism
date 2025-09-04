pipeline {
    agent any

    environment {
        // 👇 Change this to switch repo easily
        GIT_REPO = "https://github.com/JeevanKumar100/MaharashtraTourism.git"
        // GIT_REPO = "https://github.com/ursmaheshj/MaharashtraTourism.git"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/master']],
                    userRemoteConfigs: [[url: "${GIT_REPO}"]]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t tourism-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                        docker stop tourism-app || true
                        docker rm tourism-app || true
                        docker run -d -p 8000:8000 --name tourism-app tourism-app
                    '''
                }
            }
        }
    }
}
