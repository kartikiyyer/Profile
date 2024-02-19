This is a project to host my profile using render platform (https://render.com/). 

https://profile-6dzu.onrender.com

## Frontend logic
Frontend is implemented html, css, jquery, bootstrap.
Frontend is making calls to backend using REST APIs.

Theme is taken from the following site:
Theme Name: Folio
Theme URL: https://bootstrapmade.com/folio-bootstrap-portfolio-template/
Author: BootstrapMade.com
Author URL: https://bootstrapmade.com


## Backend logic
Backed is implemented in python, flask, heroku, swagger, REST APIs.

Please do leave a feedback/comment.

## Running the project locally
### Installation instructions
Following python packages are needed to build this project:
Package            Version
------------------ -------
python             3.10
click              8.1.3
Flask              2.2.2
importlib-metadata 7.0.1
itsdangerous       2.1.2
Jinja2             3.1.2
MarkupSafe         2.1.1
pip                21.2.4
setuptools         58.0.4
Werkzeug           2.2.2
zipp               3.17.0

Please refer requirements.txt for latest package versions.

1. Install python 3.10
2. Check if pip installed with python or Install pip
3. Go to project folder
4. python3 -m venv venv
5. source venv/bin/activate
pip install flask==1.0.2 (Will install its dependencies.)

### Build/Run command
python3 src/routes/route_profile.py

## Hosting on render platform
1. Make changes to the code locally.
2. Check the build.sh script for correctness
3. Commit your code to github
4. In the Render website Dashboard, go to the Blueprints page and click New Blueprint Instance.
5. Select the repository that contains your blueprint and click Connect.
6. Give your blueprint project a name and click Apply.
That’s it! Your project will be live at its .onrender.com URL as soon as the build finishes.
Refer: https://docs.render.com/deploy-django#create-a-build-script
