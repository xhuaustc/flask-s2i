pipeline {
  agent any
  stages {
    stage('test') {
      parallel {
        stage('test') {
          steps {
            sh 'echo "test"'
          }
        }
        stage('error') {
          steps {
            sh 'echo "test2"'
          }
        }
      }
    }
    stage('ci') {
      steps {
        sh 'echo "ci"'
        fileExists 'test'
      }
    }
    stage('done') {
      steps {
        sh 'echo "done"'
      }
    }
  }
}