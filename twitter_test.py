# -*- coding: utf-8 -*-
from time import sleep #timeモジュールの中からsleep関数のみをimportする。
file = open('tweet_list.txt','a') #ファイルを書き込みモードでオープンする。

import twitter
import code #自作ファイル「code」の参照を行わさせる

api = twitter.Api(code.consumer_key,code.consumer_secret,
                  code.access_token_key,code.access_token_secret)

tweet1 = 0
tweet2 = 0

print ("誰のツイートを取得しますか？（IDを入力してください）")
target_name = input('>>>')

infinite =1
while(infinite <= 1):
    user = api.GetUser(screen_name = target_name)
    tweet1 = user.status.created_at
    sleep(10)
    if tweet1 != tweet2:
        file.write(user.status.created_at +"\n\t"+ user.status.text + "\n\n")
        print (user.status.created_at +"\n\t"+ user.status.text + "\n\n")
    tweet2 = tweet1