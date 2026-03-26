pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Repository already cloned by Jenkins'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'No tests yet'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'start /B python app.py'
            }
        }
    }
}