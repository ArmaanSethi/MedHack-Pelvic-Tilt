from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

travel = open("travel.txt", 'r').read().split("\n")


@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == "GET":
        return render_template('index.html')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)

def modal(a):
    scripts.label_image
    graph = retrain_graph.pb
    image = a
