import os
import subprocess

def get_video_size(video_path):
    cmd = [
        "ffprobe", 
        "-v", "error", 
        "-select_streams", "v:0", 
        "-show_entries", "stream=width,height", 
        "-of", "csv=s=x:p=0", 
        video_path
    ]
    output = subprocess.check_output(cmd).decode("utf-8").strip()
    width, height = map(int, output.split('x'))
    return width, height

def resize_videos(video_folder, reference_video):
    ref_width, ref_height = get_video_size(reference_video)
    output_folder = os.path.join(video_folder, "resized")
    os.makedirs(output_folder, exist_ok=True)

    for video_file in os.listdir(video_folder):
        if video_file.endswith((".mp4", ".avi", ".mkv")):
            input_path = os.path.join(video_folder, video_file)
            output_path = os.path.join(output_folder, video_file)
            cmd = [
                "ffmpeg", 
                "-i", input_path, 
                "-vf", f"scale={ref_width}:{ref_height}", 
                output_path
            ]
            subprocess.run(cmd)
            print(f"Resized {video_file} to {ref_width}x{ref_height}")

if __name__ == "__main__":
    video_folder = "/Users/czsmacbook/Desktop/html/video2"
    reference_video = "/Users/czsmacbook/Desktop/html/video/leave1.mp4"
    resize_videos(video_folder, reference_video)
