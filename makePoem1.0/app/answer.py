import visual, translate, poem
import os

def Answer(url):
  #url="http://img.au-syd.mybluemix.net/_uploads/photos/aab0f8d252e6489.jpg"
  tags = ["海","湖","树","花","天","云","山","路"]
  test = translate.Translate(visual.VisualContent(url))
  res = poem.Poem(tags,test)
  return res
'''
dirr = "D:/test/"
pathDir = os.listdir(dirr)
for cont in pathDir:
  item = os.path.join('%s%s' % (dirr,cont))
  print(item + "\n")
  url = open(item,'rb')
  print(Answer(url))
'''
url = "http://47.93.229.184/photos/357a67c1f2acfa3.jpg"
print(Answer(url))