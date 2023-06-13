import requests

lastfm_api_key = "your_api_key"

def get_similar_artists(artist_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist_name}&api_key={lastfm_api_key}&format=json"
    response = requests.get(url)
    data = response.json()
    similar_artists = data["similarartists"]["artist"]
    return similar_artists[:10] # Limit to 10 similar artists

def get_artist_tags(artist_name):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&artist={artist_name}&api_key={lastfm_api_key}&format=json"
    response = requests.get(url)
    data = response.json()
    tags = [tag["name"] for tag in data["toptags"]["tag"]]
    return tags

def calculate_similarity_rate(artist1, artist2):
    url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist1}&api_key={lastfm_api_key}&format=json"
    response = requests.get(url)
    data = response.json()
    similar_artists = [artist["name"] for artist in data["similarartists"]["artist"]]
    if artist2 in similar_artists:
        return round(1.0 / (similar_artists.index(artist2) + 1) * 100, 2)
    else:
        return 0

def display_similar_artists(similar_artists, artist_name):
    print(f"Similar artists for {artist_name}:")
    for artist in similar_artists:
        name = artist["name"]
        tags = get_artist_tags(name)
        similarity_rate = calculate_similarity_rate(artist_name, name)
        print(f"{name} ({tags[0]}) - {similarity_rate}%")
    print()

if __name__ == "__main__":
    artist_name = input("Enter an artist name: ")
    similar_artists = get_similar_artists(artist_name)
    display_similar_artists(similar_artists, artist_name)