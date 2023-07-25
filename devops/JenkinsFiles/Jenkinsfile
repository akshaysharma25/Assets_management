pipeline {
    agent any

stages {
	    stage('Fetch code') {
            steps {
               git credentialsId: 'your-git-credentials', branch: '$BRANCH_NAME', url: 'https://github.com/akshaysharma25/Assets_management.git''
            }

	    }
	}

}
