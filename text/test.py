import os
import time

badapple_video = open('./badapple_edit.txt', 'r')
badapple_text = badapple_video.read()
badapple_scenes = badapple_text.split("SPLIT")

# print(len(badapple_scenes[0]))
# print(badapple_scenes[0].split('\n'))

'''
edit_video = open('./badapple_edit.txt', 'w')

for badapple_scene in badapple_scenes :
    edit_scenes = badapple_scene.split('\n')
    for i in range(6, len(edit_scenes)-6) :
        if i == 6 :
            edit_scenes[i] = "`\n|" + edit_scenes[i] + "|"    
        elif i == len(edit_scenes) - 7 :
            edit_scenes[i] = "|" + edit_scenes[i] + "|\n`"
        else :
            edit_scenes[i] = "|" + edit_scenes[i] + "|"

    last_num = len(edit_scenes)

    edit_video.write("\n".join(edit_scenes[6:last_num-6]))
    edit_video.write('SPLIT\n')

edit_video.close()
'''

for badapple_scene in badapple_scenes :
    print(badapple_scene)
    time.sleep(0.09)
    os.system('cls')