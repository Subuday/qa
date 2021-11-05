#  QA Assignment 1. Docker

https://docs.google.com/document/d/1laT1QVVWXNbZZrSk_cuPFMxUZtbNLkGZyBwVX7j8HPI

## Pre-requisites

You should have docker installed: https://docs.docker.com/get-docker/

## Quickstart

Run server by executing `fileserver.sh`. By default, container port is 8080. 
You can change the port by changing the environment variable `PORT` in the file. 

Run client by executing `fileclient.sh`. By default, client connects to the server using 8080 port.
You can change the connection port by changing the environment variable `PORT` in the file.