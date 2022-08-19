import os

from src.test import ServiceGenerator

service = ServiceGenerator()
app = service.app


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}! This is my seventh application".format(name)
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
