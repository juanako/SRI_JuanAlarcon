pipeline{

	agent {label 'NodeSSH'}

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub_id')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t helloapp:v1 .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push helloapp:v1'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
