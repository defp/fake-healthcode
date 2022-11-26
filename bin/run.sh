
docker rm fhc
docker run -d -p 8081:8081 -p 8080:8080 --name=fhc --restart=always fake-healthcode:latest
