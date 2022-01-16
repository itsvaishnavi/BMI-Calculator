import flask
from flask import Flask, render_template, request

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def api_all():
	st=''
	if request.method == "POST" and 'weight' in request.form:
		weight = float(request.form.get('weight'))
		height = float(request.form.get('height'))
		bmi = weight/((height/100)**2)
		st="Calculated BMI is "+str(round(bmi,2))
	return render_template("temp.html", data=st)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)