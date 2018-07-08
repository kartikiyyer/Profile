from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project/policy-enforcer')
def project_policy_enforcer():
	return render_template('policy-enforcer.html')
