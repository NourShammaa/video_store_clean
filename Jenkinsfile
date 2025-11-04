pipeline {
  agent any

  environment {
    KUBECONFIG    = '%USERPROFILE%\\.kube\\config'
    MINIKUBE_HOME = '%USERPROFILE%\\.minikube'
  }

  triggers { pollSCM('H/2 * * * *') }

  stages {
    stage('Start/Ensure Minikube') {
      steps {
        bat '''
        minikube status || minikube start --driver=docker
        minikube kubectl -- get nodes
        '''
      }
    }

    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/NourShammaa/video_store_clean.git'
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat '''
        rem IMPORTANT: ensure MINIKUBE_HOME points to YOUR profile first
        set MINIKUBE_HOME=%USERPROFILE%\\.minikube

        rem Evaluate docker-env in-place (no temp file; preserves quoting)
        for /f "tokens=* usebackq" %%i in (`minikube docker-env --shell=cmd`) do %%i

        docker version
        docker build -t mydjangoapp:latest .
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        rem Use minikube-wrapped kubectl to avoid wrong contexts
        minikube kubectl -- apply -f deployment.yaml
        minikube kubectl -- apply -f service.yaml
        minikube kubectl -- rollout status deployment/django-deployment --timeout=240s
        '''
      }
    }

    stage('Run DB migrations') {
      steps {
        bat 'minikube kubectl -- exec deploy/django-deployment -- python manage.py migrate --noinput'
      }
    }
  }
}
