pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/GusEgas/actividad3.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Asumiendo que tienes un Dockerfile en la raíz del repositorio
                    sh 'docker build -t calculator-app .'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Ejecutar pruebas unitarias con Docker
                    sh 'docker run --rm --volume `pwd`:/opt/calc --env PYTHONPATH=/opt/calc -w /opt/calc calculator-app:latest pytest --cov --cov-report=xml:results/coverage.xml --cov-report=html:results/coverage --junit-xml=results/unit_result.xml -m unit || true'
                }
            }
        }

        // Puedes añadir más etapas según sea necesario
    }

    post {
        always {
            // Pasos para realizar después de ejecutar las pruebas, como limpieza o envío de notificaciones
            echo "El trabajo de Jenkins ha finalizado"
        }
    }
}
