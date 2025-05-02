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
                bat 'call venv\\Scripts\\activate & python autoscale\\manage.py makemigrations & python autoscale\\manage.py migrate'
            }
        }
    }
}
