from app import app
from app.controllers import author_controller, book_controller


if __name__ == '__main__':
    app.run(debug=True)