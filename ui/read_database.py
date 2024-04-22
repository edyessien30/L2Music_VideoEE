from logic.PlayList import PlayList

if __name__ == '__main__':
    all_videos, all_playlists = PlayList.read_data()

    print()
    print("All Videos:")
    for video in all_videos:
        print(video)
    print()
    print("All Playlists:")
    for playlist in all_playlists:
        print(playlist)