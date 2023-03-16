from flask import Flask, Response, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>hello</h1>"


@app.route("/customers")
def get_customers():
    python_list = [{"id": 1, "name": "jack"}, {"id": 2, "name": "hannah"}]
    my_response = jsonify(python_list)
    return my_response
    

if __name__ == "__main__":
    app.run()


