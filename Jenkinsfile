	node{
        stage('Checkout Project'){
            properties([pipelineTriggers([[$class: 'GitHubPushTrigger']])])
            checkout scm
            git_branch = env.BRANCH_NAME
            git_tag = sh returnStdout: true, script: 'git tag -l --points-at HEAD'
        }

		stage("Bake Docker") {
			echo 'Bake Docker'
		}
	stage('Test'){
	      parallel (
		"JUnit": { 
		    sh "echo JUnit"
		},
		"DBUnit": { 
		    sh "echo DBUnit"
		},
		"Jasmine": { 
		    sh "echo Jasmine"
		},
	      )
	    }
    
    stage('Deploy Dev'){
        sh "echo Dev"
    }
	stage('Browser Tests'){
      parallel (
        "Firefox": { 
            sh "echo Firefox"
        },
        "Edge": { 
            sh "echo Edge"
        },
        "Safari": { 
            sh "echo Safari"
        },
        "Chrome": { 
            sh "echo Chrome"
        },
      )
    }
    stage('Deploy Staging'){
        sh "echo Staging"
    }
		stage('Browser Tests'){
      parallel (
        "Firefox": { 
            sh "echo Firefox"
        },
        "Edge": { 
            sh "echo Edge"
        },
        "Safari": { 
            sh "echo Safari"
        },
        "Chrome": { 
            sh "echo Chrome"
        },
      )
    }
	
	stage('Deploy Perf'){
        sh "echo Staging"
    }
		stage('Browser Tests'){
      parallel (
        "VAPT": { 
            sh "echo VAPT"
        },
        "Load Tests": { 
            sh "echo Load Tests"
        },
        "Stress Tests": { 
            sh "echo Stress Tests"
        },
        "Spike Tests": { 
            sh "echo Spike Tests"
        },
      )
    }
    stage('Blue Production'){
        sh "echo Blue Production"
    }
		stage('Post Deployment Browser Tests'){
      parallel (
        "Firefox": { 
            sh "echo Firefox"
        },
        "Edge": { 
            sh "echo Edge"
        },
        "Safari": { 
            sh "echo Safari"
        },
        "Chrome": { 
            sh "echo Chrome"
        },
      )
    }
   stage('Green Production'){
        sh "echo Green Production"
    }
	stage("Merge Pull Request")
		{
			sh "echo Merge Pull Request"
		}
	stage("Merge to Master")
	{
		sh "echo Merge to Master"
	}

}
