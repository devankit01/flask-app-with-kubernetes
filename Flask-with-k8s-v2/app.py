import uuid
from flask import Flask


instance_id = uuid.uuid4().hex
app = Flask(__name__)


@app.route('/')
def index():
    return "Instance id {}".format(instance_id)


if __name__ == "__main__":
    app.run(port=5000, debug=True)