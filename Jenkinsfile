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
        stage('') {
          steps {
            sh 'echo "test2"'
          }
        }
      }
    }
    stage('ci') {
      steps {
        sh 'echo "ci"'
      }
    }
    stage('done') {
      steps {
        sh 'echo "done"'
      }
    }
  }
}