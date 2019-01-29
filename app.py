from database import *
from os import *
from flask import Flask, flash , render_template, url_for , request ,session, escape, request, redirect
from werkzeug.utils import secure_filename

from flask import session as login_session #login_session can store info about current user

app = Flask(__name__)

UPLOAD_FOLDER = '/static/path'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "in order to use login_session you need a secret_key"


@app.route('/')
def AboutUs():
	return render_template('aboutUs.html')


@app.route('/register' , methods=['GET' , 'POST'])
def register():
	if request.method== 'GET':
		return render_template('signup.html')
	else:	
		username = request.form['txt_username']
		email = request.form['txt_email']
		password = request.form['txt_password']
		SignUp(username , email , password)
		login_session['username'] = username
		return redirect(url_for('home_page' ))
 

@app.route('/LogIn', methods=['GET' , 'POST'])
def LogIn():
	if request.method== 'GET':
		return render_template('login.html')
	else:	
		username = request.form['txt_username']
		password = request.form['txt_password']
		#When they login, store the username in session
		login_session['username'] = username
		u=query_by_name(username)
		if u is not None and u.uname==username and u.password==password:
			return redirect(url_for('home_page' ))
		else:
			return render_template('login.html')


@app.route('/home', methods=['GET'])
def home_page():
	if request.method== 'GET':	
		posts = query_all_posts()
		print([p.uname for p in posts])
		return render_template('home.html' ,posts=posts)
	posts = query_all_posts()	
	return render_template('home.html' ,posts=posts)

@app.route('/tips', methods=['GET'])
def Tips():
	if request.method=='GET':
		return render_template('tips.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/post', methods=['GET' , 'POST'])
def Post():
	if request.method=='GET':
		return render_template('post.html')
	if request.method == 'POST':
		print("POSTED!!!")
		#Check if someone is logged in by seeing if "username" is in login_session
		if 'username' in login_session:
			uname=login_session['username'] #later we can get the username back!
			print((uname))

		else: #not logged in, you decide what to do if this happens
			uname = ""

		text=request.form['txt_text']
		# check if the post request has the file part

		if 'file' not in request.files:
			print('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			print('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			file.save('static/'+file.filename)
			print('here')
		posts=query_all_posts()

		#Store the FILENAME in the database, then use that as the src for the img
		add_post(uname,text,file.filename)

		return redirect(url_for('home_page'))

if __name__ == '__main__':
    app.run(debug=True)
# @app.route('/sign_out')
# def sign_out():
#     session.pop('username')
#     return render_template('login.html')


# @app.route('/home' , methods=['GET' , 'POST'])
# def home_page():
# 	if session.get('username')==None:
# 		return redirect(url_for('LogIn_page'))
# 	if request.method== 'GET':	
# 		posts = query_all_posts()
# 		return render_template('home.html' ,posts=posts , username=session.get('username') )
# 	posts = query_all_posts()	
# 	return render_template('home.html' ,posts=posts , username=session.get('username') )
