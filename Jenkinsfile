pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t myjenkinsapp .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 8095:80 --name jenkinscontainer myjenkinsapp || exit 0'
            }
        }
    }
}