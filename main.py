from flask import Flask, render_template, request, redirect
from pyfunc import fetch_data, insert_customer
app = Flask(__name__)



@app.route('/') #'/' this is the landing page of the website
def helloworld():
    name = "Letina"
    
    return render_template("index.html", name=name)
@app.route("/customers")
def customer():
    customer = fetch_data("customers")
    print(customer)
    return render_template("customers.html", customer=customer)

@app.route('/addproducts', methods=["POST", "GET"])
def addproducts():
   if request.method=="POST":
      id = request.form["id"]
      firstname= request.form["firstname"]
      lastname=request.form["lastname"]
      email=request.form["quantity"]
      phone=request.form["phone"]

      print(id)
      print(firstname)
      print(lastname)
      print(email)
      print(phone)


if __name__ == "__main__":
    app.run(debug=True)