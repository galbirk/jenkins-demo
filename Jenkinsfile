pipeline {
    agent any
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
            sh 'python -m pytest -q test.py'
            }
        }
    }
}
