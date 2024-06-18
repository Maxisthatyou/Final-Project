from pytube import YouTube

def download_youtube_video(url, path):
    try:

        yt = YouTube(url)

        stream = yt.streams.get_highest_resolution()

        stream.download(output_path=path)
        
        print(f"Downloaded: {yt.title}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    video_url = input("Enter the URL of the YouTube video: ")
    
    save_path = input("Enter the path to save the downloaded video (e.g., /path/to/download/folder): ")
    
    download_youtube_video(video_url, save_path)