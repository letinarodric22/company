from flask import Flask, render_template
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432", database="company")
cur= conn.cursor()

@app.route('/') #'/' this is the landing page of the website
def helloworld():
    name = "Letina"
    
    return render_template("index.html", name=name)
@app.route("/customers")
def customer():
    cur.execute("SELECT * from customers")
    customer = cur.fetchall()
    print(customer)
    

    return render_template("customers.html", customer=customer)


if __name__ == "__main__":
    app.run(debug=True)