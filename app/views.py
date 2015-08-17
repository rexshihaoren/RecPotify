import os
from flask import Flask, render_template, send_from_directory, session, request,url_for, redirect, flash
from flask_oauthlib.client import OAuth, OAuthException
# from app import app, db, lm, spotify, oauth, log
from app import app, spotify, log

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/login')
def login():
    log.debug(type(spotify))
    log.debug(spotify.__dict__)
    callback=url_for('oauth_authorized',
        next=request.args.get('next')  or None, _external = True)
    log.debug("Callback url: %s" % callback)
    return spotify.authorize(callback = callback)


@app.route('/callback')
def oauth_authorized():
    next_url = request.args.get('next') or url_for('index')
    resp = spotify.authorized_response()
    log.debug("Reponse is %s; is of type %s" % (resp,type(resp)))
    if resp is None:
        flash('Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        ), category='warning')
        return redirect(next_url)
    if isinstance(resp, OAuthException):
        log.debug('resp is OAuthException')
        flash('Access denied: %s' % resp.message, category='warning')
        return redirect(next_url)
    session['spotify_token'] = (resp['access_token'], '')
    log.debug('Requesting user information.....')
    # user info
    me = spotify.get_user()
    log.debug('Getting user info success!')
    log.debug('User info %s' %me.data)
    session['logged_in'] = True
    session['user'] = me.data['display_name']
    flash('Logged in as id={0} name={1}'.format(
        me.data['id'],
        me.data['display_name']), category = 'success')
    return redirect(next_url)

@spotify.tokengetter
def get_spotify_token(token=None):
    return session.get('spotify_token')

@app.route('/logout')
def logout():
    session.clear()
    session.pop('user', None)
    session['logged_in'] = False
    flash('You were signed out', category='info')
    return redirect(request.referrer or url_for('index'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    # get current user_profile
    profile = spotify.get_user()
    followed_artists = spotify.get_followed_artists()
    return render_template('user.html', profile=profile.data, followed_artists=followed_artists.data)

