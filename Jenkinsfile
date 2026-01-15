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
                bat 'where python'
                bat 'python --version'
            }
        }

        stage('Run App') {
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