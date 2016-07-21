
# Misc utils made with python in docker container.

## Commands

### gitcheck
Reports git status for repositories in spesified folders and subfolders.
```
root@2343d5a84897:/usr/src/app# python gitutils/main.py /home/workspace/_drerik/
#
#   [✓] = Committed [✗] = Dirty  [?] = Not a git repository
#
# Checking /home/workspace/_drerik/
[✗]  dc-utils-gitcheck
[✓]  django-rest-workshop
[✓]  docker-compose-python
[✓]  docker-django-starter
[?]  docker-influxdb
[?]  esp8266_oled
[?]  nodemcu_dht11
[✓]  tipsntricks
root@2343d5a84897:/usr/src/app#
```
To run from docker:
```
docker run -it --rm -v $HOME:/home drerik/python-utils gitcheck /home/workspace/my-git-repo-folder
```

## Build
To build the container local, run the following command:
```
docker build -t drerik/python-utils .
```
