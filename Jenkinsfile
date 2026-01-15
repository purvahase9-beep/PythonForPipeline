pipeline {
    agent any

    tools {
        python 'Python314'   // MUST match name in Global Tool Configuration
    }

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'where python'
                bat 'python --version'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Flask App Test') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Build Success') {
            steps {
                echo 'Pipeline executed successfully'
            }
        }
    }
}
