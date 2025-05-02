pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                bat '. venv/bin/activate && python autoscale/manage.py makemigrations'
                bat '. venv/bin/activate && python autoscale/manage.py migrate'
            }
        }
    }
}
