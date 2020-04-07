from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url='https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup= soup(page_html,"html.parser")

containers = page_soup.findAll("div" , {"class" : "_3liAhj"})
#print(len(containers))

#print(soup.prettify(containers[0]))
container=containers[0]
#print(container.div.img["alt"])

price=container.findAll("div",{"class" : "_1uv9Cb"})
#print(price[0].text)

ratings=container.findAll("div",{"class" : "niH0FQ _36Fcw_"})
#print(rating[0].text)

filename= "webscraper001.csv"
f=open(filename,"w")

headers="Name,Price,Rating\n"
f.write(headers)

for container in containers:
    pr_name=container.div.img["alt"]

    p_container=container.findAll("div",{"class" : "_1uv9Cb"})
    p_price = p_container[0].text.strip()

    r_container=container.findAll("div",{"class" : "niH0FQ _36Fcw_"})
    p_rating=r_container[0].text

    #print("p_name:" + pr_name)
    #print("p_price:"+p_price)
    #print("p_rating:"+p_rating)

    trim_p_price = ''.join(p_price.split(','))
    rm_rupee=trim_p_price.split("₹")
    add_rs_p_price="Rs." + rm_rupee[1]
    split_p_price=add_rs_p_price.split('E')
    final_price=split_p_price[0]

    split_p_rating=p_rating.split(" ")
    final_rating=split_p_rating[0]

    print(pr_name.replace(",","|")+","+final_price+","+final_rating+"\n")
    f.write(pr_name.replace(",","|")+","+final_price+","+final_rating+"\n")

f.close()


