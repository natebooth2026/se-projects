from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/api/add/<x>/<y>")
def add_numbers(x,y):
    return jsonify({"result": float(x)+float(y)})

if __name__ == "__main__":
    app.run(debug=True)