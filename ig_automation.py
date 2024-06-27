import requests

graph_url = 'https://graph.facebook.com/v15.0/'

## 1. Uploading the photo inside the container
def post_image(caption='', image_url='',instagram_account_id='',access_token=''):
    url = graph_url + instagram_account_id + '/media'
    param = dict()
    param['access_token'] = access_token
    param['caption'] = caption
    param['image_url'] = image_url
    response = requests.post(url, params=param)
    response = response.json()
    return response

## 2. Publishing the container.
# creation_id is container_id
def publish_container(creation_id = '',instagram_account_id='',access_token=''):
    url = graph_url + instagram_account_id + '/media_publish'
    param = dict()
    param['access_token'] = access_token
    param['creation_id'] = creation_id
    response = requests.post(url,params=param)
    response = response.json()
    return response


def uploading_photo(captions:list[str] = [], image_urls:list[str] = [],instagram_account_id='',access_token=''):

    responses_ig = []
    if len(captions) != len(image_urls):
        print("Error-- The size of captions ")
        return 
    
    n = len(captions)
    for i in range(n):
        response_request = post_image(caption= captions[i], image_url= image_urls[i],instagram_account_id= instagram_account_id,access_token=access_token)
        response_upload = publish_container(creation_id = response_request['id'], instagram_account_id=instagram_account_id, access_toke=access_token )
        
        responses_ig.append([response_request, response_upload])

    return 
        

        
    
post_image()
caption = ""
image_url = ""
instagram_account_id = ""
access_token= ""
