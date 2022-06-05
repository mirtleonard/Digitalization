from __future__ import print_function
from django.core.files.storage import default_storage as storage
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
from oauth2client import file, client, tools
from googleapiclient import discovery
from django.conf import settings
from httplib2 import Http
import os, io, shutil

SCOPES = 'https://www.googleapis.com/auth/drive.file'
cwd = os.getcwd() + '/googleAPI'
store = file.Storage(cwd + '/storage.json')
creds = store.get()
if creds.invalid:
    #creds.refresh(Http())
    flow = client.flow_from_clientsecrets(cwd + '/oauth.json', SCOPES)
    creds = tools.run_flow(flow, store)

DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

def createFolder(name):
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = DRIVE.files().create(body=file_metadata,
                                    fields='id').execute()
    return file.get('id')


def downloadFiles(folder_name):
    hdd = shutil.disk_usage("/")
    print (hdd.free / (1024 ** 2))
    if (hdd.free / (1024 ** 2) <= 50):
        clearStorage();
    folder_id = searchFile(folder_name)
    if not folder_id:
        return
    files = DRIVE.files().list(q="'{}' in parents".format(folder_id)).execute().get('files', [])
    for file in files:
        request = DRIVE.files().get_media(fileId=file['id'])
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print ("Download %d%%." % int(status.progress() * 100))

        storage.save(os.path.join(settings.MEDIA_ROOT, folder_name + '/img.png') , fh)

def deleteFile(folder_name):
    folder_id = searchFile(folder_name)
    if folder_id:
        DRIVE.files().delete(fileId=folder_id).execute()

def searchFile(name):
    try:
        return DRIVE.files().list(q="name='{}'".format(name)).execute().get('files', [])[0]['id']
    except:
        return None

def saveFiles(photos, folder_name):
    folder_id = searchFile(folder_name)
    if not folder_id:
        folder_id = createFolder(folder_name)
    for photo in photos:
        file_metadata = {
            'name' : photo.name,
            'parents' : [folder_id],
        }
        media = MediaIoBaseUpload(photo, mimetype='image/jpeg')
        DRIVE.files().create(body=file_metadata,
                             media_body=media,
                             fields='id').execute()

def clearStorage(path = ''):
    try:
        shutil.rmtree(settings.MEDIA_ROOT + path)
    except:
        pass

#print(searchFile("activity30"));
