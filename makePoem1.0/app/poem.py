# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random
import visual, translate
import os

'''
检测图片的标签
'''
def IsTag(tags,test):
  flag = 0
  resTag = []
  for tag in tags:
    for word in test:
      l = len(word)
      for i in range(l):
        if(word[i] == tag):
          resTag.append(tag)
          flag = 1
  if(flag == 0):
    return False
  else:
    return resTag

'''
未标签诗句
'''
def ElsePoem():
  felse = pd.DataFrame(pd.read_excel("else.xls"))
  cnt = felse["诗"].count()
  num = random.randint(1,cnt-1)
  poem = str(felse["诗"][num:num+1]).split()[1]
  return poem

#print(ElsePoem())
def Poem(tags,test):
  tag = IsTag(tags,test)
  f = pd.DataFrame(pd.read_excel("season.xls"))
  if(tag == False):
  	global poem
  	poem = ElsePoem()
  else:
    tagCnt = len(tag)
    global poemCnt,condition
    poemCnt = 0
    if(tagCnt == 1):
      condition = f.loc[(f[tag[0]]==1)]["诗"]
      poemCnt = f.loc[(f[tag[0]]==1)]["诗"].count()
    if(tagCnt == 2):
      condition = f.loc[(f[tag[0]]==1)&(f[tag[1]]==1)]["诗"]
      poemCnt = f.loc[(f[tag[0]]==1)&(f[tag[1]]==1)]["诗"].count()
    if(tagCnt == 3):
      condition = f.loc[(f[tag[0]]==1)&(f[tag[1]]==1)&(f[tag[2]]==1)]["诗"]
      poemCnt = f.loc[(f[tag[0]]==1)&(f[tag[1]]==1)&(f[tag[2]]==1)]["诗"].count() 
    if(tagCnt == 4):
      condition = f.loc[(f[tag[0]]==1)&(f[tag[1]]==1)&(f[tag[2]]==1)&(f[tag[3]]==1)]["诗"]
      poemCnt = f.loc[(f[tag[0]]==1)&(f[tag[1]]==1)&(f[tag[2]]==1)&(f[tag[3]]==1)]["诗"].count()
    if(poemCnt == 0):
      condition = f.loc[(f[tag[0]]==1)]["诗"]
      poemCnt = f.loc[(f[tag[0]]==1)]["诗"].count()

    num = random.randint(0,poemCnt-1)
    poem = str(condition[num:num+1]).split()[1]
  return poem

'''
if __name__ == "__main__":
  tags = ["海","湖","树","花","天","云","山","路"]
  dirr = "D:/test/"
  pathDir = os.listdir(dirr)
  for cont in pathDir:
    item = os.path.join('%s%s' % (dirr,cont))
    print(item + "\n")
    url = open(item,'rb')
    test = translate.Translate(visual.VisualContent(url))
    print(Poem(tags,test))
'''

