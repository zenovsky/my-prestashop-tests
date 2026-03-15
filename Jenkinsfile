pipeline {
    agent any

    parameters {
        string(name: 'HUB_EXECUTOR', defaultValue: 'nginx', description: 'Selenoid address (network service name)')
        string(name: 'APP_URL', defaultValue: 'http://prestashop', description: 'Application URL')
        choice(name: 'BROWSER_NAME', choices: ['ch', 'ff'], description: 'Browser')
        string(name: 'BROWSER_VERSION', defaultValue: '128.0', description: 'Browser version')
        string(name: 'THREADS', defaultValue: '1', description: 'Number of threads (requires pytest-xdist plugin)')
        choice(name: 'TEST_TYPE', choices: ['all', 'api', 'ui'], description: 'Tests types: all - all tests, api - only API, ui - only UI')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

    stage('Linting') {
        steps {
            script {
            echo "Checking with Ruff linter..."
                try {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/python3 -m pip install ruff
                    ./venv/bin/python3 -m ruff check .
                '''
                } finally {
                echo "Cleaning the virtual environment..."
                sh 'rm -rf venv'
                }
            }
        }
    }

        stage('Prepare Environment') {
            steps {
                echo 'Running services via Makefile...'
                sh 'make clean || true'
                sh 'make setup'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests from a container using Docker Compose...'
                withCredentials([usernamePassword(
                    credentialsId: 'PRESTASHOP_ADMIN_CREDS', 
                    usernameVariable: 'EXTRACTED_EMAIL', 
                    passwordVariable: 'EXTRACTED_PASS'
                )]) {
                    script {
                        sh 'mkdir -p allure-results'
                        def testContainer = "tests_runner_${BUILD_NUMBER}"

                        def testMarker = ""
                        if (params.TEST_TYPE == "api") {
                            testMarker = "-m api"
                        } else if (params.TEST_TYPE == "ui") {
                            testMarker = "-m ui"
                        }
                        
                        try {
                            sh """
                            docker compose run --name ${testContainer} \
                                -e HUB_EXECUTOR=${params.HUB_EXECUTOR} \
                                -e APP_URL=${params.APP_URL} \
                                -e BROWSER_NAME=${params.BROWSER_NAME} \
                                -e BROWSER_VERSION=${params.BROWSER_VERSION} \
                                -e ADMIN_EMAIL=${EXTRACTED_EMAIL} \
                                -e ADMIN_PASSWORD=${EXTRACTED_PASS} \
                                tests /bin/sh -c "
                                    echo 'Cleaning install folder...' && rm -rf /var/www/html_site/install;
                                    pytest -n ${params.THREADS} \
                                    --browser ${params.BROWSER_NAME} \
                                    --url ${params.APP_URL} \
                                    --browser_version ${params.BROWSER_VERSION} \
                                    --executor ${params.HUB_EXECUTOR} \
                                    --alluredir=/app/allure-results
                                "
                            """
                        } finally {
                            echo "Copying allure results from container..."
                            sh "docker cp ${testContainer}:/app/allure-results/. ./allure-results/ || true"
                            echo "Delete the test container, stop the services..."
                            sh "docker rm -f ${testContainer} || true"
                            sh "make clean || true"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, 
                   jdk: '', 
                   results: [[path: 'allure-results']]
        }
    }
}