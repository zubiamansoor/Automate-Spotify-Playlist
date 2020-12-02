
# 1. Log into Youtube
# 2. Grab our liked videos 
# 3. Create a new playlist
    # a. First, find a way to interact with Spotify, i.e, using an API
    # b. Send a request to the API that uses your user id to make a playlist
    # Good reference: https://developer.spotify.com/documentation/web-api/reference/playlists/create-playlist/
# 4. Search for the song
# 5. Add new song to the Spotify playlist

# libraries
import json
import requests
from spotify_info import spotify_user_id, spotify_token

class CreatePlaylist:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    # 1. Log into Youtube
    def get_youtube_client(self):
        pass

    # 2. Grab our liked videos:
    def get_liked_videos(self):
        pass
    
    # 3. Create a new playlist:
    def create_playlist(self):
        
        # this step converts python objects into json strings
        request_body = json.dumps({
            "name": "Youtube Liked Videos",
            "description": "Youtube Liked Songs",
            "public": True

        })

        # a. Interact with Spotify
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id) 
        # this step specifies the endpoint
        # the function "format" inserts value into the placeholder using curly braces

        # b. Make a POST request to the Spotify API Webpage
        # the first argument is the url, second is data in the form of a dictionary
        response = requests.post(
            query,
            data = request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)

            }
        )
        
        # the "response" body contains the created playlist object in JSON format
        response_json = response.json()
        # print(response_json)

        # playlist id
        return response_json["id"]
         
    # 4. Search for the song
    def get_spotify_uri(self, song_name, artist):
        '''Search for the song by writing queries'''
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        # use hexcodes %20 or + for spaces, and %3A for :

        response = requests.get(
            query,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # get the first song
        uri = songs[0]["uri"]

        return uri

    # 5. Add new song to Spotify playlist
    def add_song_to_playlist(self):
        pass

