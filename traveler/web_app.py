
from flask import Flask

application = Flask(__name__)


@application.route('/')
def index():
    """ Main
    """
    return 'Hello Traveler!'


if __name__ == '__main__':
    application.run()
