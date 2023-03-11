news1 = "Rishi Sunak is facing criticism that his proposed laws on small boat crossings will be unworkable and lead to tens of thousands of people fleeing war and persecution being locked up."
news2 = "A Whitehall source briefed on the plan confirmed that even children could be detained with their families, as the government seeks to stop an estimated 60,000 people a year from making the perilous journey from mainland Europe."
news3 = "Previous plans to deport those entering the UK by small boat to Rwanda have been rejected by the courts, but No 10 and the Home Office are proposing to insert a “brake” on human rights legislation in an attempt to stop legal challenges."


number_of_like_for_news1 = 20
number_of_like_for_news2 = 100
number_of_like_for_news3 = 1

news_list = [news1, news2, news3]
likes_list = [number_of_like_for_news1, 
            number_of_like_for_news2,
            number_of_like_for_news3]

interested_news_list = []

# range(4) = [0, 1, 2, 3]
for index in range(len(news_list)):
    if likes_list[index] > 15:
        interested_news_list.append(news_list[index])

for news in interested_news_list:
    print(news)

def Freq_words(interested_news):
    word_list = ' '.join(interested_news).split(' ')
    count_list = []
    for word in word_list:
        for news in interested_news:
            count_list.append(news.count(word))
