from flask import redirect, request, flash
from flask_app import app
from flask_app.models.booking import Booking, studio_calendar


# Google Cal SELECT Route templates to get studio events. Will implement in version 2.
# # ---------- Bookings (all) Page -----------
# @app.route("/bookings")
# def bookings():
#     return render_template("bookings.html", all_bookings = Booking.select_all_bookings())

# # ---------- Bookings (one) Page -----------
# @app.route("/bookings/<id>")
# def bookings_one(id):
#     return render_template("show_booking.html", booking = Booking.get_one({"id":id}))


# ------------------------------------------------------
# -------------------- POST Routes ---------------------
# ------------------------------------------------------

# ---------- INSERT New Booking Post -----------
@app.route('/insert/booking', methods=["POST"])
def insert_booking():
    
    # Form input error handling
    formError = False
    if not request.form["name"]:
        flash("A name (or event title) is required.")
        formError = True
    if not request.form["date"]:
        flash("Date is required.")
        formError = True
    if request.form["start_time"] > request.form["end_time"]:
        flash("Start time must be before end time.")
        formError = True
    if not request.form["start_time"]:
        flash("Start time is required.")
        formError = True
    if not request.form["end_time"]:
        flash("End time is required.")
        formError = True
    if formError: 
        return redirect('/booking')
    
    data = {
        "start": {
            "dateTime": (str(request.form["date"]) + "T" + str(request.form["start_time"]) + ":00-07:00"),
            "timeZone": "America/Los_Angeles"
        },
        "end": {
            "dateTime": (str(request.form["date"]) + "T" + str(request.form["end_time"]) + ":00-07:00"),
            "timeZone": "America/Los_Angeles"
        },
        "summary": request.form["name"],
        # 'attendees': [
        #     {'email': request.form["email"]},
        # ]
    }
    
    print(data)
    Booking.insert_booking(data, studio_calendar(request.form["studio"]))
    return redirect('/booking')


# # ---------- UPDATE Booking Post -----------
# @app.route('/bookings/<id>/update', methods=["POST"])
# def edit_booking(id):
#     data = {
#         "id": id,
#         "name": request.form["name"],
#     }
#     Booking.update_booking(data)
#     return redirect('/')


# # ---------- DELETE Booking Post -----------
# @app.route('/bookings/<id>/delete')
# def delete_booking(id):

#     data = {"id": id}
#     Booking.delete(data)
#     return redirect('/')
