# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:36:15 2017

@author: 100419
"""

import facebook

token="EAACEdEose0cBAPPEkAcecNCeZBdQdq6notnLxIoFZC9egE4ZAlZCtm6rr28Bz2VQb7mD1jGH4kHnu7ye72rcKyuN7EgKIuPL0dCLGoWxm5ORsAstqGbEqEJQx3KMDP7ZA2mh10ROuNgOHQ1czLZCOR3gfcie16gTSNPDQnHM8kZB8qhZAZAAI6PhrSzWUQPj41xkZD"
graph=facebook.GraphAPI(access_token=token,version='2.7')
#post=graph.get_object(id='838133046237454_1609690265748391')
#post=graph.get_object(id='838133046237454_1609690265748391?fields=message')
post=graph.get_object(id='838133046237454_1609690265748391?fields=likes')
print(post["id"])
#if'message' in post:
#    print(post["message"])
    #print('訊息:{}' .format(post['message']))
    likes=post['likes']['data']
    print('共有',len(likes),'人按讚')
    for like in likes:
        print(like['name'],end="、")
    
#else:
    #print("缺少message欄位")