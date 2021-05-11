# Keunwoo Choi
# This example crawl snoring sound by searching keyword 'snore'.

# Edited HanGyu Kim 2021-05-11
from __future__ import print_function
import freesound # $ git clone https://github.com/MTG/freesound-python
import os
import sys

api_key = 'aW0HJYBYbzWt49eScPXM3fDlBmsNlICuZYNKuzar'
#folder = 'data_freesound/' # folder to save
selection = "crying"
folder = "./sound_dataset/" +selection+ "/"

freesound_client = freesound.FreesoundClient()
freesound_client.set_token(api_key)

try:
    os.mkdir(folder)
except:
    pass


# Search Example
print("Searching for : "+ selection)
print("----------------------------")

results_pager = freesound_client.text_search(
    query=selection,
    # filter="tag:tenuto duration:[1.0 TO 15.0]",
    sort="rating_desc",
    fields="id,name,previews,username"
)
print("Num results:", results_pager.count)
print("\t----- PAGE 1 -----")
for sound in results_pager:
    print("\t-", sound.name, "by", sound.username)
    filename = str(sound.id) + '_' + sound.name.replace(u'/', '_')+".mp3"
    try:
        if not os.path.exists(folder + filename):
            sound.retrieve_preview(folder, filename)
    except:
        pass
print()
for page_idx in range(int(results_pager.count/15)):
    print("\t----- PAGE {} -----".format(page_idx+2))
    #next_page = int(page_idx) + int(2)
    try:
        results_pager = results_pager.next_page()
        for sound in results_pager:
            print("\t-", sound.name, "by", sound.username)
            filename = str(sound.id) + '_' + sound.name.replace(u'/', '_')+".mp3"
            if not os.path.exists(folder + filename):
                sound.retrieve_preview(folder, filename)
    except:
        pass    
    print()
print("End!!!!!!!!!!!!!!!!!!!!")
