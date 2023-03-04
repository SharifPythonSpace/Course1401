news1 = 'this'
news2 = "it is the seconde news"
news3 = "that is the third news!"


our_yellow_news = [news1, news2, news3]

for news in our_yellow_news:
    if len(news)<5:
        print(news)
    else:
        print('nothing')