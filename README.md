# CS340 html interface design

Setup on local computer
---
git project
```
git clone https://github.com/yichangliao/interface.git
```
run python virtual
```
# Linux and Mac
python3 -m venv venv

# Windows Command Prompt
python -m venv venv
```
activate virtual
```
# Linux and Mac
source venv/bin/activate

# Windows Command Prompt
venv/Scripts/activate.bat
```
install project package
```
pip3 install --upgrade pip
pip install -r requirements.txt
```
Run local project
---
```
python3 app.py
```
Run on flip
---
```
gunicorn -b 0.0.0.0:{any_valid_port} -D app:app
```
kill gunicorn
```
pkill -u {your_user_name} gunicorn
```
Collaboration by VScode and Github(after setup on local computer)
---
first update all files from Github
```
git pull origin master
```
if just want to add other files to project
```
git add .
git commit -m '{comment or description}'
git push origin master
```
if try to modify files
```
git checkout {name of the branch}
```
start editing files...

once done, push branch to github for comparison and merge
```
git push -u origin {name of the branch}
```
Usefull link
---
