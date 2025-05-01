pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python manage.py test'
            }
        }
    }
}