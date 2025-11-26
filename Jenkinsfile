pipeline {
    agent any

    environment {
        // Docker image naming convention: username/rollno-todo
        IMAGE = "vriddhi07/imt2023611-todo"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[
                    url: 'https://github.com/vriddhi-07/To_Do_List_App',
                    credentialsId: 'github-creds'
                  ]]
                ])
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "python -m pip install --upgrade pip"
                bat "pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "pytest -v"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE%:%BUILD_NUMBER% ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    bat """
                        docker login -u %USER% -p %PASS%
                        docker push %IMAGE%:%BUILD_NUMBER%
                    """
                }
            }
        }

    } // end stages
} // end pipeline

