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

 