# Lets import moviepy, lets also import numpy we will use it a some point
from moviepy import *
import numpy as np


#################
# VIDEO LOADING #
#################
# We load our video
Qr_clip = VideoFileClip("Qr.MP4").subclipped(0, 2)  # Clip 1: First 2 seconds
Interview_clip = VideoFileClip("Interview.MP4").subclipped(
    0, 5
)  # Clip 2: First 5 seconds
Boarding_clip = VideoFileClip("Boarding.MP4").subclipped(
    0, 5
)  # Clip 3: First 5 seconds

Diving_clip = VideoFileClip("Diving.mp4").subclipped(30, 40)

Tandem_clip = VideoFileClip("Tandem.mp4").subclipped(25, 73)

End_clip = VideoFileClip("Diving.mp4").subclipped(42, 48)

Audio_clip = AudioFileClip("audio.wav")

intro_text = TextClip(
    text="Go Jump America presents",
    font="Gilroy-Medium.ttf",
    font_size=50,
    color="#fff",
    text_align="center",
    size=(1280, 100),
)
Qr_text = TextClip(
    text="Scan the QR code",
    font="Gilroy-Medium.ttf",
    font_size=50,
    color="#fff",
    text_align="center",
    size=(1280, 100),
)
Interview_text = TextClip(
    text="Interview with Sebastian Martinez",
    font="Gilroy-Medium.ttf",
    font_size=50,
    color="#fff",
    text_align="center",
    size=(1280, 100),
)

Boarding_text = TextClip(
    text="Boarding the plane",
    font_size=50,
    font="Gilroy-Medium.ttf",
    color="#fff",
    text_align="center",
    size=(1280, 100),
)
Diving_text = TextClip(
    text="Taking the Leap of a Lifetime!",
    font_size=50,
    font="Gilroy-Medium.ttf",
    color="#fff",
    text_align="center",
    size=(1280, 100),
)

logo_clip = ImageClip("1.png").resized(width=400)
moviepy_clip = ImageClip("1.png").resized(width=300)

intro_text = intro_text.with_duration(4).with_start(0)
logo_clip = logo_clip.with_start(intro_text.start + 2).with_end(intro_text.end)

Qr_clip = Qr_clip.with_start(logo_clip.end)
Qr_text = Qr_text.with_start(Qr_clip.start).with_end(Qr_clip.end)

Interview_clip = Interview_clip.with_start(Qr_clip.end)
Interview_text = Interview_text.with_start(Interview_clip.start).with_end(
    Interview_clip.end
)

Boarding_clip = Boarding_clip.with_start(Interview_clip.end)
Boarding_text = Boarding_text.with_start(Boarding_clip.start).with_end(
    Boarding_clip.end
)

# Diving_clip = Diving_clip.with_start(Boarding_clip.end)

Tandem_clip = Tandem_clip.with_start(Boarding_clip.end)
Diving_text = Diving_text.with_start(Tandem_clip.start).with_end(Tandem_clip.start + 4)
End_clip = End_clip.with_start(Tandem_clip.end)

Audio_clip = Audio_clip.with_start(Diving_clip.start).with_end(End_clip.end)


######################
# CLIPS POSITIONNING #
######################
# Now that we have set the timing of our different clips, we need to make sure they are in the right position
# We will keep things simple, and almost always set center center for every texts

intro_text = intro_text.with_position(("center", "center"))
Qr_text = Qr_text.with_position(("center", "center"))
Interview_text = Interview_text.with_position(("center", "center"))
Boarding_text = Boarding_text.with_position(("center", "center"))
Diving_text = Diving_text.with_position(("center", "center"))


intro_text = intro_text.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])
logo_clip = logo_clip.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])

Qr_text = Qr_text.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])
Qr_clip = Qr_clip.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])

Interview_text = Interview_text.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])
Interview_clip = Interview_clip.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])

Diving_text = Diving_text.with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(1)])
Diving_clip = Diving_clip.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])

Tandem_clip = Tandem_clip.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])

End_clip = End_clip.with_effects([vfx.CrossFadeIn(2), vfx.CrossFadeOut(2)])

###############
# CLIP FILTER #
###############
# Lets finish by modifying our rambo clip to make it sepia


# We will start by defining a function that turn a numpy image into sepia
# It takes the image as numpy array in entry and return the modified image as output
def sepia_filter(frame: np.ndarray):
    # Sepia filter transformation matrix
    # Sepia transform works by applying to each pixel of the image the following rules
    # res_R = (R * .393) + (G *.769) + (B * .189)
    # res_G = (R * .349) + (G *.686) + (B * .168)
    # res_B = (R * .272) + (G *.534) + (B * .131)
    #
    # With numpy we can do that very efficiently by multiplying the image matrix by a transformation matrix
    sepia_matrix = np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    )

    # Convert the image to float32 format for matrix multiplication
    frame = frame.astype(np.float32)

    # Apply the sepia transformation
    # .T is needed because multiplying matrix of shape (n,m) * (m,k) result in a matrix of shape (n,k)
    # what we want is (n,m), so we must transpose matrix (m,k) to (k,m)
    sepia_image = np.dot(frame, sepia_matrix.T)

    # Because final result can be > 255, we limit the result to range [0, 255]
    sepia_image = np.clip(sepia_image, 0, 255)

    # Convert the image back to uint8 format, because we need integer not float
    sepia_image = sepia_image.astype(np.uint8)

    return sepia_image


Qr_clip = Qr_clip.image_transform(sepia_filter)

# Diving_clip = Diving_clip.without_audio()
Tandem_clip = Tandem_clip.without_audio()
End_clip = End_clip.without_audio()

# Calculate the durations of the muted clips
diving_duration = Diving_clip.duration
tandem_duration = Tandem_clip.duration
end_duration = End_clip.duration

# Calculate when Tandem clip starts relative to the overall video
tandem_start_time = (
    Boarding_clip.end
)  # This is when Tandem clip starts in the final video

# Get the audio segments starting from when Tandem clip begins
tandem_audio = Audio_clip.subclipped(0, Tandem_clip.duration).with_start(
    tandem_start_time
)
end_audio = Audio_clip.subclipped(
    Tandem_clip.duration, Tandem_clip.duration + End_clip.duration
).with_start(Tandem_clip.end)

# Attach the trimmed audio to the muted clips
Tandem_clip = Tandem_clip.with_audio(tandem_audio)
End_clip = End_clip.with_audio(end_audio)


final_clip = CompositeVideoClip(
    [
        intro_text,
        logo_clip,
        Qr_clip,
        Qr_text,
        Interview_clip,
        Interview_text,
        Boarding_clip,
        Boarding_text,
        # Diving_clip,
        Diving_text,
        Tandem_clip,
        End_clip,
    ],
    size=(1280, 720),
)

final_clip.preview(fps=10)


final_clip.write_videofile("./result.mp4")
