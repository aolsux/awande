# Awesome Anomaly Detection (Awande)
A toy project to demonstrate CI & Monitoring

# Building the application
Awande ist build with the included docker file with the following command:

    cd <your-project-root>
    docker build . -t awande:x.y.z
    
# Integration with CI
Start the Jenkins/Docker container from within the `infra` directory (check readme there).

    cd infra && docker-compose up jenkins
    
Then setup a Pipeline job pointing to this Github repository.

Awesome, lets write some tests!

# Testing
The tests from the test directory will be run by the Jenkins server from within the `Test` stage. See the Jeninsfile 
for the configuration.

# Building
Building and testing now happens from within our own container. We simply call the

    docker build -t name:tag .

from within our Jenkins pipeline.

Because everything essentially uses the same Docker deamon (containers just mount it from the host). The built image
will be available on your host as well:

    docker images
    
        REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
        awande              v0.3.0              78bd1e28349c        7 seconds ago        143MB
        builder             1.0.0               c091db3eb6dd        About a minute ago   683MB
        jenkins-docker      1.0.0               94fca9afb394        About an hour ago    859MB
 