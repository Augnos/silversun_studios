# from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.auth import create_service

# Auth service build parameters
client_secret_file = 'flask_app/config/credentials.json'
api_name = 'calendar'
api_version = 'v3'
scopes = ['https://www.googleapis.com/auth/calendar.events']

service = create_service(client_secret_file, api_name, api_version, scopes)

# Returns calendar ID depending on studio selected
def studio_calendar(studio):
    if studio == "studio_a":
        return "c_1887fvbjsimgghkbmqeu2kirblq9q@resource.calendar.google.com"
    if studio == "studio_b":
        return "c_188bk9jmjf75uge4g4319luuql6q8@resource.calendar.google.com"
    if studio == "studio_c":
        return "c_18896sfskcn9mg25l00tet4jannn2@resource.calendar.google.com"
    if studio == "live_room":
        return "c_1885ahjvknvmogg9ldra4ls1m37fc@resource.calendar.google.com"

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
