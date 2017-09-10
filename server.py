from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import label_image

def script_caller(image):
        graph = "retrained_graph.pb" # on site
        image = "images/post/20.jpeg" # user input

        textFile = "retrained_labels.txt" #on the site

        return label_image.function(graph, image, textFile)

@app.route("/", methods=['GET', 'POST'])
def root():
    return render_template('index.html')

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
    app.run(host = "0.0.0.0", port = 5000, debug = True)
