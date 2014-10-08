#!/usr/bin/env python
import sys
import urllib2
import re
import compare


if sys.version_info[1] >= 6:  import json
else: import simplejson as json

re_spid = re.compile(r"^[0-9a-zA-Z]{22}$")
re_spurl = re.compile(r"^http:\/\/open\.spotify\.com\/track\/([0-9a-zA-Z]{22})$")

url_api = "http://ws.spotify.com/lookup/1/.json?uri=http://open.spotify.com/track/"


def getSpotifyID(txt):
    if re_spid.match(txt):
        return txt
    m = re_spurl.match(txt)
    if m:
        return m.group(1)
    return None

def getAPIURL(txt):
    id = getSpotifyID(txt)
    if id:
        return url_api + id
    else:
        return None

def getInfoJSON(txt):
    url = getAPIURL(txt)
    if url:
        return urllib2.urlopen(url).read()
    else:
        return None

def getMetaInfo(txt):
    info_json = getInfoJSON(txt)
    if info_json:
        return json.loads(info_json)
    else:
        return None

def getTrackInfo(txt):
    meta_info = getMetaInfo(txt)
    if meta_info:
        track = meta_info["track"]
        artist = [a["name"] for a in track["artists"]]
        album = track["album"]["name"]
        track = track["name"]
        return artist, album, track
    else:
        return None

class Track(compare.Track):
    def __init__(self, txt):
        self.artists, self.album, self.track = getTrackInfo(txt)