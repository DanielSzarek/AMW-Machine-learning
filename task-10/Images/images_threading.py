import timeit
from urllib import request
import requests
from concurrent.futures import ThreadPoolExecutor


API_URL = "https://picsum.photos/v2/list"


def download_image(link):
    filename = link.split('id/')[1].replace("/", "-")
    request.urlretrieve(link, f"images_threading/{filename}.jpg")


def main():
    response = requests.get(API_URL)
    array = response.json()
    links = list(map(lambda item: item["download_url"], array))
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, links)


if __name__ == "__main__":
    time = timeit.Timer(main).timeit(number=1)
    print(f"THREADING - Time taken to download images: {time}")
