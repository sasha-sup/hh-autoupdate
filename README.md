# hh-autoupdate
### Made with Selenuim and Selenoid

How to run:
You need to setup Docker first.
```sh
# export you hh.ru credentials
export HH_USER=example-username
export HH_PASSWORD=example-password
# Download Configuration Manager 
# https://github.com/aerokube/cm
wget https://github.com/aerokube/cm/releases/download/1.8.1/cm_linux_amd64
# Set exec permissions and run it
chmod +x cm_linux_amd64
./cm_linux_amd64 selenoid start
# Install python3 requirements
pip3 install -r requirements.txt
```
Set cronjob for main.py script.
```sh
0 */6 * * * python3 main.py
```



