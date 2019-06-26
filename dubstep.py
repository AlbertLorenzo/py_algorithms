def song_decoder(song):
    filtered = song.replace('WUB', '')
    return filtered.replace("", " ").strip()

print(song_decoder("AWUBBWUBC"))