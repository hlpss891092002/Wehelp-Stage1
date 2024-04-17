import urllib.request as req
import csv
all_data_list=[]
def get_data(url):
  request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
    "Cookie":"over18=1"
  })
  with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
  import bs4
  root=bs4.BeautifulSoup(data, "html.parser")
  article_title=[]
  article_likes=[]
  article_time=[]
  all_list=[]
  def get_titles():
    titles=root.find_all("div", class_="title")
    mark=root.find_all("")
    for title in titles:
      if title.a != None :
        title_string=(title.a.string)
        article_title.append(title_string)
  def get_likes():
    nrecs=root.find_all("div", class_="nrec")
    for nrec in nrecs:
      if nrec.find_next_sibling("div").a==None :
        continue
      elif nrec.span == None:
        article_likes.append("0")
      else:
        like=nrec.span.string
        article_likes.append(like)
  def get_time():
     for title in article_title:
      title_content="https://www.ptt.cc"+root.find("a", string=title)["href"]
      request=req.Request(title_content, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "Cookie":"over18=1"
      })
      with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
      root1=bs4.BeautifulSoup(data, "html.parser")
      time_list = root1.find_all("span", class_="article-meta-value")
      if len(time_list)==0:
        article_time.append("")
      else:
        article_time.append(time_list[3].string)
  def render_all_data():
    i=0
    while i<len(article_likes):
      list=[]
      list.append(article_title[i])
      list.append(article_likes[i])
      list.append(article_time[i])
      str0=",".join(list)
      all_data_list.append(str0)
      i+=1
    # all_data_list.append("完成一頁")
  get_titles()
  get_likes()
  get_time()
  render_all_data()
    
  previousPage=root.find("a", string="‹ 上頁")
  return previousPage["href"]
pageURL="https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:
  pageURL="https://www.ptt.cc"+get_data(pageURL)
  print(f"完成第{count}頁")
  count+=1
with open("article.csv", mode="w", encoding="utf-8",newline="") as csvfile:
  for article in all_data_list:
    csvfile.write(article+"\n")