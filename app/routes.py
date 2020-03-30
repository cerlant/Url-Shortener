from flask import render_template, redirect, flash, url_for
from app import app, db
from app.form import UrlShortenerForm
from app.models import Data



@app.route('/', methods=['GET','POST'])
def home():
    domain = app.config['SERVER_NAME']
    form = UrlShortenerForm()
    if form.validate_on_submit():
        url = Data.query.filter_by( url=form.url.data ).first()
        if url is not None:
            flash(url_for('redirect_to_short_url',urlhash=url.get_url_shortened()) ) 
        else:
            url = Data(url=form.url.data)
            db.session.add(url)
            db.session.commit() # commit firsts to get id
            url.short_url()
            db.session.commit()
            flash(url_for('redirect_to_short_url',urlhash=url.url_hash) )
    
    return render_template('home.html',title='Url Shortener by Cerlant', form=form, domain=domain)

@app.route('/<urlhash>')
def redirect_to_short_url(urlhash):
    data = Data.query.filter_by(url_hash=urlhash).first_or_404()
    if data is not None:
        return redirect(data.url)