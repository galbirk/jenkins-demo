pipeline {
    agent any

    stages {
        stage('Install requirements') {
            steps{
            echo '######################## Install requirements #####################'
            sh 'sudo apt update && sudo apt install python-pip && python -m pip install -r requirements.txt'
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
