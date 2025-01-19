# MA YouTube Video And Playlists Downloader 🎥

## Overview 🌟
This is a YouTube video downloader tool using yt-dlp. The program allows you to download videos and playlists from YouTube with additional options for quality, format, audio extraction, and subtitle downloading. You can specify your cookies to bypass restrictions, and the tool supports downloading in MP4, MKV, and other formats.

## Features ✨
- Download individual YouTube videos or entire playlists 📥
- Download videos in various formats like MP4, MKV, etc. 🎞️
- Option to extract audio as MP3 from videos 🎶
- Download subtitles in SRT format for supported videos 💬
- Supports specifying the video quality (e.g., 360p, 720p, 1080p, etc.) 🖥️
- Automatically detects and processes YouTube playlists 🔄

## System Requirements 💻
To use this tool, you need the following:
- **Python 3.x** 🐍 (If you don't have Python, you can download it from [here](https://www.python.org/downloads/))
- **yt-dlp** installed (Run `pip install yt-dlp` in your terminal to install it) 🛠️
- **FFmpeg** installed for video and audio processing (Download FFmpeg from [here](https://ffmpeg.org/download.html) and follow the installation instructions) 🎬
- **Tkinter** installed (Usually comes pre-installed with Python, but if not, install it using `pip install tk`) 🖥️
- **ttkbootstrap** installed (For Bootstrap-themed Tkinter interface) (Install via `pip install ttkbootstrap`) 💠

## How to Extract Cookies 🍪
To extract cookies for yt-dlp, use the **Get cookies.txt Locally** extension for your browser. Follow the instructions below:

### Extract Cookies in Chrome 🌐
1. Go to the [Chrome Web Store](https://chrome.google.com/webstore/detail/get-cookiestxt-locally) and install the extension. 🛒
2. Open YouTube or the site from which you want to download videos. 🎥
3. Click on the extension's icon in the browser's toolbar. 🖱️
4. Click "Export as" and save the `cookies.txt` file locally. 📂

### Extract Cookies in Firefox 🌍
1. Go to the [Firefox Add-ons page](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/) for the **Cookies.txt** extension. 🔌
2. Install the extension in Firefox. 🦊
3. Open the website from which you want to download content (e.g., YouTube). 🎬
4. Click the extension icon in the Firefox toolbar and export the cookies to a `cookies.txt` file. 📄

## Running the Downloader 🚀
After setting up the required tools and extracting cookies, follow these steps to download a video or playlist:
1. Enter the YouTube or video URL in the provided field. You can paste the URL of a single video or an entire playlist. 🌐
2. If you are downloading a playlist, the program will automatically detect the playlist and offer an option to download all the videos in that playlist. 🎞️
3. Choose the extracted `cookies.txt` file using the "Browse" button. 📂
4. Choose the download location where the video or playlist will be saved. 📥
5. Select the quality and format (MP4, MKV, etc.) for the video(s). 🎥
6. Click "Download Video/Playlist" to start the download process. ⬇️

## Advanced Options 🔧
- **Audio Only**: If you choose to download only the audio, the program will download the MP3 version of the video. 🎧
- **Subtitles**: You can download subtitles in SRT format for videos that support them. 💬
- **Formats**: The program allows you to choose the format of the downloaded video, including MP4, MKV, and other supported formats. 🎞️

## Common Issues ❗
### Errors during download ⚠️
If you encounter an error during the download process, ensure that:
- The cookies file is correct and contains valid cookies. ✅
- The video URL is valid and not restricted in your region. 🌍
- Your internet connection is stable. 🌐

If the error persists, check the console for additional information and update the software tools (`yt-dlp`) to the latest version. 🔄

## License 📜
Copyright 2025 - Murtaza Akbari
