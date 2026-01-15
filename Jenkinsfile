pipeline {
    agent any

    stages {

        stage('Setup Python Environment') {
            steps {
                powershell '& "C:\\Users\\Ruchita\\AppData\\Local\\Python\\bin\\python.exe" --version'
                powershell '& "C:\\Users\\Ruchita\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Flask App Test') {
            steps {
                powershell '& "C:\\Users\\Ruchita\\AppData\\Local\\Python\\bin\\python.exe" -c "import flask; print(flask.__version__)"'
            }
        }

        stage('Build Success') {
            steps {
                echo 'Flask Jenkins pipeline executed successfully!'
            }
        }
    }
}