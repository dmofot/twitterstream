Streaming Twitter to File
=========================

Python scripts for accessing the public Twitter streaming API.  *twitterstream_public.py* and *twitterstream_filtered_geo.py* are examples of the straight [Twitter API](https://dev.twitter.com/streaming/overview), while *tweepy_geo.py* uses the [Tweepy](https://github.com/tweepy/tweepy) python module.  In order to use these scripts, you will need:
* Consumer Key (API Key)
* Consumer Secret (API Secret)
* Access Token
* Access Token Secret

which you'll need to visit [Twitter's App Manager](https://apps.twitter.com/) to create a new app to receive the above items.  Simply plug your keys into the scripts and run using one of the usage examples below.

## Usage Examples

This command pipes the output to a *json* or *txt* file. Stop the script with Ctrl-C, but wait a few minutes (at the very least) for data to accumulate.  If you run a filtered stream and the output file has a size of 0 bytes, you probably didn't let it run long enough.

* ***Recommended Method*** - Run one of the scripts and save the output to json file <br>
`$ python twitterstream_public.py > public_stream.json` <br>
`$ python twitterstream_filtered_geo.py > geo.json` <br>
`$ python tweepy_geo.py > tweepy_geo.json` <br>

* Run one of the scripts and save output to text file <br>
`$ python twitterstream_public.py > public_stream.txt` <br>
`$ python twitterstream_filtered_geo.py > geo.txt` <br>
`$ python tweepy_geo.py > tweepy_geo.json` <br>

Once the script is stopped (Ctrl + C), you should be able to see the tweets in your output file.
**NOTE: ** The public stream is Twitter's 1% live stream and will produce a lot more tweets than any filtered stream.