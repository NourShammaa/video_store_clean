// Jenkins pipeline for Django + Minikube (Windows setup)

def IMAGE = 'video_store_clean:latest'  // Keep this synced with deployment.yaml

pipeline {
  agent any

  triggers { 
    // Poll GitHub for changes every 2 minutes
    pollSCM('H/2 * * * *') 
  }

  stages {

    stage('Checkout') {
      steps {
        echo "📦 Checking out source code..."
        git branch: 'main', url: 'https://github.com/NourShammaa/video_store_clean.git'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat '''
        echo === Configuring Docker to use Minikube environment ===
        call minikube docker-env --shell=cmd > docker_env.bat
        call docker_env.bat

        echo === Building Docker image inside Minikube ===
        docker build -t video_store_clean:latest .
        docker images
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        echo === Setting Minikube and Kube config paths ===
        set MINIKUBE_HOME=C:\\Users\\jenkinslocal.DESKTOP-9U8H60R\\.minikube
        set KUBECONFIG=C:\\Users\\jenkinslocal.DESKTOP-9U8H60R\\.kube\\config

        echo === Applying Kubernetes manifests ===
        kubectl apply -f deployment.yaml --validate=false
        kubectl apply -f service.yaml --validate=false

        echo === Waiting for rollout to complete ===
        kubectl rollout status deployment/django-deployment --timeout=90s

        echo === Showing current pods and services ===
        kubectl get pods -o wide
        kubectl get svc
        '''
      }
    }

  }
}
