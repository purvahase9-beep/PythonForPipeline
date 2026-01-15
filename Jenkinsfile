pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat "\"C:\\Users\\Purva\\AppData\\Local\\Programs\\Python\\Python314\\python.exe\" --version"
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat "\"C:\\Users\\Purva\\AppData\\Local\\Programs\\Python\\Python314\\python.exe\" -m pip install --upgrade pip"
                bat "\"C:\\Users\\Purva\\AppData\\Local\\Programs\\Python\\Python314\\python.exe\" -m pip install -r requirements.txt"
            }
        }

        stage('Run Flask App Test') {
            steps {
                bat "\"C:\\Users\\Purva\\AppData\\Local\\Programs\\Python\\Python314\\python.exe\" app.py"
            }
        }

        stage('Build Success') {
            steps {
                echo 'Pipeline executed successfully'
            }
        }
    }
}
