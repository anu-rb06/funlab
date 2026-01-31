pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/anu-rb06/funlab.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-python-app")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker rm -f my-python-container || true'
                    sh 'docker run -d -p 5000:5000 --name my-python-container my-python-app'
                }
            }
        }
    }
}
