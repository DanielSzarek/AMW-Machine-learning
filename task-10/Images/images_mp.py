import timeit
from urllib import request
import requests
import multiprocessing


API_URL = "https://picsum.photos/v2/list"


def download_image(link):
    filename = link.split('id/')[1].replace("/", "-")
    request.urlretrieve(link, f"images_mp/{filename}.jpg")


def main():
    response = requests.get(API_URL)
    array = response.json()
    links = list(map(lambda item: item["download_url"], array))

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(download_image, [url for url in links])


if __name__ == "__main__":
    time = timeit.Timer(main).timeit(number=1)
    print(f"MULTIPROCESSING - Time taken to download images: {time}")
