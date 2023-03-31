# step - 1 IMPORT FLASK
from flask import Flask, request, render_template

# step -2 CREATE THE OBJECT WITH A PARAMETER __NAME__
app = Flask(__name__)

user_names =['nagasundarchokkakula','allu-saikiran-53566221b','anil-eagala','vicharapu-vinay-kumar-62b099192']


# https://www.linkedin.com/in/nagasundarchokkakula/
# https://www.linkedin.com/in/allu-saikiran-53566221b/
# https://www.linkedin.com/in/anil-eagala/
# https://www.linkedin.com/in/vicharapu-vinay-kumar-62b099192/



# step 3 - CREATE AN END POINT using routes and bind them witha functionality

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/search',methods=['GET','POST'])
def search_fun():
    if request.method == 'POST':
        return "welcome to the search page using POST Req"
    else:
        return render_template('search.html')


@app.route('/add',methods=['POST','GET'])
def add_fun():
    a = request.form.get('var_1')
    b = request.form.get('var_2')
    return str(int(a)+int(b))

@app.route('/in/<user>')
def profile_page(user):
    if user in user_names:
        return f"Welcome {user}"
    else:
        return "Username not found"


# step 4 - RUN THE APPLICATION
if __name__ == '__main__' :
    app.run(debug=True)