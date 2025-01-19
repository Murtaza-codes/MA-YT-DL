<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="yt-dlp YouTube Downloader - Download videos, playlists, and audio from YouTube in multiple formats like MP4, MKV, and MP3.">
    <meta name="keywords" content="YouTube downloader, yt-dlp, download videos, download playlists, YouTube MP4, YouTube MKV, download audio, cookies extraction">
    <meta name="author" content="Your Name">
    <title>yt-dlp Downloader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }

        .container {
            max-width: 900px;
            margin: 30px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h1, h2 {
            text-align: center;
            color: #333;
        }

        h3 {
            color: #333;
            margin-top: 20px;
        }

        ul {
            margin: 20px 0;
            padding-left: 20px;
        }

        pre {
            background-color: #f8f8f8;
            padding: 10px;
            border-radius: 4px;
            border: 1px solid #ddd;
            font-size: 14px;
            overflow-x: auto;
        }

        .section {
            margin-bottom: 40px;
        }

        code {
            background-color: #f1f1f1;
            padding: 2px 5px;
            border-radius: 4px;
        }

        .note {
            background-color: #ffe8d6;
            padding: 10px;
            border: 1px solid #f1c27d;
            border-radius: 5px;
            margin-top: 20px;
        }

        .note ul {
            padding-left: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>MA YouTube Video And Playlists Downloader</h1>

        <div class="section">
            <h2>Overview</h2>
            <p>This is a YouTube video downloader tool using yt-dlp. The program allows you to download videos and playlists from YouTube with additional options for quality, format, audio extraction, and subtitle downloading. You can specify your cookies to bypass restrictions, and the tool supports downloading in MP4, MKV, and other formats.</p>
        </div>

        <div class="section">
            <h2>Features</h2>
            <ul>
                <li>Download individual YouTube videos or entire playlists.</li>
                <li>Download videos in various formats like MP4, MKV, etc.</li>
                <li>Option to extract audio as MP3 from videos.</li>
                <li>Download subtitles in SRT format for supported videos.</li>
                <li>Supports specifying the video quality (e.g., 360p, 720p, 1080p, etc.).</li>
                <li>Automatically detects and processes YouTube playlists.</li>
            </ul>
        </div>

        <div class="section">
            <h2>System Requirements</h2>
            <ul>
                <li>Python 3.x</li>
                <li>yt-dlp installed (You can install it via <code>pip install yt-dlp</code>)</li>
                <li>A web browser with the <strong>Get cookies.txt Locally</strong> extension installed for cookies extraction.</li>
            </ul>
        </div>

        <div class="section">
            <h2>How to Extract Cookies</h2>
            <p>To extract cookies for yt-dlp, use the <strong>Get cookies.txt Locally</strong> extension for your browser. Follow the instructions below:</p>
            <h3>Extract Cookies in Chrome</h3>
            <ul>
                <li>Go to the <a href="https://chrome.google.com/webstore/detail/get-cookiestxt-locally" target="_blank">Chrome Web Store</a> and install the extension.</li>
                <li>Open YouTube or the site from which you want to download videos.</li>
                <li>Click on the extension's icon in the browser's toolbar.</li>
                <li>Click "Export as" and save the <code>cookies.txt</code> file locally.</li>
            </ul>
            <h3>Extract Cookies in Firefox</h3>
            <ul>
                <li>Go to the <a href="https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/" target="_blank">Firefox Add-ons</a> page for the <strong>Cookies.txt</strong> extension.</li>
                <li>Install the extension in Firefox.</li>
                <li>Open the website from which you want to download content (e.g., YouTube).</li>
                <li>Click the extension icon in the Firefox toolbar and export the cookies to a <code>cookies.txt</code> file.</li>
            </ul>
        </div>

        <div class="section">
            <h2>Running the Downloader</h2>
            <p>After setting up the required tools and extracting cookies, follow these steps to download a video or playlist:</p>
            <ul>
                <li>Enter the YouTube or video URL in the provided field. You can paste the URL of a single video or an entire playlist.</li>
                <li>If you are downloading a playlist, the program will automatically detect the playlist and offer an option to download all the videos in that playlist.</li>
                <li>Choose the extracted <code>cookies.txt</code> file using the "Browse" button.</li>
                <li>Choose the download location where the video or playlist will be saved.</li>
                <li>Select the quality and format (MP4, MKV, etc.) for the video(s).</li>
                <li>Click "Download Video/Playlist" to start the download process.</li>
            </ul>
            <p>The program will automatically fetch available formats for each video in the playlist and download them in the selected quality and format. If you select "Audio Only", it will download the audio files for each video in MP3 format.</p>
        </div>

        <div class="section">
            <h2>Advanced Options</h2>
            <ul>
                <li><strong>Audio Only:</strong> If you choose to download only the audio, the program will download the MP3 version of the video.</li>
                <li><strong>Subtitles:</strong> You can download subtitles in SRT format for videos that support them.</li>
                <li><strong>Formats:</strong> The program allows you to choose the format of the downloaded video, including MP4, MKV, and other supported formats.</li>
            </ul>
        </div>

        <div class="section">
            <h2>Common Issues</h2>
            <div class="note">
                <h3>Errors during download</h3>
                <p>If you encounter an error during the download process, ensure that:</p>
                <ul>
                    <li>The cookies file is correct and contains valid cookies.</li>
                    <li>The video URL is valid and not restricted in your region.</li>
                    <li>Your internet connection is stable.</li>
                </ul>
                <p>If the error persists, check the console for additional information and update the software tools (yt-dlp) to the latest version.</p>
            </div>
        </div>

        <div class="section">
            <h2>License</h2>
            <p>Copyright 2025 - Murtaza Akbari</p>
        </div>

    </div>

</body>
</html>
