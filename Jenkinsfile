pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                sh '. venv/bin/activate && python autoscale/manage.py makemigrations'
                sh '. venv/bin/activate && python autoscale/manage.py migrate'
            }
        }
    }
}
