from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

studio_a_id = "c_1887fvbjsimgghkbmqeu2kirblq9q@resource.calendar.google.com"
studio_b_id = "c_188bk9jmjf75uge4g4319luuql6q8@resource.calendar.google.com"
studio_c_id = "c_18896sfskcn9mg25l00tet4jannn2@resource.calendar.google.com"
live_room_id = "c_1885ahjvknvmogg9ldra4ls1m37fc@resource.calendar.google.com"
timeZone = "America/Los_Angeles"

class Booking:
    def __init__(self, data):
        self.id = data['id']
        self.calendarId = data['calendarId']
        self.summary = data['summary']
        self.description = data['description']
        self.start = data['start']
        self.end = data['end']
        self.attendees = data['attendees']


    # ---------- Get All Bookings -----------
    @classmethod
    def select_all_bookings(cls):
        event = service.events().get(calendarId='primary', eventId='eventId').execute()
        print event['summary']

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
