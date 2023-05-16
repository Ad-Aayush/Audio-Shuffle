# Python code to convert video to audio
import moviepy.editor as mp
import os

files = os.listdir(".")
# tmp = tmp.split('\n')
for f in files:
    if f[-1] != "4":
        files.remove(f)
print(files)

# Insert Local Video File Path
for f in files:
    if files.index(f) == 0:
        clip = mp.VideoFileClip(f)
        rate = clip.fps
        print("FPS : " + str(rate))
        clip.audio.write_audiofile(str(files.index(f)) + ".mp3")
