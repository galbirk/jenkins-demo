pipeline {
    agent {docker {
            image 'python:3.8'
        }
    }

    stages {
        stage('Install requirements') {
            steps{
            echo '######################## Install requirements #####################'
            sh 'python -m pip install -r requirements.txt'
            }
            
        }
        stage('Run Test') {
            steps{
            echo '######################## Run Test #####################'
            sh 'pytest -q .\test.py'
            }
        }
    }
}
