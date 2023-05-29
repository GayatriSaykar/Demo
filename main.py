from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__,static_folder="./frontend/build", static_url_path="/")


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'digitalflake'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        details = request.form
        email = details['email']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("select * from Admin")
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('../digitalflakee/src/login.js')


if __name__ == '__main__':
    app.run()
