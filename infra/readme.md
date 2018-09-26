# Infrastructure

For demonstration purpose we run our own Jenkins CI server from within docker.
For a real setup it should obviously run on dedicated hardware or somewhere in the cloud...

# Starting Jenkins
To start Jenkins run the following command from this directory

    docker-compose up jenkins
   
This will create a the following things:
  - a dedicated network device
    This will allow other services from the docker-compose file to talk to each other
  - `jenkins-home` volume
    A "docker image" that stores the jenkins user data (i.e. build logs, ...). It allows to restart the Jenkins server
    without losing data
  - It launches Jenkins
     - The web UI is reachable at [http://localhost:8080] (or in case of windows docker toolbox, use the docker-machine IP).
     - During the first start, the startup log will provide you with the admin password. 
     - Make sure to add the Pipeline and Git plugins
     
Because we want to run our CI builds and tests within a Docker container as well (why? - reproducibility!) we need to 
install docker CLI within the Jenkins docker container and mount the docker socket. 
See e.g. https://getintodevops.com/blog/the-simple-way-to-run-docker-in-docker-for-ci: 

On your machine:

    docker ps # will give you the container id of your jenkins (you need to start it first, see above)
    docker --version # memorize the host docker version for below
    docker exec -it -u root <jenkins-container-id> /bin/bash  

Within the docker container:

    apt-get update && \
    apt-get -y install apt-transport-https \
         ca-certificates \
         curl \
         gnupg2 \
         software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
       $(lsb_release -cs) \
       stable" && \
    apt-get update

and 

    apt-cache madison doker-ce # will show available versions
    apt-get -y install docker-ce=<best matchin version>
 
We need to install the same CLI as on the host, as we will use the docker socket from the host. The below steps are also 
implemented in the Jenkis.docker file in this directory which is used by the docker-compose script. To use the docker-compose
script, build the "Jenkins with Docker" image with (on your host)

    docker build -t jenkins-docker:1.0.0 -f ./Jenkins.docker .
    
# Building the Builder
Our pipeline script needs git to be available within the docker image. We define our own custom builder container in the 
Builder.docker file.

    docker build -t builder:1.0.0 -f ./Builder.docker . 