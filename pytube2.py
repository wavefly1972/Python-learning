# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:05:20 2017

@author: 100419
"""


from pytube import YouTube
'''
yt=YouTube("https://www.youtube.com/watch?v=27ob2G3GUCQ")
#yt=YouTube()
yt.url="https://www.youtube.com/watch?v=27ob2G3GUCQ"
video=yt.get("mp4","360p")

video.download("c:\\SPB_Data\\temp")
'''

# http://www.e-happy.com.tw/indexforum.asp?bid=17370
# http://python-pytube.readthedocs.io/en/latest/user/quickstart.html#downloading-a-video

yt = YouTube("https://www.youtube.com/watch?v=2_3yue-NVoI&t=9s")
#stream = yt.streams.filter(file_extension ='mp4', res ='360p')
#stream = yt.streams.first()
#stream.download("c:\\SPB_Data\\temp")
print("影片原始檔名:"+ yt.title)  
print("所有影片相關串流:") 
print(yt.streams.all())  #打印所有Stream名稱
#yt.streams.set_title("小魔術1")
#formatlist=yt.get_videos()
#allformat=str(formatlist)
stream = yt.streams.filter(file_extension ='mp4', res ='360p').all()
print("目前下載的串流：" ,stream)
stream[0].download("c:\\Anaconda3\\temp")




#yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')
#yt = YouTube('https://www.youtube.com/watch?v=RwR1uif_uDg')
#yt = YouTube('https://www.youtube.com/watch?v=27ob2G3GUCQ')
#yt.set_filename("小魔術1")
#print(yt.title)
#print(yt.streams.all())
#stream = yt.streams.first()
#stream=yt.streams.filter(file_extension='mp4').all()
#stream.download("c:\\SPB_Data\\temp")
#stream.download()