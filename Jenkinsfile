pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                bat 'python autoscale/manage.py makemigrations'
                bat 'python autoscale/manage.py migrate'
            }
        }
    }
}
