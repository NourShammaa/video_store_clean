// Jenkins pipeline for Minikube + Django
// One place to change image name/tag:
def IMAGE = 'video_store_clean:latest'   // keep in sync with deployment.yaml

pipeline {
  agent any

  triggers { pollSCM('H/2 * * * *') } // every ~2 minutes

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/NourShammaa/video_store_clean.git'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat '''
        REM Point Docker CLI to Minikube's Docker daemon
        call minikube docker-env --shell=cmd > docker_env.bat
        call docker_env.bat

        REM Build image inside Minikube
        docker build -t video_store_clean:latest .
        docker images
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml
        kubectl rollout status deployment/django-deployment
        kubectl get pods -o wide
        '''
      }
    }
  }
}
