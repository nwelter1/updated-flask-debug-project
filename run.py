from flask import Flask
from app import app 


# from debug_project_app import app
# # from app import create_app

# app = create_app()

if __name__ == "__main__":
    app.run(debug = True)