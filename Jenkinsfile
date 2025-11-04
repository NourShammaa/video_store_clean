pipeline {
  agent any

  options {
    disableConcurrentBuilds()
  }

  // No SCM trigger here—run manually or add exactly one trigger later.
  // triggers { pollSCM('H/5 * * * *') }

  environment {
    // Make Jenkins use your user paths that already work
    HOME          = 'C:\\Users\\nours'
    USERPROFILE   = 'C:\\Users\\nours'
    MINIKUBE_HOME = 'C:\\Users\\nours\\.minikube'
    // Kubeconfig exported from your working shell (Step A earlier)
    KUBECONFIG    = 'C:\\ProgramData\\Jenkins\\kube\\kubeconfig-fixed'
  }

  stages {

    stage('Start/Ensure Minikube') {
      steps {
        bat """
          @echo on
          echo Using KUBECONFIG=%KUBECONFIG%
          minikube -p minikube status || minikube start --driver=docker
          if errorlevel 1 exit /b 1
          minikube kubectl -- get nodes
        """
      }
    }

    stage('Point Docker to Minikube') {
      steps {
        bat """
          @echo on
          for /f "tokens=*" %%i in ('minikube docker-env --shell=cmd') do %%i
          docker info | find "Name"
        """
      }
    }

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build in Minikube Docker') {
      steps {
        bat """
          @echo on
          rem Build image inside Minikube's Docker
          minikube image build -t mydjangoapp:latest . -- --progress=plain
        """
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat """
          @echo on
          minikube kubectl -- apply -f deployment.yaml
          minikube kubectl -- apply -f service.yaml
          minikube kubectl -- rollout status deploy/mydjangoapp --timeout=180s
          minikube kubectl -- get pods -o wide
        """
      }
    }

    stage('Run DB migrations') {
      steps {
        bat """
          @echo on
          for /f %%p in ('minikube kubectl -- get pods -l app=mydjangoapp -o name') do minikube kubectl -- exec %%p -- python manage.py migrate --noinput
        """
      }
    }
  }

  post {
    always {
      bat "minikube kubectl -- get all"
    }
  }
}
