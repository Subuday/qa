docker network create lab1
docker pull subuday/qaassigment1
docker run -d --rm -e PORT=8080 --network lab1 --name server -p 8080:8080 --mount type=volume,source=servervol,destination=//usr//src//app//serverdata subuday/qaassigment1