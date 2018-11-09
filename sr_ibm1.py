import requests
import codecs
import os

headers = {
    'Content-Type': 'audio/mp3',
}

count = 4412 # number of examples
while count < 5000:
    folder_path = r"F:\study\Multi-length\data\newsCrawler\data_dm_new"
    file_path = folder_path + "/" + str(count)

    # check existence of video
    if not os.path.exists(file_path + "/audio.mp3"):
        count += 1
        continue

    data = open(file_path + "/audio.mp3", 'rb').read()
    response = requests.post('https://stream.watsonplatform.net/speech-to-text/api/v1/recognize', headers=headers,
                             data=data, auth=('6fa99fad-71af-4112-a74f-08bd813d5cf8', 'm8rOb6bzvkot'))
    dic = response.json()
    # check results
    if 'error' in dic:
        count += 1
        continue
    results = dic['results']

    file = codecs.open(file_path + "/transcript.txt", 'a')
    for result in results:
        alternatives_dict = result['alternatives']
        confidence = alternatives_dict[0]['confidence']
        transcript = alternatives_dict[0]['transcript']
        file.write(str(confidence)+"\n")
        file.write(str(transcript)+"\n")

    file.close()
    print("Finish extraction in ", count)
    count += 1
