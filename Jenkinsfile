pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build start'
        sh 'pipenv install'
        echo 'Prepared'
      }
    }
    stage('Test') {
      steps {
        sh '''pipenv install --dev
pipenv run pytest'''
      }
    }
  }
}