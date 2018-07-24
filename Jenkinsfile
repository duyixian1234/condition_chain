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
        sh 'pipenv run pytest --cov=condition_chain'
    }
  }
}