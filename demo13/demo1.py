# 原生爬虫
from urllib import request
import re
class Spider():
  url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.45k14n9nsbm'
  # video-info 中的所有内容 ()组要匹配video-info中间的内容
  pattern = '<div class="video-info">([\s\S]*?)</div>'
  pattern_title = '<div class="video-title">([\s\S]*?)</div>'
  pattern_nickname = '<div class="video-nickname" title="[\s\S]*?">([\s]*?)</div>'
  pattern_number = '<div class="video-number">([\s]*?)</div>'
  pattern_num = '<div class="video-station-info"><i class="video-station-num">([\s\S]*?)</i></div>'
  def __get_data(self):
    data = request.urlopen(self.url)
    html = data.read()
    html_str = str(html, encoding='utf-8')
    return html_str
  def start(self):
    htmlstr = self.__get_data()
    self.analysis(htmlstr)
  def analysis(self, html):
    html_all = re.findall(self.pattern, html)
    data_list = []

    for html in html_all:
      name = re.findall(self.pattern_nickname, html)
      title = re.findall(self.pattern_title, html)
      number = re.findall(self.pattern_number, html)
      num = re.findall(self.pattern_num, html)
      all_data = {
        "name":name,
        "title":title,
        "number":number,
        "num":num
      }
      data_list.append(all_data)
    print(data_list)


spider = Spider()
spider.start()
