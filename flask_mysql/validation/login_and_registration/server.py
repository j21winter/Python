from app import app
# import controllers here! 
from app.controllers import user_controller

if __name__ == ('__main__'):
    app.run(debug = True)