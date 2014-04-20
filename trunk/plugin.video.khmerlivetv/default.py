import httplib
import urllib,urllib2,re,sys
import cookielib,os,string,cookielib,StringIO,gzip
import os,time,base64,logging
from t0mm0.common.net import Net
import xml.dom.minidom
import xbmcaddon,xbmcplugin,xbmcgui
try: import simplejson as json
except ImportError: import json
import cgi
import CommonFunctions
common = CommonFunctions
common.plugin = "plugin.video.khmerlivetv"
strDomain ='http://www.khmerlive.tv/'
strdomainn='rtmp://'
def HOME():
        addDir('News','http://www.khmerlive.tv/archive/?c=2',2,'')
        addDir('Politics','http://www.khmerlive.tv/archive/?c=1',2,'')		
        addDir('Entertainment & Music','http://www.khmerlive.tv/archive/?c=4',2,'')
        addDir('Game','http://www.khmerlive.tv/archive/?c=7',2,'')
        addDir('Life Style','http://www.khmerlive.tv/archive/?c=6',2,'')
        addDir('Sport','http://www.khmerlive.tv/archive/?c=3',2,'')		
        addDir('Khmer Boxing','http://www.khmerlive.tv/archive/?q=Khmer+Boxing',2,'http://www.khmernz.com/xbmc/khmer2all/kboxing.png')				
        addDir('Hun Sen','http://www.khmerlive.tv/archive/?q=Hun+Sen',2,'http://www.khmernz.com/xbmc/khmer2all/hunsen.jpg')
        addDir('Cha Cha Cha Game Show','http://www.khmerlive.tv/archive/?q=Cha+Cha+Cha+Game+Show',2,'http://www.khmernz.com/xbmc/khmer2all/chachacha.jpg')								
def INDEX(url):
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')             
        match=re.compile('<div id="archive">(.+?)<div class="right_column">').findall(newlink)
        if(len(match) >= 1):
                linkmatch=re.compile('<div class="archivehoriz_label"><a href="(.+?)" ><div class="thumb_image"><img src="(.+?)" width="100" height="75" title=".+?" alt="(.+?)" />').findall(match[0])
                for vzLink,vzpic,vzLinkName in linkmatch:
                    addLink(vzLinkName.encode("utf-8"),strDomain+vzLink,3,vzpic)		
 
def GetContent(url):
    try:
       net = Net()
       second_response = net.http_GET(url)
       return second_response.content
    except:	
       d = xbmcgui.Dialog()
       d.ok(url,"Can't Connect to site",'Try again in a moment')
def GET_HTTP(url):
  req = urllib2.Request(url)
  req.add_header('User-Agent','Mozilla/5.0 (Windows NT 5.1; rv:8.0) Gecko/20100101 Firefox/8.0')
  response = urllib2.urlopen(req)
  html=response.read()
  response.close()
  return html	   

def VIDEOLINKS(url,title):
  html = GET_HTTP(url)
  match=re.compile("'rtmp://(.+?)'").findall(html)  
  for link in match:
    listitem = xbmcgui.ListItem(title)
    listitem.setInfo('video', {'Title': title})
    xbmc.Player( xbmc.PLAYER_CORE_DVDPLAYER ).play(strdomainn+link, listitem)



def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        contextMenuItems = []
        liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
		
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param    



params=get_params()
url=None
name=None
mode=None
formvar=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        formvar=int(params["formvar"])
except:
        pass		


sysarg=str(sys.argv[1]) 
if mode==None or url==None or len(url)<1:
        #OtherContent()
        HOME()
       
elif mode==2:
        #d = xbmcgui.Dialog()
        #d.ok('mode 2',str(url),' ingore errors lol')
        INDEX(url)
elif mode==3:
  VIDEOLINKS(url,name)

	   
xbmcplugin.endOfDirectory(int(sysarg))
