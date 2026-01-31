pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/anu-rb06/funlab.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t funlab-image .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Running container...'
                sh '''
                docker stop funlab || true
                docker rm funlab || true
                docker run -d --name funlab -p 8089:8000 funlab-image
                '''
            }
        }
    }
}
