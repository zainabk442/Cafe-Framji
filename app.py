from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

from dotenv import load_dotenv
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = "change-this-later"
load_dotenv()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

class User(UserMixin):
    def __init__(self, id):
        self.id = id

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            user = User(id=1)
            login_user(user)

            return redirect(url_for("admin_bookings"))

        return "Invalid username or password"

    return render_template("admin_login.html")

def init_db():
    conn = sqlite3.connect("cafe_framji.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            guests TEXT NOT NULL,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/admin/bookings")
@login_required
def admin_bookings():

    conn = sqlite3.connect("cafe_framji.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bookings")

    bookings = cursor.fetchall()

    conn.close()

    return render_template(
        "admin.html",
        bookings=bookings
    )

@app.route("/admin/bookings/delete/<int:booking_id>", methods=["POST"])
def delete_booking(booking_id):

    conn = sqlite3.connect("cafe_framji.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM bookings WHERE id = ?",
        (booking_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("admin_bookings"))


@app.route("/admin/bookings/edit/<int:booking_id>", methods=["GET", "POST"])
def edit_booking(booking_id):

    conn = sqlite3.connect("cafe_framji.db")
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form.get("name")
        phone = request.form.get("phone")
        date = request.form.get("date")
        time = request.form.get("time")
        guests = request.form.get("guests")
        message = request.form.get("message")

        cursor.execute("""
            UPDATE bookings
            SET name = ?,
                phone = ?,
                date = ?,
                time = ?,
                guests = ?,
                message = ?
            WHERE id = ?
        """, (
            name,
            phone,
            date,
            time,
            guests,
            message,
            booking_id
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("admin_bookings"))

    cursor.execute(
        "SELECT * FROM bookings WHERE id = ?",
        (booking_id,)
    )

    booking = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_booking.html",
        booking=booking
    )

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/our-story")
def our_story():
    return render_template("our-story.html")


@app.route("/booking", methods=["POST"])
def booking():

    name = request.form.get("name")
    phone = request.form.get("phone")
    date = request.form.get("date")
    time = request.form.get("time")
    guests = request.form.get("guests")
    message = request.form.get("message")

    conn = sqlite3.connect("cafe_framji.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bookings
        (name, phone, date, time, guests, message)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, phone, date, time, guests, message))

    conn.commit()
    conn.close()

    return render_template(
        "index.html",
        booking_success=True,
        name=name,
        date=date,
        time=time,
        guests=guests
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)






# from flask import Flask, render_template, request
# import sqlite3

# app = Flask(__name__)

# def init_db():
#     conn = sqlite3.connect("cafe_framji.db")

#     cursor = conn.cursor()

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             phone TEXT NOT NULL,
#             date TEXT NOT NULL,
#             time TEXT NOT NULL,
#             guests TEXT NOT NULL,
#             message TEXT,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#     """)

#     conn.commit()
#     conn.close()

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/menu")
# def menu():
#     return render_template("menu.html")

# @app.route("/gallery")
# def gallery():
#     return render_template("gallery.html")

# @app.route("/our-story")
# def our_story():
#     return render_template("our-story.html")


# @app.route("/booking", methods=["POST"])
# def booking():

#     name = request.form.get("name")
#     phone = request.form.get("phone")
#     date = request.form.get("date")
#     time = request.form.get("time")
#     guests = request.form.get("guests")
#     message = request.form.get("message")

#     print("----- NEW BOOKING -----")
#     print("Name:", name)
#     print("Phone:", phone)
#     print("Date:", date)
#     print("Time:", time)
#     print("Guests:", guests)
#     print("Message:", message)
#     print("----------------------")

#     return f"""
#     <h1>Reservation Received!</h1>
#     <p>Thank you, {name}.</p>
#     <p>Your table request has been received.</p>
#     <p>Date: {date}</p>
#     <p>Time: {time}</p>
#     <p>Guests: {guests}</p>
#     <br>
#     <a href="/">Back to Café Framji</a>
#     """

# if __name__ == "__main__":
#     init_db()
#     app.run(debug=True)