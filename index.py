from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Youtube Downloader'
    return render_template('index.html', title=title)

@app.route('/submit', methods=['POST'])
def post_submit():
    url = request.form['inputYoutube']
    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download('./')
    filename = yt.title
    return redirect(url_for('index', filename=filename))


if __name__ == '__main__':
  app.run(debug=True, port=9000)
