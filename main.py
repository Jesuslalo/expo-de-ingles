from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modern-innovations')
def modern_innovations():
    return render_template('modern_innovations.html')

@app.route('/impact-challenges')
def impact_challenges():
    return render_template('impact_challenges.html')

@app.route('/ref-con')
def reflection_conclusion():
    return render_template('ref_con.html')

if __name__ == '__main__':
    app.run(debug=True)
