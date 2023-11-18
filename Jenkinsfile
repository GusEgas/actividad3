pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/GusEgas/actividad3.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Asumiendo que utilizas un entorno virtual para Python
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                    sh 'pytest test/unit/'
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    // Ejecuta aquí tus pruebas de API
                    sh 'pytest test/rest/'
                }
            }
        }

        // Puedes añadir más etapas según sea necesario
    }
}
