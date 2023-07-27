pipeline {
    agent any

    environment {
        versionTags = "" // Initialize versionTags as an empty string to avoid issues with undefined variables
    }

    stages {
        stage('Checkout') {
            steps {
                // Use the "GIT_CRED" credentials to access the private repo
                checkout([$class: 'GitSCM',
                    branches: [[name: "$BRANCH_NAME"]],
                    userRemoteConfigs: [[
                        url: 'https://github.com/akshaysharma25/Assets_management.git',
                        credentialsId: 'GIT_CRED'
                    ]]
                ])
            }
        }

        stage('Read Version Tags') {
            steps {
                script {
                    // Read the last line of file1.txt and store it in the 'versionTags' variable
                    versionTags = sh(script: "tail -n 1 test", returnStdout: true).trim()
                }
            }
        }

        stage('Build') {
            steps {
                // Use the 'versionTags' variable as needed in the build steps
                echo "Building version: $versionTags"
                // Other build steps
            }
        }

        // Other stages in your pipeline
        // ...
    }

    post {
        always {
            cleanWs() // Clean workspace at the end, regardless of pipeline status
        }
    }
}
