from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import label_image
from werkzeug import secure_filename

def script_caller(image):
        graph = "retrained_graph.pb" # on site
        #image = "images/post/20.jpeg" # user input
        textFile = "retrained_labels.txt" #on the site
        return label_image.function(graph, image, textFile)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/", methods=['GET', 'POST'])
def root():
    return render_template('index.html')

@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('static/user_upload.jpeg')
      return do_things('static/user_upload.jpeg')
    #   return 'file uploaded successfully'

@app.route('/results')
def do_things(image = None):
    (labels, confidences) = script_caller(image)
    the_label = "None"
    for i in range(len(labels)):
        if(confidences[i]) > 0.5:
            the_label = labels[i]
            the_confidence = confidences[i]
    return render_template('results.html', label = the_label, confidence = the_confidence)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug = True)
