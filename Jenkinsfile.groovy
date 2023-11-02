pipeline {
    agent any
    stages {
        stage('Checkout from GitHub') {
            steps {
                git 'https://github.com/lovalan/finalproject.git'
            }
        }
        stage('Maven Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Deploy with Ansible and Docker') {
            steps {
                ansiblePlaybook(
                    playbook: 'mon_playbook-ansible.yml',
                    inventory: 'ansible-playbook mon_playbook-ansible.yml -i mon_inventaire-ansible.yml'
                )
                script {
                    docker.build('mon_dockerfile')
                    docker.withRegistry('https://docker-hub', 'credentials-id') {
                        docker.image('mon_dockerfile').push()
                    }
                }
            }
        }
        stage('Deploy to AWS') {
            steps {
                sh 'ansible-playbook deploy.yml'
            }
        }
    }
}