pipeline {
    agent {
        docker { image 'builder:1.0.0' }
    }
    stages {
        stage('Setup') {
            steps {
                sh 'echo "Python version: $(python --version)"'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest -v'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t awande:$(git describe --tags --abbrev=0) .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Here we could push our image to docker hub, call a deploy script or do a kubectl update'
            }
        }
    }
}