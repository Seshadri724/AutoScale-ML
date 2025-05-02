pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                bat """
                python -m venv venv
                venv\\Scripts\\activate
                pip install -r requirements.txt
                """
            }
        }

        stage('Build') {
            steps {
                bat """
                cd autoscaleml
                call venv\\Scripts\\activate
                python manage.py makemigrations
                python manage.py migrate
                """
            }
        }
    }
}
