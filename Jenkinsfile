pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yaml'
    }
    
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv & call venv\\Scripts\\activate & pip install -r requirements.txt'
            }
        }

        stage('Build Containers') {
            bat "docker-compose -f ${DOCKER_COMPOSE_FILE} up -d --build"
        }

        stage('Migrate Databases') {
            steps {
                bat 'cd autoscaleml & call ..\\venv\\Scripts\\activate & python manage.py makemigrations & python manage.py migrate'
            }
        }

        stage('Stop Containers') {
            steps {
                bat 'docker-compose -f ${DOCKER_COMPOSE_FILE} down'
            }
        }
    }
}
