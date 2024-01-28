/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.9-alpine3.19' } }
    stages {
        stage('Build') {
            steps {
                sh '''
                python3 --version
                ls -la
                source venv/bin/activate
                pip3 install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                python3 -m unittest
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh 'python3 helloworld.py'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}