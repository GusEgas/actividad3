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
                    sh 'docker build -t calculator-app .'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sh 'docker run --rm --volume `pwd`:/opt/calc --env PYTHONPATH=/opt/calc -w /opt/calc calculator-app:latest pytest --cov --cov-report=xml:results/coverage.xml --cov-report=html:results/coverage --junit-xml=results/unit_result.xml -m unit || true'
                    sh 'docker cp calculator-app:/opt/calc/results .'
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    sh 'docker network create calc-test-api || true'
                    sh 'docker run -d --rm --volume `pwd`:/opt/calc --network calc-test-api --env PYTHONPATH=/opt/calc --name apiserver --env FLASK_APP=app/api.py -p 5000:5000 -w /opt/calc calculator-app:latest flask run --host=0.0.0.0'
                    sh 'docker run --rm --volume `pwd`:/opt/calc --network calc-test-api --env PYTHONPATH=/opt/calc --env BASE_URL=http://apiserver:5000/ -w /opt/calc calculator-app:latest pytest --junit-xml=results/api_result.xml -m api || true'
                    sh 'docker run --rm --volume `pwd`:/opt/calc --env PYTHONPATH=/opt/calc -w /opt/calc calculator-app:latest junit2html results/api_result.xml results/api_result.html'
                    sh 'docker stop apiserver || true'
                    sh 'docker rm --force apiserver || true'
                    sh 'docker network rm calc-test-api || true'
                    sh 'docker cp apiserver:/opt/calc/results .'
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results/*.xml, results/coverage/*, results/*.html'
            cleanWs()
        }
    }
}
