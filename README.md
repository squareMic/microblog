# microblog

This is just a repo for redoing "The Flask Mega-Tutorial" from https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Credits go to Miguel Grinberg


# Changelog

### 2025-07-30 Added Dockerfile
- command to build run:
```bash
docker image build -t <tag-name>
```
- command to run container
```bash
docker container run -it -p 5000:5000 -e FLASK_APP=microblog <tag-name-of-container>
```
- run in debug mode and make development files accessible from host
```bash
docker container run -it -p 5000:5000 -e FLASK_APP=microblog -v $PWD:/microblog -e FLASK_DEBUG=1 <tag-name-of-container>
```
