pipeline{
    agent {
        docker{
            image 'python:3-alpine'
        }
    }
    stages{
         stage("first"){
        steps{
            sh 'python --version'
            sh 'python Pre_processing.py'
        }
    }
    stage('second'){
        steps{
            sh 'python build_model.py'
        }
    }
    stage('third'){
        steps{
            sh 'python trainModel.py'
        }
    }
    stage('fourth'){
        steps{
            sh 'python testModel.py'
        }
    }
    }
   
    
    
    
}
