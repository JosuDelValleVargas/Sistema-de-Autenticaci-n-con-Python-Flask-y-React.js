import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Usuario, Personas,Planetas,Vehiculos,Favoritos_personas,Favoritos_planetas,Favoritos_vehiculos

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Usuario, db.session))
    admin.add_view(ModelView(Personas, db.session))
    admin.add_view(ModelView(Planetas, db.session))
    admin.add_view(ModelView(Vehiculos, db.session))
    admin.add_view(ModelView(Favoritos_personas, db.session))
    admin.add_view(ModelView(Favoritos_planetas, db.session))
    admin.add_view(ModelView(Favoritos_vehiculos, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))