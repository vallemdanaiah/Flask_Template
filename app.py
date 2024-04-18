from flask import render_template,redirect,url_for,request

from flask import Flask 

# Create a Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')


registered_users = []
@app.route('/register',methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        mobile = request.form['mobile']
        address = request.form['address']
        state = request.form['state']
        qualification = request.form['qualification']
        registered_users.append({"username": username, "email": email, 'password':password,'mobile':mobile,'address':address,'state':state,'qualification':qualification})
        return redirect(url_for('registered_list'))
    return render_template('register.html')


@app.route('/registered_list')
def registered_list():
    return render_template('registered_users.html', users=registered_users)















@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        # use = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # mobile = request.form['mobile']
        # address = request.form['address']
        # state = request.form['state']
        # qualification = request.form['qualification']
        
        
        return redirect(url_for('userhomepage'))    
    return render_template('login.html')
@app.route('/userhomepage')
def userhomepage():
    return render_template('users/userhome.html')


@app.route('/users')
def users():
    return render_template('users.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True,port=7000)
