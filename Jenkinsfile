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
                }
            }
        }

        stage('Run API Tests') {
            steps {
                script {
                    sh 'docker network create calc-test-api || true'
                    sh 'docker run -d --rm --volume `pwd`:/opt/calc --network calc-test-api --env PYTHONPATH=/opt/calc --name apiserver --env FLASK_APP=app/api.py -p 5000:5000 -w /opt/calc calculator-app:latest flask run --host=0.0.0.0'
                    sh 'docker run --rm --volume `pwd`:/opt/calc --network calc-test-api --env PYTHONPATH=/opt/calc --env BASE_URL=http://apiserver:5000/ -w /opt/calc calculator-app:latest pytest --junit-xml=results/api_result.xml -m api  || true'
                    sh 'docker stop apiserver'
                    sh 'docker rm --force apiserver'
                    sh 'docker network rm calc-test-api'
                }
            }
        }

        stage('Run E2E Tests') {
            steps {
                script {
                    sh 'docker network create calc-test-e2e-wiremock || true'
                    sh 'docker stop apiwiremock || true'
                    sh 'docker rm --force apiwiremock || true'
                    sh 'docker stop calc-web || true'
                    sh 'docker rm --force calc-web || true'
                    sh 'docker run -d --rm --name apiwiremock --volume `pwd`/test/wiremock/stubs:/home/wiremock --network calc-test-e2e-wiremock -p 8080:8080 -p 8443:8443 calculator-wiremock'
                    sh 'docker run -d --rm --volume `pwd`/web:/usr/share/nginx/html --volume `pwd`/web/constants.wiremock.js:/usr/share/nginx/html/constants.js --volume `pwd`/web/nginx.conf:/etc/nginx/conf.d/default.conf --network calc-test-e2e-wiremock --name calc-web -p 80:80 nginx'
                    sh 'docker run --rm --volume `pwd`/test/e2e/cypress.json:/cypress.json --volume `pwd`/test/e2e/cypress:/cypress --volume `pwd`/results:/results --network calc-test-e2e-wiremock cypress/included:4.9.0 --browser chrome || true'
                    sh 'docker rm --force apiwiremock'
                    sh 'docker rm --force calc-web'
                    sh 'docker run --rm --volume `pwd`:/opt/calc --env PYTHONPATH=/opt/calc -w /opt/calc calculator-app:latest junit2html results/cypress_result.xml results/cypress_result.html'
                    sh 'docker network rm calc-test-e2e-wiremock'
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results/*.xml'
            junit 'results/*_result.xml'
            echo "El trabajo de Jenkins ha finalizado"
        }
        failure {
            echo "Enviar correo: El trabajo '${env.JOB_NAME}#${env.BUILD_NUMBER}' ha fallado."
        }
    }
}
