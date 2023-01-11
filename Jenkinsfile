pipeline{

	agent {label 'NodeSSH'}

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub_id')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t jalakon/jenkinsfile:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push jalakon/jenkinsfile:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
