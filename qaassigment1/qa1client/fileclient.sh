docker pull subuday/qa1client
docker run -d --rm -e PORT=8080 --net lab1 --name client --mount type=volume,source=clientvol,destination=//usr//src//app//clientdata subuday/qa1client