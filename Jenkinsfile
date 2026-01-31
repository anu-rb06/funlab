pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t funlab-image .'
            }
        }

        stage('Run Container') {
            steps {
                echo "Running Docker container..."
                sh 'docker run -d -p 8081:8000 funlab-image'
            }
        }

    }
}
