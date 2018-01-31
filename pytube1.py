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

yt = YouTube("https://www.youtube.com/watch?v=CNfTBlF4RBw&t=155s")
#stream = yt.streams.filter(file_extension ='mp4', res ='360p')
#stream = yt.streams.first()
#stream.download("c:\\SPB_Data\\temp")

stream = yt.streams.filter(file_extension ='mp4', res ='720p').all()
print(stream)
stream[0].download("C:\\Anaconda3\\temp")




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