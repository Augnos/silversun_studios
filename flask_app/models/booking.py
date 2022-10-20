from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Booking:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ---------- Get All Bookings -----------
    @classmethod
    def select_all_bookings(cls):
        query = "SELECT * FROM bookings;"
        results = connectToMySQL('schema').query_db(query)
        bookings = []
        for booking in results:
            bookings.append(cls(booking))
        return bookings


    # ---------- Insert New Booking -----------
#     ---psuedocode---
#     Insert booking parameters: name, calendar(room), start_time, end_time, comment
#     GET calendar bookings in a list
#     Check for booking conflicts:
#         For conflicts, return error for user to retry booking.
#         If no conflicts, create new event with title as user's name.
    @classmethod
    def insert_booking(cls, data):
        query = "INSERT INTO bookings ( created_at, updated_at ) VALUES ( NOW() , NOW() );"
        return connectToMySQL('schema').query_db(query, data)
