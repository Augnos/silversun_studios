from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'flask_app/config/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)



def studio_calendar(studio):
    if studio == "studio_a":
        return "c_1887fvbjsimgghkbmqeu2kirblq9q@resource.calendar.google.com"
    if studio == "studio_b":
        return "c_188bk9jmjf75uge4g4319luuql6q8@resource.calendar.google.com"
    if studio == "studio_c":
        return "c_18896sfskcn9mg25l00tet4jannn2@resource.calendar.google.com"
    # if studio == "live_room" return "c_1885ahjvknvmogg9ldra4ls1m37fc@resource.calendar.google.com"

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
        service = build('calendar', 'v3', credentials=None)

        response = service.events().insert(calendarId=studio_calendar,body=data).execute()
        print(response)
