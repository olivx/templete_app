pipeline {
    agent any

    environment {
        DOCKER_REGISTRY_URL = 'localhost:5000'
        IMAGE_BASE_NAME = 'template_app'
        DEPLOYMENT_NAME = 'template-app-api'
        NAMESPACE = 'default'
    }

    stages {
        stage('test') {
            steps {
                sh 'docker-compose build'
                sh 'docker-compose run --entrypoint make api test'
            }

            post{
                always{
                    cobertura   coberturaReportFile: 'coverage.xml',
                                conditionalCoverageTargets: '85, 0, 0',
                                enableNewApi: false,
                                lineCoverageTargets: '90, 0, 0',
                                maxNumberOfBuilds: 10,
                                methodCoverageTargets: '90, 0, 0',
                                sourceEncoding: 'ASCII',
                                zoomCoverageChart: false
                    junit 'junit.xml'
                    sh 'docker-compose down'
                }
            }

        }

        stage('build'){
            when { 
                branch 'master'
            } 
            steps {
                sh 'docker build -t $DOCKER_REGISTRY_URL/$IMAGE_BASE_NAME:$GIT_COMMIT .'
                sh 'docker push $DOCKER_REGISTRY_URL/$IMAGE_BASE_NAME:$GIT_COMMIT'
            }
        }

        stage('deploy'){
            when {
                branch 'master'
            }
            steps {
                sh 'kubectl --record deployment.apps/$DEPLOYMENT_NAME \
                            set image deployment.v1.apps/$DEPLOYMENT_NAME \
                            template-app-api=$DOCKER_REGISTRY_URL/$IMAGE_BASE_NAME:$GIT_COMMIT \
                            migrations=$DOCKER_REGISTRY_URL/$IMAGE_BASE_NAME:$GIT_COMMIT -n $NAMESPACE'
            }
        }

    }

    post {
        always {
            office365ConnectorSend message: "New pipeline run for branch project - ${env.IMAGE_BASE_NAME} - branch ${env.BRANCH_NAME}",
                                   status:"${currentBuild.currentResult}",
                                   webhookUrl:'https://outlook.office.com/webhook/860cd5c1-6d35-433a-987b-76f8938d06ae@68f06401-3da9-4972-96e1-bd5e2bf1d646/JenkinsCI/1ad19474f48e41c09be40265e3f7cbdb/1f89debb-d369-4dbc-9ce0-94d375b9d701'
        }
    }

}