import json
import requests


response = requests.get('https://jsonplaceholder.typicode.com/albums')
albums = json.loads(response.text)
print(albums)

users_albums = {}
for album in albums:
    user_id = album['userId']
    if user_id in users_albums:
        users_albums[user_id] += 1
    else:
        users_albums[user_id] = 0

sorted_users_albums = sorted(
    users_albums.items(),
    key=lambda x: x[1],
    reverse=True
)

max_albums = sorted_users_albums[0][1]

users = []
for user_id, number_of_albums in sorted_users_albums:
    if number_of_albums == max_albums:
        users.append(str(user_id))

max_users = " & ".join(users)
print(max_users)

s = "s" if len(users) > 1 else ""
print(f"User{s}: {max_users} get {max_albums} albums")


def keep(album):
    return str(album['userId'] in users)


with open('filtered_data_file.json', 'w') as writer:
    filtered_albums = list(filter(keep, albums))
    json.dump(filtered_albums, writer, indent=2)
