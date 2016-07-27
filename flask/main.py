import os
from flask import Flask, render_template 


app = Flask(__name__)


@app.route('/')
@app.route('/<user>')
def index(user = None):
    return render_template("user.html", user=user)


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html",name = name)

@app.route('/shopping')
def food():
    food = ["cheese", "tuna", "beef", "toothpaste"]
    return render_template("shopping.html",food=food)


"""
#homepage routing
@app.route('/')
def index():
   return 'method used: %s' % request.method
    
@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "you are using POST"
    else:
        return "you are probably using GET"
"""   
    
    
"""    
@app.route('/tuna')
def tuna():
    return '<h2>tuna is gross</h2>'
    
@app.route('/profile/<username>')
def profile(username):
    return "hey there %s" %username 

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "postId number is:  %s" %post_id 
"""   
    
if __name__=="__main__":
    app.run(host=os.environ['IP'],port=int(os.environ['PORT']))
    