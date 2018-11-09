import os
import subprocess
import codecs


file_path = r"F:\study\Multi-length\data\newsCrawler\data_dm_new"


if __name__ == '__main__':
    count = 11 # number of data_dm examples

    # options of ffmpeg
    videoType = "mp4"
    audioType = "mp3"
    ffmpegFormatCode = 'ffmpeg -i {0} -f {1} -vn {2}'

    while True:
        folder_path = file_path + "/" + str(count)

        # whether processing of all examples have done
        if not os.path.exists(folder_path):
            break

        video_path = folder_path + "/video.mp4"
        audio_path = folder_path + "/audio.mp3"

        # whether video exist
        if not os.path.exists(video_path):
            count += 1
            continue

        # whether audio exist
        if os.path.exists(audio_path):
            count += 1
            continue

        command = ffmpegFormatCode.format(video_path, audioType, audio_path)
        #os.popen(command)
        pipe = subprocess.Popen(command, stdout=subprocess.PIPE)
        print(count)
        if count % 4 == 0:
            pipe.wait()

        count += 1
        if count == 12:
            break

