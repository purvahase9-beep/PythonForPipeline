pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/purvahase9-beep/PythonForPipeline.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python --version'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App Test') {
            steps {
                bat 'python -c "import flask; print(flask.__version__)"'
            }
        }

        stage('Build Success') {
            steps {
                echo 'Flask application build successful!'
            }
        }
    }
}