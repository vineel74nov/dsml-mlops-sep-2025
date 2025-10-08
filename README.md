https://chat.whatsapp.com/CgNgYE1BbY7LoWTrhzlvra

# Session - 2: Streamlit

## Command History

```bash
7012  mkvirtualenv streamlit
7013  pip3 list
7014  pip3 install numpy=1.10
7015  pip3 install numpy==1.10
7016  pip3 install numpy==1.10.1
7017  pip3 install imp
7018  pip3 install numpy --upgrade
7019  pip3 list
7020  pip3 install pandas
7021  pip3 list
7022  pip3 freeze > requirements.txt
7023  ls
7024  cat requirements.txt
7025  mkvirtualenv oct3
7026  pip3 list
7027  pip3 install -r requirements.txt
7028  pip3 list
7029  history
```
# Session - 4: Docker

**Build images**

* `docker build -t oct8 .`
* `docker build -t oct9 .`
* `docker build -t oct8_v2 .`

**Auth & inspection**

* `docker login`
* `docker image ls`
* `docker image ls | head`  *(list images, then trim output)*
* `docker container ls`     *(show running containers)*

**Run containers (mapping host → container port)**

* `docker run -p 8000:8000 oct8`            *(host 8000 → container 8000)*
* `docker run -p 9000:8000 oct8`            *(host 9000 → container 8000)*
* `docker run -d -p 9000:8000 oct8`         *(detached)*
* `docker run -it -p 9000:8000 oct8 bash`   *(interactive shell in the container)*

**Tag & push to Docker Hub**

* `docker tag oct8_v2:latest shivam13juna/docker_oct8:latest`
* `docker push shivam13juna/docker_oct8:latest`

---

### Minimal “do the same thing” script

```bash
# 1) Build the image
docker build -t oct8 .

# 2) Run it (host:9000 -> container:8000), detached
docker run -d --name oct8_app -p 9000:8000 oct8

# 3) (Optional) open a shell inside a fresh container
# docker run -it --rm -p 9000:8000 oct8 bash

# 4) Prepare the image for Docker Hub and push it
docker tag oct8:latest shivam13juna/docker_oct8:latest
docker login
docker push shivam13juna/docker_oct8:latest
```


