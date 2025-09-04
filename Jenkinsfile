pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/JeevanKumar100/MaharashtraTourism.git'
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
                    sh 'docker stop tourism-app || true && docker rm tourism-app || true'
                    sh 'docker run -d -p 8000:8000 --name tourism-app tourism-app'
                }
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/ursmaheshj/MaharashtraTourism.git'
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
                    sh 'docker stop tourism-app || true && docker rm tourism-app || true'
                    sh 'docker run -d -p 8000:8000 --name tourism-app tourism-app'
                }
            }
        }
    }
}
