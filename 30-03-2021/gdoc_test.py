
from googleapiclient import discovery
from oauth2client import client

import httplib2

# Google doc credential params
user_agent = "Drive API Python Quickstart"
token_uri = "https://accounts.google.com/o/oauth2/token"
revoke_uri = "https://accounts.google.com/o/oauth2/revoke"
client_id = "511801326402-5jo82okccra3utjuokvookijcqsk7jnv.apps.googleusercontent.com"
client_secret = "d630xUwk9RAsPXjr9VHvd6Jn"

def get_gdoc_service(access_token):
    '''
    Create and return the google API retrieval service and fetch the content from the given gdoc id
    '''

    credentials = client.OAuth2Credentials(
        access_token=access_token,
        refresh_token=None,
        token_expiry=None,
        user_agent=user_agent,
        token_uri=token_uri,
        revoke_uri=revoke_uri,
        client_id=client_id,
        client_secret=client_secret)
    return discovery.build('drive', 'v3', http=credentials.authorize(httplib2.Http()))
service = get_gdoc_service('ya29.a0AfH6SMBwCi1fGKfG9-x07V9HiI9vli62a5rQG_I90HG7eTpJXhtaSuDu4XRMZ7dhAplLZrtp4CczZHcyPAO_xuP66ZFs55Uho4SAeHsSO3oseqOt15R7WqNsmafYpdn-2rXAhEprpyR_H0yV816cCrocNrkghTBKRmgT7oBLi13YqOV39SurRe91dXNGnlEf9HDZJdzd1ICmllFUo8v0GBKlzwyxwRFZ0AtHZA')
image_file = service.files().get_media(fileId='16yaowzRuIemz3MHSSFsm_3GQJ-SK0oJ9').execute()
print(image_file)