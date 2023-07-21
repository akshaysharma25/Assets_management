env.VERSION="""$BUILD_NUMBER"""

node(label: 'Jenkins-Nodes')
{
	try
	{
        stage('Git checkout')
        {
            try
            {
                checkout([$class: 'GitSCM', branches: [[name: '$BRANCH_NAME']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'jenkins', url: 'git@github.com:akshaysharma25/Assets_management.git']]])

                sh """
                #!/bin/bash
                echo $BRANCH_NAME
                git checkout $BRANCH_NAME
                  
                """
            }
            catch (exc)
            {
                echo 'Git checkout failed'
                throw exc
            }
        }
	}
    finally
	{
        cleanWs()
    	dir("${env.WORKSPACE}@tmp")
		{
      		deleteDir()
    	}
    }
}
