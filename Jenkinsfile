pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yaml'
        IMAGE_NAME = 'amanprakash23/autoscaleml'
        IMAGE_TAG = 'latest'
    }
    
    stages {
        // stage('Install Dependencies') {
        //     steps {
        //         bat 'python -m venv venv & call venv\\Scripts\\activate & pip install -r requirements.txt'
        //     }
        // }

        stage('Build Containers') {
            steps {
                bat "docker-compose -f ${DOCKER_COMPOSE_FILE} up -d --build"
            }
        }

        // stage('Migrate Databases') {
        //     steps {
        //         bat 'cd autoscaleml & call ..\\venv\\Scripts\\activate & python manage.py makemigrations & python manage.py migrate'
        //     }
        // }

        stage('Stop Containers') {
            steps {
                bat "docker-compose -f ${DOCKER_COMPOSE_FILE} down"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat ' docker login -u %DOCKER_USER% -p %DOCKER_PASS% && docker tag autoscale-ml %IMAGE_NAME%:%IMAGE_TAG% && docker push %IMAGE_NAME%:%IMAGE_TAG% && docker logout' 
                }
            }
        }
    }
}

