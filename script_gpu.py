# Set path to use custom ffmpeg binary
import os
os.environ["FFMPEG_BINARY"] = "/usr/local/bin/ffmpeg"

from moviepy import VideoFileClip, ImageClip, concatenate_videoclips
from moviepy.video.fx import FadeIn, FadeOut

try:
    # Load the video files
    print("Loading video files...")
    clip1 = VideoFileClip("1.MP4").subclipped(0, 2)  # Clip 1: First 2 seconds
    clip2 = VideoFileClip("2.MP4").subclipped(0, 5)  # Clip 2: First 5 seconds
    clip3 = VideoFileClip("3.MP4").subclipped(0, 5)  # Clip 3: First 5 seconds

    # Apply fade-out effect to clip1
    clip1 = FadeOut(duration=0.5).apply(clip1)  # Fade out over 0.5 seconds

    # Apply fade-in and fade-out effects to clip2
    clip2 = FadeIn(duration=0.5).apply(clip2)  # Fade in over 0.5 seconds
    clip2 = FadeOut(duration=1).apply(clip2)  # Fade out over 1 second

    # Apply fade-in effect to clip3
    clip3 = FadeIn(duration=1).apply(clip3)  # Fade in over 1 second

    # Load the PNG image and set its duration
    print("Loading image file...")
    image = ImageClip("1.png", duration=3)  # Show image for 3 seconds
    # image = image.with_audio(clip1.audio.set_duration(image.duration))
    image = FadeIn(duration=1).apply(image)  # Add fade-in to the image
    image = FadeOut(duration=1).apply(image)  # Add fade-out to the image

    # Concatenate the video and image clips with transitions
    print("Concatenating video clips and image with transitions...")
    final_clip = concatenate_videoclips([clip1, image, clip2, clip3], method="compose")

    # Write the final output video with NVIDIA CUDA hardware acceleration
    print("Writing the final video to 'output_with_fades_gpu.mp4' using CUDA hardware acceleration...")
    
    final_clip.write_videofile(
        "output_with_fades_gpu.mp4",
        codec="h264_nvenc",  # NVIDIA NVENC encoder
        preset="fast",  # Adjust for speed vs. quality
        #ffmpeg_params=[
        #    "-c:v", "h264_nvenc",    # Use NVIDIA's CUVID decoder for H.264 video
        #    "-pix_fmt", "yuv420p"    # Ensure compatibility for playback
        #],
        audio_codec="aac",  # Use AAC for audio encoding
	    threads=32,
        logger=None,
        fps=60,
    )

    print("Video processing completed successfully! The output is saved as 'output_with_fades.mp4'.")

except Exception as e:
    print(f"An error occurred: {e}")
