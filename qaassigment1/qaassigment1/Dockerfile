FROM openjdk:11
WORKDIR /usr/src/app
COPY ./build/libs/qaassigment1-0.0.1.jar app.jar
ENV PORT 8080
ENTRYPOINT ["java","-jar","app.jar"]
