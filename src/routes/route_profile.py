import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project/policy-enforcer')
def project_policy_enforcer():
	return render_template('policy-enforcer.html')

@app.route('/project/cloud-native-contrail-networking')
def project_cloud_native_contrail_networking():
	return render_template('cloud-native-contrail-networking.html')

@app.route('/project/juniper-fabric-manager')
def project_juniper_fabric_manager():
	return render_template('juniper-fabric-manager.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
