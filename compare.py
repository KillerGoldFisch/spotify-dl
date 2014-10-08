#!/usr/bin/env python
import difflib
import os

def get_distance(a, b):
    return difflib.SequenceMatcher(None, a.upper(), b.upper()).ratio()

def get_distance_list(a, b):
    matches = []
    al = a[:]
    bl = b[:]
    for a in al:
        cur_v = 0.0
        for b in bl:
            v = get_distance(a, b)
            if v > cur_v:
                cur_v = v
        matches.append(cur_v)
    return sum(matches) / float(len(matches))


def _get_distance_track(a_album, a_artists, a_track, b_album, b_artists, b_track):
    d_album = get_distance(a_album, b_album)
    d_artist = get_distance_list(a_artists, b_artists)
    d_track = get_distance(a_track, b_track)
    return (1.0*d_album + 7.0*d_artist + 4.0*d_track)/12.0

def get_distance_track(track_a, track_b):
    return _get_distance_track(track_a.album, track_a.artists, track_a.track,
                               track_b.album, track_b.artists, track_b.track)

def get_groove_track(l):
    return Track([l["ArtistName"],], l["AlbumName"], l["SongName"], l)

def get_groove_tracks(s):
    tracks = []
    for m,l in enumerate(s):
        tracks.append(get_groove_track(l))
    return tracks

def get_best_match(track, tracks):
    best_t = None
    best_s = 0.0
    for t in tracks:
        score = track.compare(t)
        if score > best_s:
            best_s = score
            best_t = t
    return best_s, best_t

class Track:
    def __init__(self, artists, album, track, meta):
        self.artists = artists
        self.album = album
        self.track = track
        self.meta = meta

    def compare(self, track):
        return get_distance_track(self, track)

    def getName(self):
        return "%s - %s"%(", ".join(self.artists), self.track)

    def getFileName(self):
        return self.getName() + ".mp3"

    def getFileExists(self, path):
        return os.path.exists(os.path.join(path, self.getFileName()))

    def get_bets_match(self, tracks):
        return get_best_match(self, tracks)

    def __str__(self):
        return "Artists=%s \t| Album=%s \t| Track=%s"%(
            unicode(str(self.artists)).encode( "utf-8" ),
            unicode(self.album).encode( "utf-8" ),
            unicode(self.track).encode( "utf-8" ))

    def __repr__(self):
        return self.__str__()