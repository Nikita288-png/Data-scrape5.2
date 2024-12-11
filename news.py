import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

newsUrl='https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'
newsHeader={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "if-none-match": "W/\"3801c-TitY76GKnYBjmFKdyaQvnOF9FsM\"",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "FTAllocation=f9d093b7-ca6f-49aa-8174-f6ea95c5be63; FTClientSessionId=6a71b80b-0199-4183-a399-6ac83b247188; spoor-id=be0dd413-8305-41b0-9f42-15e09e21e6ce; o-typography-fonts-loaded=1; usnatUUID=a52f91ff-37cf-439f-911f-3cae79a5e609; __exponea_etc__=36df5d1d-4c66-49cf-b6af-39c25328de25; __exponea_time2__=-85.73274660110474; consentUUID=49c4f56a-5b7c-4813-9301-3753ab997ace_38; consentDate=2024-12-11T08:51:37.158Z; FTConsent=marketingBypost%3Aoff%2CmarketingByemail%3Aoff%2CmarketingByphonecall%3Aoff%2CmarketingByfax%3Aoff%2CmarketingBysms%3Aoff%2CenhancementBypost%3Aoff%2CenhancementByemail%3Aoff%2CenhancementByphonecall%3Aoff%2CenhancementByfax%3Aoff%2CenhancementBysms%3Aoff%2CbehaviouraladsOnsite%3Aoff%2CdemographicadsOnsite%3Aon%2CrecommendedcontentOnsite%3Aon%2CprogrammaticadsOnsite%3Aon%2CcookiesUseraccept%3Aoff%2CcookiesOnsite%3Aoff%2CmembergetmemberByemail%3Aoff%2CpermutiveadsOnsite%3Aoff%2CpersonalisedmarketingOnsite%3Aon; FTCookieConsentGDPR=true; _cb=CFVA7_CjERNNCMQftn; _cb_svref=https%3A%2F%2Fwww.ft.com%2Ftechnology; _t_tests=eyJWVW5GUmxtVVVVWW8xIjp7ImNob3NlblZhcmlhbnQiOiJCIiwic3BlY2lmaWNMb2NhdGlvbiI6WyJDWDlLbXkiXX0sImxpZnRfZXhwIjoibSJ9; _chartbeat2=.1733923850439.1733923865456.1.D8p96CDB3CazDYm8TqDgsAwWDdcUXA.4; ft-access-decision-policy=DENIED_ZEPHR_ALLOTHERTRAFFIC_0_0",
    "Referer": "https://www.ft.com/technology",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }
newsResp=rq.get(url=newsUrl,headers=newsHeader)

newSoup=BeautifulSoup(newsResp.content,'html.parser')

allNews=newSoup.select('div[class="o-teaser-collection o-teaser-collection--stream"]>ul>li')

allnewdata=[]
for n in allNews:
    date=n.select_one('div[class="stream-card_date"]>time')
    if date:
        date=date=date.attrs['datetime']
        
    images=n.select_one('div [class="o-teaser_image-container js-teaser-image-container"]>img')
    if images:
        images={'src':images.attrs['src'],
                'alt':images.attrs['alt']}
        
    headlines=n.select_one('div[class="o-teaser_heading"]>a')
    if headlines:
            headlines=headlines.text

    newsdata={'date':date,
              'headlines':headlines,
              'images':images}
    allnewdata.append(newsdata)

    newsdata=pd.DataFrame(allnewdata)
    newsdata.to_csv('newsdata.csv')


        
    
