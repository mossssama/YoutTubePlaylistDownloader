from pytube import Playlist


def install():
    print('Enter URL Here: ')
    links = input('')
    play_list = Playlist(links)
    print('Enter Your path: ')
    direction = input('')

    for video in play_list.videos:
        print("Currently Downloading this video: " + video.title)
        video.streams.get_highest_resolution().download(direction)
    print('Download successfully completed')


print('Welcome to Youtube high quality playlist downloader')
install()
print('\n\tThanks for using this script;    Eng.  Mohamed Osama')

k = input("\nPress close to exit")
