from moviepy.editor import *
import moviepy.editor as mpe

def video_syn(path1,path2,num):
    clip1 = mpe.VideoFileClip(path1)
    clipSize = clip1.size
    clip2 = mpe.VideoFileClip(path2, verbose=True,target_resolution=[clipSize[1], clipSize[0]])
    clips = [clip1, clip2]
    video = clips_array([clips])
    video.write_videofile(fr'D:\Users\Tower\PycharmProjects\pythonProject3\video_syn\{num}.mp4')

for i in range(1,33):
    video_syn(fr'Ours\{i}.mp4', fr'VOCA\{i}.mp4', i)
