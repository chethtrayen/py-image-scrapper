import re

class Image:
  def addSrc(self, src) -> None:
    self.src = src

  def __addProtocol(self) -> str:
    tempSrc = self.src
    if(re.search("^https", tempSrc) is None):
      tempSrc = 'https:'+ tempSrc
    return tempSrc
      
  def serializeSrc(self) -> str:
      src = self.__addProtocol()
      return src

def getImageSources(images) :
  sources = []
  for img in images: 
    image = Image()
    try: 
      image.addSrc(img['src'])
    except:
      image.addSrc(img['data-src'])
    sources.append(image.serializeSrc())
  return sources