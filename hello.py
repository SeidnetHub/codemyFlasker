from flask import Flask, render_template


#Create a Flask Instance
app = Flask(__name__)

# CreTE a route decorator
@app.route('/')

#def index():
 #   return "<h1>My First Page!</h1>"
 #Filter-----
 #Capitalize, safe, lower, upper, trim, title, striptags ....



def index():
    first_name = "Seid"

    favorite_pizza =["pepperoni", "cheese", "mushrooms", 41]
    return render_template("index.html", first_name=first_name,
    favorite_pizza = favorite_pizza)


#localhost :5000/user/Seid
@app.route('/user/<name>')
def user(name):
   # return "<h1>Hello {}</h1>".format(name)

   return render_template("user.html", user_name = name)
        
#Create Custom Error Pages

#Invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500




if __name__=='__main__':
    app.run(debug=True)