import datetime
import json
import time
import requests
import swagger_client
from pprint import pprint
from requests.auth import HTTPBasicAuth


AUTH_URL = "https://restapi.ayyeka.com/auth/token";
BASE_URL = "https://restapi.ayyeka.com/v2.0";

API_KEY = "API-KEY-HERE";
API_SECRET = "API-SECRET-HERE";

JWT_TOKEN = None
VALID_TO = None

configuration = swagger_client.Configuration()

class AuthError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

def get_access_token():
    """ Method that will return an AccessToken from Ayyeka REST-API oAuth2 Service   
    """        
    global JWT_TOKEN
    global VALID_TO

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials'}
    now = datetime.datetime.now()
    response = requests.post(AUTH_URL, auth=HTTPBasicAuth(
        API_KEY, API_SECRET), data=data, headers=headers)
    if response.status_code == 200:
        try:
            JWT_TOKEN = json.loads(response.content.decode())['access_token']
            expires_in = json.loads(response.content.decode())['expires_in']
            VALID_TO = now + datetime.timedelta(seconds=expires_in)
        except Exception as e:
            raise AuthError(None,"Error occured while decoding the auth content: {1}.", str(e))
    else:        
        raise AuthError( response.status_code,"Auth failed status_code {}".response.status_code)


def fetch_and_print_site_streams(site_id):

    stream_api_instance = swagger_client.StreamApi(swagger_client.ApiClient(configuration=configuration,header_name="Authorization",header_value='Bearer {0}'.format(JWT_TOKEN)))
    # Getting a list of steams by site id
    streams = stream_api_instance.stream_get_streams_by_site(site_id)

    if len(streams)>0 :
        pprint(streams)
    else:
        print("No sites")

def fetch_and_print_sites_and_streams():
    if JWT_TOKEN is None or datetime.datetime.now() >= VALID_TO:
        get_access_token()

    site_api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration=configuration,header_name="Authorization"
                                                                        ,header_value='Bearer {0}'.format(JWT_TOKEN)))
    # Getting a list of sites
    sites = site_api_instance.site_get_all_sites()
    
    if len(sites)>0 :
        pprint(sites)
        fetch_and_print_site_streams(sites[0]['id'])
    else:
        print("No sites")

def fetch_and_print_samples():
    sample_api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration=configuration,header_name="Authorization"
                                                        ,header_value='Bearer {0}'.format(JWT_TOKEN)))
    while(True):
        token_refreshed = False
        samples_reponse = None
        try:
            """ The first time you call this API, specify a sampleID or backfillHours to define the starting
            point from which to provide the batch of samples. In addition, set enableAck to true so that the
            system will not update its internal last delivered sample id field based on the last sample
            sent in this batch."""            
            samples_reponse = sample_api_instance.sample_get_samples_scalar_batch(enable_ack=False,backfill_hours=2)
        except AuthError as e:
            if e.status_code == 401:
                get_access_token()
                token_refreshed = True
        
        if samples_reponse.samples:
            pprint(samples_reponse)
        
        if token_refreshed or samples_reponse == None or samples_reponse.has_more == False:
            time.sleep(15*60)
        
        if JWT_TOKEN is None or datetime.datetime.now() >= VALID_TO:
            get_access_token()
            sample_api_instance = swagger_client.SampleApi(swagger_client.ApiClient(configuration=configuration,header_name="Authorization"
                                                        ,header_value='Bearer {0}'.format(JWT_TOKEN)))

def main():    
    fetch_and_print_sites_and_streams()
    fetch_and_print_samples()

if __name__ == "__main__":
    main()