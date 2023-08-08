from app import app
# import controllers here! 
from app.controllers import users_controller

if __name__ == ('__main__'):
    app.run(debug = True)