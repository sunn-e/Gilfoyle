import requests
import time
from playsound import playsound
#import vlc


def get_rate(coin):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    res = requests.get(url)
    value = res.json()['bpi'][coin]['rate_float']
    print(value)
    return value


def suffer():
    """
    m = vlc.MediaPlayer("audio\\suffer.mp3")
    m.play()
    m.stop()
    """

    playsound('audio/suffer.mp3')


def gilfoyle():
    # whole day
    suffer_for_minutes = 24*60
    # bitcoin rate threshold
    threshold = 30772.71  # 4 jan 2021 11:30 IST
    for _ in range(suffer_for_minutes):
        monies = get_rate("USD")
        if monies < threshold:
            suffer()
        # sleep for 60 secs
        time.sleep(60)


if __name__ == "__main__":
    gilfoyle()
