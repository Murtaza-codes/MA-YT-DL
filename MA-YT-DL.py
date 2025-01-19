import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import subprocess
import threading
import re


def choose_file():
    file_path = filedialog.askopenfilename(
        title="Select Cookies File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        cookie_file_var.set(file_path)


def choose_download_location():
    folder_path = filedialog.askdirectory(title="Select Download Location")
    if folder_path:
        download_location_var.set(folder_path)


def is_valid_url(url):
    youtube_pattern = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
    return bool(youtube_pattern.match(url))


def fetch_available_qualities():
    """
    Fetch available formats for the given URL and update the quality list.
    """
    url = url_var.get().strip()
    cookie_file = cookie_file_var.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a video URL.")
        return

    if not is_valid_url(url):
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    if not cookie_file:
        messagebox.showerror("Error", "Please select a cookies file.")
        return

    try:
        command = [
            "yt-dlp",
            "--cookies", cookie_file,
            "--list-formats",
            url
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if stderr:
            messagebox.showerror("Error", f"Error fetching formats:\n{stderr}")
            return

        formats = re.findall(r'(\d{3,4}p)', stdout)  # Extracting qualities like 360p, 720p, etc.
        unique_formats = sorted(set(formats), key=lambda x: int(x.replace("p", "")))

        if not unique_formats:
            messagebox.showerror("Error", "No available qualities found.")
            return

        # Update the quality menu
        quality_menu['menu'].delete(0, 'end')
        for fmt in unique_formats:
            quality_menu['menu'].add_command(label=fmt, command=lambda f=fmt: quality_var.set(f))

        quality_var.set(unique_formats[0])  # Set the default quality to the first available quality
        messagebox.showinfo("Success", "Available qualities fetched successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while fetching formats:\n{e}")


def download_video():
    # Disable the button during the download
    download_button["state"] = DISABLED
    progress_label.config(text="Preparing download...")

    def run_download():
        try:
            url = url_var.get().strip()
            cookie_file = cookie_file_var.get().strip()
            format_choice = format_var.get()
            download_location = download_location_var.get().strip()
            quality = quality_var.get()  # Selected quality
            download_audio = audio_var.get()
            download_subtitles = subtitles_var.get()

            if not url:
                messagebox.showerror("Error", "Please enter a video or playlist URL.")
                return

            if not is_valid_url(url):
                messagebox.showerror("Error", "Please enter a valid YouTube video or playlist URL.")
                return

            if not cookie_file:
                messagebox.showerror("Error", "Please select a cookies file.")
                return

            if not download_location:
                messagebox.showerror("Error", "Please select a download location.")
                return

            # Command for yt-dlp
            command = [
                "yt-dlp",
                "--cookies", cookie_file,
                "-P", download_location,
                url
            ]

            # Add selected quality if available
            if quality:
                command.extend(["-f", f"bestvideo[height={quality.replace('p', '')}]+bestaudio/best"])

            # Set the format to MP4 by default
            command.extend(["--recode-video", "mp4"])

            if download_audio:
                command.extend(["--extract-audio", "--audio-format", "mp3"])

            if download_subtitles:
                command.extend(["--write-subs", "--sub-format", "srt"])

            # Run the command and log output in the terminal
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            for line in process.stdout:
                print(line.strip())  # Print each line to the terminal
                progress_label.config(text=line.strip())  # Show progress in the UI
                root.update_idletasks()

            process.wait()

            if process.returncode == 0:
                messagebox.showinfo("Success", "Download completed successfully!")
            else:
                messagebox.showerror("Error", "An error occurred during the download.")

        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")
        finally:
            progress_label.config(text="")
            download_button["state"] = NORMAL

    # Run download in a separate thread
    threading.Thread(target=run_download).start()


# Initialize ttkbootstrap
root = ttk.Window(themename="vapor")
root.title("yt-dlp Downloader")
root.geometry("700x700")

# Variables
cookie_file_var = ttk.StringVar()
url_var = ttk.StringVar()
format_var = ttk.StringVar(value="MP4")  # Default format is MP4
download_location_var = ttk.StringVar()
quality_var = ttk.StringVar()
audio_var = ttk.BooleanVar()
subtitles_var = ttk.BooleanVar()

# UI Components
url_label = ttk.Label(root, text="Video/Playlist URL:", font=("Arial", 12))
url_label.pack(fill=X, padx=10, pady=5)
url_entry = ttk.Entry(root, textvariable=url_var, font=("Arial", 12))
url_entry.pack(fill=X, padx=10, pady=5)

cookie_label = ttk.Label(root, text="Cookies File:", font=("Arial", 12))
cookie_label.pack(fill=X, padx=10, pady=5)
cookie_frame = ttk.Frame(root)
cookie_frame.pack(fill=X, padx=10, pady=5)
cookie_entry = ttk.Entry(cookie_frame, textvariable=cookie_file_var, font=("Arial", 12))
cookie_entry.pack(side=LEFT, expand=True, fill=X, padx=5)
cookie_button = ttk.Button(cookie_frame, text="Browse", command=choose_file, bootstyle=INFO)
cookie_button.pack(side=RIGHT)

download_label = ttk.Label(root, text="Download Location:", font=("Arial", 12))
download_label.pack(fill=X, padx=10, pady=5)
download_frame = ttk.Frame(root)
download_frame.pack(fill=X, padx=10, pady=5)
download_entry = ttk.Entry(download_frame, textvariable=download_location_var, font=("Arial", 12))
download_entry.pack(side=LEFT, expand=True, fill=X, padx=5)
download_button = ttk.Button(download_frame, text="Browse", command=choose_download_location, bootstyle=INFO)
download_button.pack(side=RIGHT)

quality_label = ttk.Label(root, text="Available Qualities:", font=("Arial", 12))
quality_label.pack(fill=X, padx=10, pady=5)
quality_menu = ttk.OptionMenu(root, quality_var, "")
quality_menu.pack(fill=X, padx=10, pady=5)

fetch_quality_button = ttk.Button(root, text="Fetch Qualities", command=fetch_available_qualities, bootstyle=SUCCESS)
fetch_quality_button.pack(fill=X, padx=10, pady=5)

format_label = ttk.Label(root, text="Select Format:", font=("Arial", 12))
format_label.pack(fill=X, padx=10, pady=5)
format_menu = ttk.OptionMenu(root, format_var, "MP4", "MKV")
format_menu.pack(fill=X, padx=10, pady=5)

audio_check = ttk.Checkbutton(root, text="Download Audio Only (MP3)", variable=audio_var, bootstyle="success")
audio_check.pack(fill=X, padx=10, pady=5)

subtitles_check = ttk.Checkbutton(root, text="Download Subtitles (SRT)", variable=subtitles_var, bootstyle="success")
subtitles_check.pack(fill=X, padx=10, pady=5)

progress_label = ttk.Label(root, text="", font=("Arial", 10))
progress_label.pack(fill=X, padx=10, pady=5)

download_button = ttk.Button(root, text="Download Video/Playlist", command=download_video, bootstyle=PRIMARY)
download_button.pack(fill=X, padx=10, pady=20)

# Run the application
root.mainloop()