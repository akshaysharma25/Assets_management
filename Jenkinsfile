pipeline {
    agent any

    stages {
        stage('Fetch code') {
            steps {
                git credentialsId: 'your-git-credentials', branch: '$BRANCH_NAME', url: 'https://github.com/akshaysharma25/Assets_management.git'
            }
        }

        // Add more stages for your build, test, deployment, etc.
        // ...
    }

    post {
        always {
            // Clean up the workspace directory after the pipeline completes
            cleanWs()
        }
    }
}
