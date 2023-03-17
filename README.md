# Flask_Project
Machine_Learning_Project
Software and account requirement.

1. Github Account 

2. Heroku Account

3. VS code IDE

4. GIT cli
---

to pull the complete repository
```
git pull
```

Creating Conda Environment
```
conda create -p venv python=3.7 -y
```

```
conda activate venv/
```

```
pip install -r requirements.txt
```

To add new/ modified files
```
git add .
```

To commit all changes as a verion 
```
git commit -m "message"
```

To change version/change to git
```
git push origin main
```

To check if file is added
```
git status
```
h
```
git log
```

To check remote main url
```
git remote -v
```

To check history of run commands
```
history
```

Docker image
```
docker build -t <image_name>:<tagname> .
```
Note> image name must be lower case

To list docker images
```
docker images
```

To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image id>
```

To check running containers in docker
```
docker ps
```

To stop docker container
```
docker stop <container id>
```
