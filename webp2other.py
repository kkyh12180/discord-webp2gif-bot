import os
from PIL import Image, ImageSequence

def webp2gif(path) :
    file_name = os.path.basename(path).split(".")[0]
    im = Image.open(path)
    im.info.pop('background', None)
    im.save(f'./image/tmp/{file_name}.gif', 'gif', save_all=True)
    im.close()

def webp2png(path) :
    file_name = os.path.basename(path).split(".")[0]
    im = Image.open(path)
    im.save(f'./image/tmp/{file_name}.png', 'png')
    im.close()

def is_move(path) :
    try :
        im = Image.open(path)
        index = 0
        for frame in ImageSequence.Iterator(im) :
            index += 1
        if index > 1 : 
            im.close()
            return True
        else :
            im.close()
            return False
    except :
        print("Except")
        return False

def main() :
    img_path = "./image/webpgif.webp"
    if is_move(img_path) :
        webp2gif(img_path)
    else :
        webp2png(img_path)

if __name__ == "__main__" :
    main()