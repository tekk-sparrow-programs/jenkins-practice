/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.9-alpine3.19' } }
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'source venv/bin/activate && python -m unittest discover tests'
                }
            }
        }
        stage('Deploy to Localhost') {
            steps {
                script {
                    sh 'source venv/bin/activate && python3 helloworld.py &'
                }
            }
        }
    }
    post {
        always {
            script {
                sh 'deactivate || true'
            }
        }
        success {
            script {
                echo 'This will run only if successful'
            }
        }
        failure {
            script {
                echo 'This will run only if failed'
            }
        }
        unstable {
            script {
                echo 'This will run only if the run was marked as unstable'
            }
        }
        changed {
            script {
                echo 'This will run only if the state of the Pipeline has changed'
                echo 'For example, if the Pipeline was previously failing but is now successful'
            }
        }
    }
}
