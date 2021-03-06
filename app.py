import os
from flask import Flask, render_template

app = Flask(__name__)
 
import db

@app.route('/')
@app.route('/index.html')
def default():
    return render_template('index.html', mapData=db.maps)

@app.route('/<mapName>')
def mapPic(mapName):
    """Return HTML for modal images"""
    for data in db.maps:
        if mapName == data[0]:
            return render_template('img.html', mapData=mapName[3:])
    return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080, debug=True)