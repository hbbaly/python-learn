# 原生爬虫
from urllib import request
import re
class Spider():
  url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.45k14n9nsbm'
  # video-info 中的所有内容 ()组要匹配video-info中间的内容
  pattern = '<div class="video-info">([\s\S]*?)</div>'
  pattern_title = '<span class="video-title" title="([\s\S]*?)">([\s\S]*?)</span>'
  pattern_nickname = '<span class="video-nickname" title="([\s\S]*?)">'
  pattern_number = '<span class="video-number"><i class="ricon ricon-eye"></i>([\s\S]*?)</span>'
  pattern_num = '<i class="video-station-num">([\s\S]*?)</i>'
  def __get_data(self):
    data = request.urlopen(self.url)
    html = data.read()
    html_str = str(html, encoding='utf-8')
    return html_str
  def start(self):
    htmlstr = self.__get_data()
    htmlstr = self.analysis(htmlstr)
    htmlstr = self.__sorted(htmlstr)
    self.__print(htmlstr)
    # print(htmlstr['name']+'-----------'+htmlstr['number'])

  def __sorted(self, anchor):
    anchor = sorted(anchor, key=self.__sorted__seed, reverse=True)
    return anchor

  def __sorted__seed(self, anchor):
    r = re.findall('\d*',anchor['number'])
    r = float(r[0])
    if '万' in anchor['number']:
      r *=10000
    return r
  def __print(self, anchors):
    for rank in range(0, len(anchors)):
      print('rank'+':'+str(rank+1)+'---------'+anchors[rank]['name']+'------'+anchors[rank]['number'])

  def analysis(self, html):
    html_all = re.findall(self.pattern, html)
    data_list = []
  
    for html in html_all:
      name = re.findall(self.pattern_nickname, html)[0]
      title = re.findall(self.pattern_title, html)[0][1]
      number = re.findall(self.pattern_number, html)[0]
      num = re.findall(self.pattern_num, html)[0]
      all_data = {
        "name":name,
        "title":title,
        "number":number,
        "num":num
      }
      data_list.append(all_data)
    return data_list


spider = Spider()
spider.start()
