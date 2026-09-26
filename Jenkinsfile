pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
        DOCKER_IMAGE = "ml-model-app:latest"
        CONTAINER_NAME = "ml-model-service"
    }
    stages {
        stage('Set Up Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Train Model') {
            steps {
                sh './venv/bin/python train.py'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/pytest test_app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d -p 8000:8000 --name $CONTAINER_NAME $DOCKER_IMAGE
                '''
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}