import os
import sys
from moviepy.editor import VideoFileClip

def trim_audio_moviepy(video_file, start_time, end_time, output_ext="mp3"):
    # xtracts and trims audio from a video file using MoviePy.
    # start_time and end_time are in seconds
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)

    # Validate time range
    if start_time < 0 or end_time > clip.duration or start_time >= end_time:
        print(f"Invalid time range. Video duration is {clip.duration:.2f} seconds.")
        clip.close()
        return

    trimmed = clip.audio.subclip(start_time, end_time)
    output_file = f"{filename}_trimmed_{int(start_time)}s_to_{int(end_time)}s.{output_ext}"
    trimmed.write_audiofile(output_file)
    print(f"Done! Saved as: {output_file}")
    clip.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 audio_trimmer.py <video_file> <start_seconds> <end_seconds>")
        print("Example: python3 audio_trimmer.py zoo.webm 0 10")
        sys.exit(1)

    vf = sys.argv[1]
    start = float(sys.argv[2])
    end = float(sys.argv[3])

    trim_audio_moviepy(vf, start, end)
