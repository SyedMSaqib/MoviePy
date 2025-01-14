from moviepy import VideoFileClip, ImageClip, concatenate_videoclips
from moviepy.video.fx import FadeIn, FadeOut
import time

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
    output_file_name = f"output_with_fades_{int(time.time() * 1000_000_0)}.mp4"
    print("Writing the final video to 'output_with_fades.mp4'...")

    final_clip.write_videofile(
        output_file_name,
        codec="libx264",  # Standard H.264 encoder (software-based)
        preset="fast",  # Adjust for speed vs. quality
        audio_codec="aac",  # Use AAC for audio encoding
	    threads=32,
    )

    print("Video processing completed successfully! The output is saved as 'output_with_fades.mp4'.")

except Exception as e:
    print(f"An error occurred: {e}")