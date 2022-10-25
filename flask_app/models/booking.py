# from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.Google import create_service

CLIENT_SECRET_FILE = 'flask_app/config/credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def studio_calendar(studio):
    if studio == "studio_a":
        return "c_1887fvbjsimgghkbmqeu2kirblq9q@resource.calendar.google.com"
    if studio == "studio_b":
        return "c_188bk9jmjf75uge4g4319luuql6q8@resource.calendar.google.com"
    if studio == "studio_c":
        return "c_18896sfskcn9mg25l00tet4jannn2@resource.calendar.google.com"
    if studio == "live_room":
        return "c_1885ahjvknvmogg9ldra4ls1m37fc@resource.calendar.google.com"

# def RFC_converter(date, time):


class Booking:
    def __init__(self, data):
        self.start = data['start']
        self.end = data['end']
        self.summary = data['summary']
        # self.attendees = data['attendees']
        # self.calendar = data['calendar']

    # ---------- Get All Bookings -----------
    # @classmethod
    # def select_all_bookings(cls):
    #     event = service.events().get(calendarId='primary', eventId='eventId').execute()
    #     print event['summary']

    # ---------- Insert New Booking -----------
    @classmethod
    def insert_booking(cls, data, studio_calendar):
        response = service.events().insert(calendarId=studio_calendar,body=data).execute()
        print(response)
