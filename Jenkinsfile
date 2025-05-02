pipeline {
    agent any
    
    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/your-repo.git'
            }
        }

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
