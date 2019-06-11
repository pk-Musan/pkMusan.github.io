from data import get_work, get_all_works
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/portfolio.html')
def portfolio():
    all_works = get_all_works()
    return render_template('/portfolio.html', all_works = all_works)

@app.route('/work/<work_name>.html')
def work(work_name):
    work = get_work(work_name)
    return render_template('/portfolio/work.html', work=work)

@app.route('/profile.html')
def profile():
    return render_template('/profile.html')

if __name__ == "__main__":
    app.run(debug=True)