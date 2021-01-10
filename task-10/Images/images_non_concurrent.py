import timeit
from urllib import request
import requests


API_URL = "https://picsum.photos/v2/list"


def download_image(link):
    filename = link.split('id/')[1].replace("/", "-")
    request.urlretrieve(link, f"images_non_concurrent/{filename}.jpg")


def main():
    response = requests.get(API_URL)
    array = response.json()
    links = list(map(lambda item: item["download_url"], array))
    for url in links:
        download_image(url)


if __name__ == "__main__":
    time = timeit.Timer(main).timeit(number=1)
    print(f"NON CONCURRENT - Time taken to download images: {time}")
