import argparse
import os
import time
import random
import requests
import ctypes
import platform




#get walpaper
def get_wallpaper():
    #random number
    num = random.randint(1,99)

    #set your api key here 
    payload = {'Authorization': '563492ad6f9170000100000109cc3487bd024b1098f4c60deee2fc77'}

    #set search query
    query = 'Tokyo'

    #url for pexels
    url = 'https://api.pexels.com/v1/search?per_page=1&page=' + str(num) + '&query=' + query

    #send request for the page
    res = requests.get(url, headers=payload)

    if res.status_code == 200:
        img_url = res.json().get('photos')[0]['src']['original']

        img = requests.get(img_url)

        with open('temp.jpg', 'wb') as f:
            f.write(img.content)

    else:
        print('error in making http request')





def set_wallpaper():
    get_wallpaper()
    #check the operating system
    system_name = platform.system().lower()
    path = ''
    if system_name == 'linux':
        path = os.getcwd()+'/temp.jpg'
        command = "gsettings set org.gnome.desktop.background picture.uri file:" + path
        os.system(command)
    elif system_name == 'windows':
        path = os.getcwd() +'//temp.jpg'
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="Enter time in minutes ")

    args = parser.parse_args()
    minute = int(args.time)
    while(True):
        time.sleep(minute*60)
        set_wallpaper()