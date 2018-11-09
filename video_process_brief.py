import os
import fnmatch
from optparse import OptionParser

file_path = r"F:\study\Multi-length\data\newsCrawler\data_dm_new"
parser = OptionParser()
parser.add_option("-s", "--src", dest="src", action="store", help="source dir", default=file_path)
parser.add_option("-d", "--dest", dest="dest", action="store", help="destination dir", default=file_path)
parser.add_option("-v", "--video-type", dest="videoType", action="store", help="input video type", default="mp4")
parser.add_option("-a", "--audio-type", dest="audioType", action="store", help="output audio type", default="mp3")


def filter_file(path, file_ext):
    flist = os.listdir(path)
    all_file = []
    for filename in flist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            all_file.extend(filter_file(filepath, file_ext))
        elif fnmatch.fnmatch(filepath, '*.' + file_ext):
            all_file.append(filepath)
        else:
            pass
    return all_file


if __name__ == '__main__':
    (options, args) = parser.parse_args()
    src = options.src
    dest = options.dest
    videoType = options.videoType
    audioType = options.audioType
    all_file = filter_file(src, videoType)
    if not os.path.exists(dest):
        os.mkdir(dest)
    ffmpegFormatCode = 'ffmpeg -i {0} -f {1} -vn {2}'

    for f in all_file:
        vFilename = os.path.split(f)[-1]
        aFilename = vFilename.split('.')[0] + '.' + audioType
        vFullFilename = os.path.join(src, vFilename)
        aFullFilename = os.path.join(dest, aFilename)
        print("Start converting {0}".format(vFilename))

        tmp = ffmpegFormatCode.format(vFullFilename, audioType, aFullFilename)
        print(tmp)

        # os.system(tmp)
        os.system(tmp)
        print("Finish conversion of {0}".format(aFilename))