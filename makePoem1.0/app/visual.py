# -*- coding: utf-8 -*-
# filename: visrecognition.py

import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3


#url = 'http://www.freep.cn/ads/outcalling.aspx?u=http://pic.027cgb.cn/20170409/2017410315623236776.jpg'
#url = "https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg"
def VisualContent(url):
  visualRecognition = VisualRecognitionV3('2016-05-20', api_key='56ddbf9546c752bbb40fb04fa35b15d71c68032e')

  content = visualRecognition.classify(images_url = url)

  images = content.get("images")
  if(images[0].get("error")):
  	return "pic is too large"
  classifiers = images[0].get("classifiers")
  classes = classifiers[0].get("classes")
  res = []
  for i in range(len(classes)):
  	#print(classes[i])
  	res.append(classes[i].get("class"))
  return res
