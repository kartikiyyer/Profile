This is a project to host my profile using heroku app.
https://kartikiyyer.herokuapp.com/

Frontend logic:
Frontend is implemented html, css, jquery, bootstrap.
Frontend is making calls to backend using REST APIs.

Theme is taken from the following site:
Theme Name: Folio
Theme URL: https://bootstrapmade.com/folio-bootstrap-portfolio-template/
Author: BootstrapMade.com
Author URL: https://bootstrapmade.com


Backend logic:
Backed is implemented in python, flask, heroku, swagger, REST APIs.


Please do leave a feedback/comment.

How to commit
Create a new repository on the command line
echo "# Profile" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/kartikiyyer/Profile.git
git push -u origin master

…or push an existing repository from the command line
git remote add origin https://github.com/kartikiyyer/Profile.git
git push -u origin master

Installation instructions:

Following requirements are needed to build this project:
python 		 2.7
click        6.7    
Flask        1.0.2  
itsdangerous 0.24   
Jinja2       2.10   
MarkupSafe   1.0    
pip          10.0.1 
setuptools   39.2.0 
Werkzeug     0.14.1 
wheel        0.31.1

Install:
python
pip
virtualvenv
pip install flask==1.0.2 (Will install its dependencies.)

Running the project:
export FLASK_APP=src/routes/route_profile.py
flask run --host=0.0.0.0 (To accept incoming connections.)
