from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
import requests
URL = "https://api.github.com/users/sivanWu0222/repos"
data = requests.get(URL).json()
print(data)
import os


class repository():
    def __init__(self, name, stars, address, descr):
        self.name = name
        self.stars = stars
        self.url_address = address
        self.descr = descr


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/')
def show_user_info():
    return render_template('user.html', repos=repos)


@app.route('/envir/')
def show_envir():
    envir = os.environ
    return render_template('envir.html', envir=envir)


@app.route('/test/')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    repos = []
    for repo in data:
        re = repository(repo['name'], repo['stargazers_count'], repo['html_url'], repo['description'])
        repos.append(re)
    app.run(debug=True)
