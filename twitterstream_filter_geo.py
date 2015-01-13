import oauth2 as oauth
import urllib2 as urllib


# Go to https://apps.twitter.com to grab your api keys
api_key = "API_KEY_HERE"
api_secret = "API_SECRET_HERE"
access_token_key = "ACCESS_TOKEN_KEY_HERE"
access_token_secret = "ACCESS_TOKEN_SECRET_HERE"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

# Construct, sign, and open a twitter request using the hard-coded credentials above.
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

    # this code is used when outside the proxy
    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)
    '''
    # use this code when behind a proxy
    proxy = urllib.ProxyHandler({
      'http': 'http://proxy.com:80',
      'https': 'https://proxy.com:80'
    })
    opener = urllib.build_opener(proxy)
    urllib.install_opener(opener)
    '''

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/filter.json?track=%23arcgis"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()
