"""
Author:       Brenden Morton
Date started: 8-12-21
"""
# Goal:
'''
Be able to:
    1) Create folders
    2) Add files to folders
    3) Add people to folders
    4) Remove folders
'''
#from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

class DriveShare():



    # Initialize connection to google drive account
    # ! Need to figure out what else to add
    def __init__(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        self.service = build('drive', 'v3', credentials=creds)

        
    def test(self):
         # Call the Drive v3 API
        results = self.service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))



    # Adds a new folder to the drive
    def create_folder(self):
        pass

    # Removes a folder from the drive
    def delete_folder(self):
        pass

    # Shares the folder with a list of users
    def share_folder(self):
        pass

    # Adds files to a folder
    def insert_to_folder(self):
        pass




drive = DriveShare()
drive.test()
#drive.create_folder()
#drive.share_folder()
#drive.insert_to_folder()
#drive.delete_folder()