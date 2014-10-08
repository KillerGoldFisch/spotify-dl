#!/usr/bin/env python
import os
import spotify
import groove
import compare
import argparse
import cout

def main():
    parser = argparse.ArgumentParser(description = 'Export Spotify playlist to MP3.')
    parser.add_argument('-f', '--filename', help='File holding list of HTTP spotify URIs.', required = True)
    args = vars(parser.parse_args())
    groove.getToken()
    with open( args['filename'], 'rb') as input:
        for line in input:
            print "~"*80

            sp_track = spotify.Track(line)

            cout.header(str(sp_track))

            if sp_track.getFileExists("."):
                cout.warning("File alredy exits")
                continue

            gs_tracks = compare.get_groove_tracks(groove.getResultsFromSearch(sp_track.getName()))

            match_score, match_track = sp_track.get_bets_match(gs_tracks)

            if not match_track:
                cout.warning("No match")
                continue

            groove.downloadSong(match_track.meta, sp_track.getFileName(), groove.chunk_report)




if __name__ == "__main__":
    main()