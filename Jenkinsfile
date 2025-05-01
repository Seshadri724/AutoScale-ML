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
                sh 'python manage.py test'                pipeline {
                    agent {
                        docker {
                            image 'python:3.9' // Use a Python Docker image
                        }
                    }
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
            }
        }
    }
}