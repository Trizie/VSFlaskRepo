from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
from .models import Lebensmittel


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    try:
        #lbm = Lebensmittel(Barcode=1238374, LebensmittelName="Olivenöl", Anzahl=2)
        #db.session.add(lbm)
        #db.session.commit()

        #lbm = Lebensmittel.query.all()[0]
        #print(lbm)
        list=["brot"]
        anzahl=[1]
        anzahl = db.session.execute(db.select(Lebensmittel.Anzahl)).scalars().all()
        list = db.session.execute(db.select(Lebensmittel.LebensmittelName)).scalars().all()

        #print('Creating Table Started =====')
        #cur = mysql.cursor()
        #cur.execute(
        #    '''
        #    SELECT Lebensmittel FROM lebensmittel
        #    '''
        #)
        #list = ["Brot"]
        #item = cur.fetchall()
        #list = [row[0] for row in item]

        #cur.execute(
        #    '''
        #    SELECT Anzahl FROM lebensmittel
        #    '''
        #)
        #anzahl = [1]
        #item = cur.fetchall()
        #anzahl = [row[0] for row in item]

        #cur.close()
        #print('Items Table Created =====')
    except Exception as e:
        print("Error while creating table",e)

    return render_template("home.html", user=current_user, fooditems=list, anzahl=anzahl)


