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
        sh 'pipenv install --dev'
        sh 'pipenv run pytest --cov=condition_chain'
      }
    }
    stage ('Deploy'){
        steps{
            sh 'pipenv install --dev'
            sh 'pipenv run python setup.py sdist bdist_wheel --universal'
            sh 'ls -l dist'
        }
    }
  }
}