pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'python autoscale/manage.py makemigrations'
                sh 'python autoscale/manage.py migrate'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python mautoscale/manage.py test'
            }
        }
    }
}
