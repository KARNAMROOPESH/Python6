import cv2
import dropbox
import time
import random

starttime = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videocapture = cv2.VideoCapture(1)
    result = True
    while result:
        ret,frame=videocapture.read()
        print(ret)
        imgname = "newpic"+ str(number) +".png"
        cv2.imwrite(imgname,frame)
        result = False
    return imgname
    videocapture.release()
    cv2.destroyAllWindows()
    

def upload(img):
     token='sl.AuYUpbsrc_1jUN1lz0AyL466xTW5ZWqtHcbacOO2sDgJfBE48PnEquLQ-xo8aL1mtvivTS0Wu-Cm8tFTI5rTZVTaRG0mM2XtteVsXpR1CoEy8N1meIeYV3Y4zTLY5Poq5ceUcTFlpHI'
     frm = img
     to = "/pictures"+(img)
     dbx = dropbox.Dropbox(token)
     with open(frm , 'rb')as p:
         dbx.files_upload(p.read(), to , mode=dropbox.files.WriteMode.overwrite)
         print("imguploaded")


def main():
    while True :
        if(time.time()- starttime > 10):
          img = take_snapshot()
          upload(img)
    
main()