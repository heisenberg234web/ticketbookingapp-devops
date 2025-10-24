pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "heisenberg123/ticketbookingapp:latest"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'saidevops',
                    url: 'https://github.com/heisenberg234web/ticketbookingapp-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}", "./app")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'saiassign') {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
        bat '''
        set KUBECONFIG=C:\Users\sairu\.kube\config
        kubectl apply -f k8s\\deployment.yaml
        kubectl apply -f k8s\\service.yaml
        '''
            }
        }
    }
}
