pipeline {
    agent any
    
    stages{
        stage("Cloning Code"){
            steps {
                echo "Cloning the code"
                git url:"https://github.com/qasimnauman/django-notes-app.git", branch: "main"
            }
        }
        
        stage("Code Build"){
            steps {
                echo "building code"
                sh "docker build . -t mynotesapp"
            }
        }
        
        stage("push to docker hub"){
            steps {
                echo "deploy to docker hub"
                withCredentials(
                    [
                        usernamePassword(
                            credentialsId:"dockerhub-login",passwordVariable:"dockerhubPass",usernameVariable:"dockerhubuser")]){
                                sh "docker tag mynotesapp ${env.dockerhubuser}/mynotesapp:latest"
                                sh "docker login -u ${env.dockerhubuser} -p ${env.dockerhubPass}"
                                sh "docker push ${env.dockerhubuser}/mynotesapp:latest"
                    }
            }
        }
        
        stage("deploy"){
            steps {
                echo "deploying the container"
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}