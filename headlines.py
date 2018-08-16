from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<var>")
def get_news(var="a name"):
	return var
if __name__ == '__main__':
	app.run(port=5000, debug=True)

