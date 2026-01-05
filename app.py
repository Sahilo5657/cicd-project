from flask import Flask

app = Flask(StudentApp)

@app.route("/")
def hello():
    app.logger.info("Hello World logged from Azure!")
    return "Hello World from Azure CI/CD Pipeline!"

if StudentApp == "__main__":
    app.run()
