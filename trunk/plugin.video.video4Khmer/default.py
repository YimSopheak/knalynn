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
common.plugin = "plugin.video.video4khmer"
strDomain ='http://www.video4khmer.com/'

def HOME():
        addDir('Search','http://www.video4khmer.com/',4,'http://www.khmernz.com/xbmc/khmer2all/search.png')
        addDir('Thai Lakorns','http://www.video4khmer.com/browse-khmer-movie-thai-lakorn-drama-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/thai.png')
        addDir('Thai Movies','http://www.video4khmer.com/browse-khmer-thai-movie-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/thai.png')
        addDir('Korean Videos','http://www.video4khmer.com/browse-khmer-movie-korean-drama-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/korean.png')
        addDir('Korean Movies','http://www.video4khmer.com/browse-khmer-korean-movie-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/korean.png')
        addDir('Chinese Drama','http://www.video4khmer.com/browse-khmer-movie-chinese-drama-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/chinese.png')
        addDir('Chinese Movies','http://www.video4khmer.com/browse-khmer-chinese-movie-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/chinese.png')
        addDir('Khmer Videos','http://www.video4khmer.com/browse-khmer-drama-watch-online-free-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/khmer.png')
        addDir('Khmer Movies','http://www.video4khmer.com/browse-khmer-movies-watch-online-free-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/khmer.png')
        addDir('Khmer Comedy','http://www.video4khmer.com/browse-khmer-comedy-watch-online-free-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/comedy.png')
        addDir('Khmer Boxing','http://www.video4khmer.com/browse-khmer-boxing-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/kboxing.png')
        addDir('Hang Meas Karaoke','http://www.video4khmer.com/browse-hang-meas-khmer-video-karaoke-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/rhm.png')
        addDir('Sunday Khmer Karaoke','http://www.video4khmer.com/browse-sunday-khmer-video-karaoke-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('Town Production Karaoke','http://www.video4khmer.com/browse-town-production-khmer-video-karaoke-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('Big Man Khmer Karaoke','http://www.video4khmer.com/browse-big-man-khmer-video-karaoke-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('M Production Karaoke','http://www.video4khmer.com/browse-m-production-khmer-video-karaoke-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('Rock Production Karaoke','http://www.video4khmer.com/browse-rock-production-khmer-video-karaoke-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('Spark Production Karaoke','http://www.video4khmer.com/browse-spark-production-khmer-video-karaoke-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('Chenla Brother Karaoke','http://www.video4khmer.com/browse-chenla-brother-khmer-video-karaoke-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('Khmer video clip','http://www.video4khmer.com/browse-khmer-clips-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('MISC','http://www.video4khmer.com/browse-this-and-that-accident-society-misc-videos-1-date.html',2,'http://www.khmernz.com/xbmc/khmer2all/nologo.png')
        addDir('Khmer Tv show','http://www.video4khmer.com/browse-watch-cambodia-tv-shows-online-videos-1-date.html',2,'http://moviekhmer.com/wp-content/uploads/2012/04/Khmer-Movie-Korng-Kam-Korng-Keo-180x135.jpg')
        addDir('Funney Videos','http://www.video4khmer.com/browse-funny-video-clips-videos-1-date.html',2,'http://moviekhmer.com/wp-content/uploads/2012/04/Khmer-Movie-Korng-Kam-Korng-Keo-180x135.jpg')		
def INDEX(url):
    try:
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        match=re.compile('<div id="list_subcats"><ul>(.+?)</ul>').findall(newlink)
        listcontent=re.compile('<a href="(.+?)">(.+?)</a>').findall(match[0])
        for vcontent in listcontent:
            (vurl,imgcontent)=vcontent
            titlecontent = re.compile('<img style=\'(.+?)\' class=imag src=(.+?)title="(.+?)" />').findall(imgcontent)
            if(len(titlecontent)):
                    (tmpvar,vimage,vname)=titlecontent[0]
                    addDir(vname.encode("utf-8"),vurl,5,vimage)
        match5=re.compile('<div class="pagination">(.+?)</div></div>').findall(newlink)
        if(len(match5)):
                pages=re.compile('<a href="(.+?)">(.+?)</a>').findall(match5[0])
                for pcontent in pages:
                        (pageurl,pagenum)=pcontent
                        addDir("Page " + pagenum,"http://www.video4khmer.com/"+pageurl,2,"")
    except: pass
			
def SEARCH():
        keyb = xbmc.Keyboard('', 'Enter search text')
        keyb.doModal()
        #searchText = '01'
        if (keyb.isConfirmed()):
                searchText = urllib.quote_plus(keyb.getText())
        url = 'http://www.video4khmer.com/search.php?keywords='+ searchText +'&btn=Search'
        SearchResults(url)
        
def SearchResults(url):
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        match=re.compile('<div id="browse_results"><ul>(.+?)</ul></div>').findall(newlink)
        if(len(match) >= 1):
                linkmatch=re.compile('<a href="(.+?)"><img src="(.+?)"  alt="(.+?)" class="imag" width[^>]*').findall(match[0])
                for vLink,vpic,vLinkName in linkmatch:
                    addLink(vLinkName,vLink,3,vpic)
        match5=re.compile('<div class="pagination">(.+?)</div></div>').findall(newlink)
        if(len(match5)):
                pages=re.compile('<a href="(.+?)">(.+?)</a>').findall(match5[0])
                for pcontent in pages:
                        (pageurl,pagenum)=pcontent
                        addDir("Page " + pagenum,"http://www.video4khmer.com/"+pageurl,6,"")			
			
def Episodes_old(url,name):
    #try:
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        match=re.compile('<ul><li class="video"><div class="video_i"><a href="(.+?)">').findall(newlink)
        vidseries = re.compile('-video_(.+?).html').findall(url)
        if(len(match[0])):
                vidseries = re.compile('-video_(.+?).html').findall(match[0])
                vidseries=vidseries[0]
                addLink(name,match[0],3,"")
        elif (len(vidseries)):
                vidseries=vidseries[0]
                addLink(name,url,3,"")
        try:
                lastvidseries = ParseXml("http://www.video4khmer.com/relatedclips.php?vid=" + vidseries)
                if(len(lastvidseries)):
                        lastvidseries = ParseXml("http://www.video4khmer.com/relatedclips.php?vid=" + lastvidseries)
                        if(len(lastvidseries)):
                                addDir("Next >>","http://www.video4khmer.com/relatedclips.php?vid=" + lastvidseries,7,"")
                else:
                        raise Exception("Didn't fine listing")
        except:
                match=re.compile('<div id="browse_results" (.+?)<ul>(.+?)</ul></div>').findall(newlink)
                if(len(match) >= 1):
                        linkmatch=re.compile('<img src="(.+?)"  alt=[^>]*').findall(match[0][1])
                        counter = 0
                        for vpic in linkmatch:
                            counter += 1
                            youtubeid = re.compile('/vi/(.+?)/').findall(vpic)
                            addLink(name + " " + str(counter),"http://www.youtube.com/watch?v="+youtubeid[0],3,vpic)
    #except: pass
	
def scrapeVideoInfo(videoid):
        result = common.fetchPage({"link": "http://player.vimeo.com/video/%s" % videoid,"refering": strDomain})
        collection = {}
        if result["status"] == 200:
            html = result["content"]
            html = html[html.find('{config:{'):]
            html = html[:html.find('}}},') + 3]
            html = html.replace("{config:{", '{"config":{') + "}"
            print repr(html)
            collection = json.loads(html)
        return collection

def getVideoInfo(videoid):
        common.log("")


        collection = scrapeVideoInfo(videoid)

        video = {}
        if collection.has_key("config"):
            video['videoid'] = videoid
            title = collection["config"]["video"]["title"]
            if len(title) == 0:
                title = "No Title"
            title = common.replaceHTMLCodes(title)
            video['Title'] = title
            video['Duration'] = collection["config"]["video"]["duration"]
            video['thumbnail'] = collection["config"]["video"]["thumbnail"]
            video['Studio'] = collection["config"]["video"]["owner"]["name"]
            video['request_signature'] = collection["config"]["request"]["signature"]
            video['request_signature_expires'] = collection["config"]["request"]["timestamp"]

            isHD = collection["config"]["video"]["hd"]
            if str(isHD) == "1":
                video['isHD'] = "1"


        if len(video) == 0:
            common.log("- Couldn't parse API output, Vimeo doesn't seem to know this video id?")
            video = {}
            video["apierror"] = ""
            return (video, 303)

        common.log("Done")
        return (video, 200)

def getVimeoVideourl(videoid):
        common.log("")
        
        (video, status) = getVideoInfo(videoid)


        urlstream="http://player.vimeo.com/play_redirect?clip_id=%s&sig=%s&time=%s&quality=%s&codecs=H264,VP8,VP6&type=moogaloop_local&embed_location="
        get = video.get
        if not video:
            # we need a scrape the homepage fallback when the api doesn't want to give us the URL
            common.log("getVideoObject failed because of missing video from getVideoInfo")
            return ""

        quality = "sd"
        
        if ('apierror' not in video):
            video_url =  urlstream % (get("videoid"), video['request_signature'], video['request_signature_expires'], quality)
            print video_url
            result = common.fetchPage({"link": video_url, "no-content": "true"})
            print repr(result)
            video['video_url'] = result["new_url"]

            common.log("Done")
            return video['video_url'] 
        else:
            common.log("Got apierror: " + video['apierror'])
            return ""
			
def Episodes(url,name):
    try:
        link = GetContent(url)
        newlink = ''.join(link.splitlines()).replace('\t','')
        match=re.compile('<div id="browse_results" (.+?)<ul>(.+?)</ul></div>').findall(newlink)
        if(len(match) >= 1):
                linkmatch=re.compile('<li class="video"><div class="video_i">(.+?)</div></li>').findall(match[0][1])
                counter = 0
                videolist =""
                vidPerGroup = 5
                for vpic in linkmatch:
                    vidlink=re.compile('<a href="(.+?)" title="(.+?)"><img src="(.+?)"  alt="(.+?)" class="imag" width="(.+?)" height="(.+?)" />').findall(vpic)
                    (vurl,vname,vimg,vtmp3,vtmp1,vtmp2)=vidlink[0]
                    counter += 1
                    youtubeid = re.compile('/vi/(.+?)/').findall(vimg)
                    if(len(youtubeid)):
                            addLink(vname.encode('utf-8'),"http://www.youtube.com/watch?v="+youtubeid[0],3,vimg)
                            videolist=videolist+"http://www.youtube.com/watch?v="+youtubeid[0]+";#"
                    else:
                            addLink(vname.encode('utf-8'),vurl,3,vimg)
                            videolist=videolist+vurl+";#"
                    if((counter%vidPerGroup==0 or counter==len(linkmatch)) and (len(videolist.split(';#'))-1) > 1):
                            addLink("-------Play the "+ str(len(videolist.split(';#'))-1)+" videos above--------",videolist,8,vimg)
                            videolist =""
                            
        match5=re.compile('<div class="pagination">(.+?)</div></div>').findall(newlink)
        if(len(match5)):
                pages=re.compile('<a href="(.+?)">(.+?)</a>').findall(match5[0])
                for pcontent in pages:
                        (pageurl,pagenum)=pcontent
                        addDir("Page " + pagenum,"http://www.video4khmer.com/"+pageurl,5,"")
    except: pass    

def ParseXml(url):
        newcontent=GetContent(url)
        vurl=""
        xmlcontent=xml.dom.minidom.parseString(newcontent.encode('utf-8'))
        items=xmlcontent.getElementsByTagName('video')
        if(len(items)>=1 and len(items[0].getElementsByTagName('url')[0].childNodes)):
                for itemXML in items:
                        vname=itemXML.getElementsByTagName('title')[0].childNodes[0].data
                        vurl=itemXML.getElementsByTagName('url')[0].childNodes[0].data
                        vimg=itemXML.getElementsByTagName('thumb')[0].childNodes[0].data
                        youtubeid = re.compile('/vi/(.+?)/').findall(vimg)
                        if(len(youtubeid)):
                                addLink(vname,"http://www.youtube.com/watch?v="+youtubeid[0],3,vimg)
                        else:
                                addLink(vname,vurl,3,vimg)
        if(len(vurl) >= 1):
                vidseries = re.compile('-video_(.+?).html').findall(vurl)[0]
        else:
                vidseries =""
        return vidseries


def GetContent(url):
    try:
       net = Net()
       second_response = net.http_GET(url)
       return second_response.content
    except:	
       d = xbmcgui.Dialog()
       d.ok(url,"Can't Connect to site",'Try again in a moment')

def playVideo(videoType,videoId):
    url = videoId
    if (videoType == "youtube"):
        url = getYoutube(videoId)
        print "myvideoyou"+url
    elif (videoType == "vimeo"):
        url = getVimeoVideourl(videoId)
    elif (videoType == "tudou"):
        url = 'plugin://plugin.video.tudou/?mode=3&url=' + videoId	
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(url)
		
def PLAYLIST_VIDEOLINKS(url,name):
        ok=True
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()
        #time.sleep(2)
        links = url.split(';#')
        print "linksurl" + str(url)
        pDialog = xbmcgui.DialogProgress()
        ret = pDialog.create('Loading playlist...')
        totalLinks = len(links)-1
        loadedLinks = 0
        remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B] into XBMC player playlist.'
        pDialog.update(0,'Please wait for the process to retrieve video link.',remaining_display)
        
        for videoLink in links:
                loadPlaylist(videoLink,name)
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                #print percent
                remaining_display = 'Videos loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B] into XBMC player playlist.'
                pDialog.update(percent,'Please wait for the process to retrieve video link.',remaining_display)
                if (pDialog.iscanceled()):
                        return False   
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(playList)
        if not xbmcPlayer.isPlayingVideo():
                d = xbmcgui.Dialog()
                d.ok('videourl: ' + str(playList), 'One or more of the playlist items','Check links individually.')
        return ok

def CreateList(videoType,videoLink):
    url1 = ""
    if (videoType == "youtube"):
        url1 = getYoutube(videoLink)
    elif (videoType == "vimeo"):
        url1 = getVimeoVideourl(videoId)
    elif (videoType == "tudou"):
        url1 = 'plugin://plugin.video.tudou/?mode=3&url=' + videoId	
    else:
        url1=videoLink

    if(len(videoLink) >0):
        print url1
        liz = xbmcgui.ListItem('[B]PLAY VIDEO[/B]', thumbnailImage="")
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.add(url=url1, listitem=liz)
        
def loadPlaylist(newlink,name):
        try:
           if (newlink.find("video4khmer.com") > -1):
                print newlink
                linkcontent = GetContent(newlink)
                newContent = ''.join(linkcontent.splitlines()).replace('\t','')
                titlecontent = re.compile("var flashvars = {file: '(.+?)',").findall(newContent)
                
                if(len(titlecontent) == 0):
                        titlecontent = re.compile('swfobject\.embedSWF\("(.+?)",').findall(newContent)
                newlink=titlecontent[0]
           if (newlink.find("dailymotion") > -1):
                match=re.compile('(dailymotion\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(newlink)
                if(len(match) == 0):
                        match = re.compile('http://www.dailymotion.com/swf/(.+?)&').findall(newlink)
                link = 'http://www.dailymotion.com/video/'+str(match[0])
                req = urllib2.Request(link)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                sequence=re.compile('"sequence":"(.+?)"').findall(link)
                newseqeunce = urllib.unquote(sequence[0]).decode('utf8').replace('\\/','/')
                #print 'in dailymontion:' + str(newseqeunce)
                imgSrc=re.compile('"videoPreviewURL":"(.+?)"').findall(newseqeunce)
                if(len(imgSrc[0]) == 0):
                	imgSrc=re.compile('/jpeg" href="(.+?)"').findall(link)
                dm_low=re.compile('"sdURL":"(.+?)"').findall(newseqeunce)
                dm_high=re.compile('"hqURL":"(.+?)"').findall(newseqeunce)
                CreateList('dailymontion',urllib2.unquote(dm_low[0]).decode("utf8"))
           elif (newlink.find("video.google.com") > -1):
                match=re.compile('http://video.google.com/videoplay.+?docid=(.+?)&.+?').findall(newlink)
                glink=""
                if(len(match) > 0):
                        glink = GetContent("http://www.flashvideodownloader.org/download.php?u=http://video.google.com/videoplay?docid="+match[0])
                else:
                        match=re.compile('http://video.google.com/googleplayer.swf.+?docId=(.+?)&dk').findall(newlink)
                        if(len(match) > 0):
                                glink = GetContent("http://www.flashvideodownloader.org/download.php?u=http://video.google.com/videoplay?docid="+match[0])
                gcontent=re.compile('<div class="mod_download"><a href="(.+?)" title="Click to Download">').findall(glink)
                if(len(gcontent) > 0):
                        CreateList('google',gcontent[0])
           elif (newlink.find("vimeo") > -1):
                print "newlink|" + newlink
                idmatch =re.compile("http://player.vimeo.com/video/([^\?&\"\'>]+)").findall(newlink)
                if(len(idmatch) > 0):
                        CreateList('vimeo',idmatch[0])
           elif (newlink.find("4shared") > -1):
                d = xbmcgui.Dialog()
                d.ok('Not Implemented','Sorry 4Shared links',' not implemented yet')		
           else:
                if (newlink.find("linksend.net") > -1):
                     d = xbmcgui.Dialog()
                     d.ok('Not Implemented','Sorry videos on linksend.net does not work','Site seem to not exist')		
                newlink1 = urllib2.unquote(newlink).decode("utf8")+'&dk;'
                print 'NEW url = '+ newlink1
                match=re.compile('(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(newlink1)
                if(len(match) == 0):
                    match=re.compile('http://www.youtube.com/watch\?v=(.+?)&dk;').findall(newlink1)
                if(len(match) > 0):
                    lastmatch = match[0][len(match[0])-1].replace('v/','')
                    CreateList("youtube",lastmatch)
                else:
                    CreateList("other",urllib2.unquote(newlink).decode("utf8"))
        except: pass
		
def loadVideos(newlink,name):
        try:
           if (newlink.find("video4khmer.com") > -1):
                print newlink
                linkcontent = GetContent(newlink)
                newContent = ''.join(linkcontent.splitlines()).replace('\t','')
                titlecontent = re.compile("var flashvars = {file: '(.+?)',").findall(newContent)
                
                if(len(titlecontent) == 0):
                        titlecontent = re.compile('swfobject\.embedSWF\("(.+?)",').findall(newContent)
                newlink=titlecontent[0]
           if (newlink.find("dailymotion") > -1):
                match=re.compile('(dailymotion\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(newlink)
                if(len(match) == 0):
                        match = re.compile('http://www.dailymotion.com/swf/(.+?)&').findall(newlink)
                link = 'http://www.dailymotion.com/video/'+str(match[0])
                req = urllib2.Request(link)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                sequence=re.compile('"sequence":"(.+?)"').findall(link)
                newseqeunce = urllib.unquote(sequence[0]).decode('utf8').replace('\\/','/')
                #print 'in dailymontion:' + str(newseqeunce)
                imgSrc=re.compile('"videoPreviewURL":"(.+?)"').findall(newseqeunce)
                if(len(imgSrc[0]) == 0):
                	imgSrc=re.compile('/jpeg" href="(.+?)"').findall(link)
                dm_low=re.compile('"sdURL":"(.+?)"').findall(newseqeunce)
                dm_high=re.compile('"hqURL":"(.+?)"').findall(newseqeunce)
                playVideo('dailymontion',urllib2.unquote(dm_low[0]).decode("utf8"))
           elif (newlink.find("video.google.com") > -1):
                match=re.compile('http://video.google.com/videoplay.+?docid=(.+?)&.+?').findall(newlink)
                glink=""
                if(len(match) > 0):
                        glink = GetContent("http://www.flashvideodownloader.org/download.php?u=http://video.google.com/videoplay?docid="+match[0])
                else:
                        match=re.compile('http://video.google.com/googleplayer.swf.+?docId=(.+?)&dk').findall(newlink)
                        if(len(match) > 0):
                                glink = GetContent("http://www.flashvideodownloader.org/download.php?u=http://video.google.com/videoplay?docid="+match[0])
                gcontent=re.compile('<div class="mod_download"><a href="(.+?)" title="Click to Download">').findall(glink)
                if(len(gcontent) > 0):
                        playVideo('google',gcontent[0])
           elif (newlink.find("vimeo") > -1):
                print "newlink|" + newlink
                idmatch =re.compile("http://player.vimeo.com/video/([^\?&\"\'>]+)").findall(newlink)
                if(len(idmatch) > 0):
                        playVideo('vimeo',idmatch[0])
           elif (newlink.find("4shared") > -1):
                d = xbmcgui.Dialog()
                d.ok('Not Implemented','Sorry 4Shared links',' not implemented yet')		
           else:
                if (newlink.find("linksend.net") > -1):
                     d = xbmcgui.Dialog()
                     d.ok('Not Implemented','Sorry videos on linksend.net does not work','Site seem to not exist')		
                newlink1 = urllib2.unquote(newlink).decode("utf8")+'&dk;'
                print 'NEW url = '+ newlink1
                match=re.compile('(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(newlink1)
                if(len(match) == 0):
                    match=re.compile('http://www.youtube.com/watch\?v=(.+?)&dk;').findall(newlink1)
                if(len(match) > 0):
                    lastmatch = match[0][len(match[0])-1].replace('v/','')
                    playVideo('youtube',lastmatch)
                else:
                    playVideo('other',urllib2.unquote(newlink).decode("utf8"))
        except: pass
		
def extractFlashVars(data):
        flashvars = {}
        found = False
        for line in data.split("\n"):
            if line.strip().startswith("yt.playerConfig = "):
                found = True
                print line
                p1 = line.find('"url_encoded_fmt_stream_map":')
                p2 = line.rfind('};')
                if p1 <= 0 or p2 <= 0:
                    continue
                data = line[p1 + 1:p2]
                print "databefore" + data
                p2 = data.find('",')
                data = data[1:p2]
                data = data.split(":")[1].strip().replace('"','').replace("\u0026","&")
                print "newdata"+data
                break
        if found:
            #data = json.loads(data)
            #print "loadjson"+data
            #data = data[data.find("flashvars"):]
            #data = data[data.find("\""):]
            #data = data[:1 + data[1:].find("\"")]

            #flashvars[u"url_encoded_fmt_stream_map"]=urllib.quote_plus("sig=5F5DCF6D8710C32BAB3BF7716F817A96129BD004.9ED642709E32DEC5070F225A2BF30BED8989C2BB&itag=43&url=http%3A%2F%2Fr9---sn-i3b7sn7d.c.youtube.com%2Fvideoplayback%3Fmt%3D1360813931%26ratebypass%3Dyes%26itag%3D43%26sver%3D3%26fexp%3D902904%252C901803%252C914036%252C911928%252C920704%252C912806%252C902000%252C922403%252C922405%252C929901%252C913605%252C925006%252C908529%252C920201%252C911116%252C926403%252C910221%252C901451%252C919114%26ms%3Dau%26upn%3DjibP6ZvjXl4%26cp%3DU0hVRVhOVF9NUENONV9QSFhKOlpqbmZMTXRYMHVP%26key%3Dyt1%26id%3D1d9229a6ccfa63e4%26mv%3Dm%26newshard%3Dyes%26ipbits%3D8%26ip%3D111.67.106.161%26source%3Dyoutube%26expire%3D1360836986%26sparams%3Dcp%252Cid%252Cip%252Cipbits%252Citag%252Cratebypass%252Csource%252Cupn%252Cexpire&type=video%2Fwebm%3B+codecs%3D%22vp8.0%2C+vorbis%22&quality=medium&fallback_host=tc.v7.cache1.c.youtube.com,sig=C1FB08FE99ACA2BFAE0D3EF67B30D1F0ED990A38.9D2480603ECACC8263BD9EACE86FDB065BCBE5A1&itag=34&url=http%3A%2F%2Fr9---sn-i3b7sn7d.c.youtube.com%2Fvideoplayback%3Fmt%3D1360813931%26itag%3D34%26sver%3D3%26fexp%3D902904%252C901803%252C914036%252C911928%252C920704%252C912806%252C902000%252C922403%252C922405%252C929901%252C913605%252C925006%252C908529%252C920201%252C911116%252C926403%252C910221%252C901451%252C919114%26ms%3Dau%26upn%3DjibP6ZvjXl4%26factor%3D1.25%26key%3Dyt1%26id%3D1d9229a6ccfa63e4%26mv%3Dm%26newshard%3Dyes%26ipbits%3D8%26ip%3D111.67.106.161%26burst%3D40%26algorithm%3Dthrottle-factor%26source%3Dyoutube%26expire%3D1360836986%26cp%3DU0hVRVhOVF9NUENONV9QSFhKOlpqbmZMTXRYMHVP%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire&type=video%2Fx-flv&quality=medium&fallback_host=tc.v3.cache4.c.youtube.com,sig=0A0393E3D42E3ECA061F3631DAE92E1A86562237.C4A42977A7BCB3697391501A87AF6DEE26C35906&itag=18&url=http%3A%2F%2Fr9---sn-i3b7sn7d.c.youtube.com%2Fvideoplayback%3Fmt%3D1360813931%26ratebypass%3Dyes%26itag%3D18%26sver%3D3%26fexp%3D902904%252C901803%252C914036%252C911928%252C920704%252C912806%252C902000%252C922403%252C922405%252C929901%252C913605%252C925006%252C908529%252C920201%252C911116%252C926403%252C910221%252C901451%252C919114%26ms%3Dau%26upn%3DjibP6ZvjXl4%26cp%3DU0hVRVhOVF9NUENONV9QSFhKOlpqbmZMTXRYMHVP%26key%3Dyt1%26id%3D1d9229a6ccfa63e4%26mv%3Dm%26newshard%3Dyes%26ipbits%3D8%26ip%3D111.67.106.161%26source%3Dyoutube%26expire%3D1360836986%26sparams%3Dcp%252Cid%252Cip%252Cipbits%252Citag%252Cratebypass%252Csource%252Cupn%252Cexpire&type=video%2Fmp4%3B+codecs%3D%22avc1.42001E%2C+mp4a.40.2%22&quality=medium&fallback_host=tc.v24.cache7.c.youtube.com,sig=17D8079585E194851B1827C484A960DA22AD51C9.02F0E6DAF8CC9EA320E477549CAC62B1788964D2&itag=5&url=http%3A%2F%2Fr9---sn-i3b7sn7d.c.youtube.com%2Fvideoplayback%3Fmt%3D1360813931%26itag%3D5%26sver%3D3%26fexp%3D902904%252C901803%252C914036%252C911928%252C920704%252C912806%252C902000%252C922403%252C922405%252C929901%252C913605%252C925006%252C908529%252C920201%252C911116%252C926403%252C910221%252C901451%252C919114%26ms%3Dau%26upn%3DjibP6ZvjXl4%26factor%3D1.25%26key%3Dyt1%26id%3D1d9229a6ccfa63e4%26mv%3Dm%26newshard%3Dyes%26ipbits%3D8%26ip%3D111.67.106.161%26burst%3D40%26algorithm%3Dthrottle-factor%26source%3Dyoutube%26expire%3D1360836986%26cp%3DU0hVRVhOVF9NUENONV9QSFhKOlpqbmZMTXRYMHVP%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire&type=video%2Fx-flv&quality=small&fallback_host=tc.v2.cache1.c.youtube.com,sig=39AE834781AA29AC4DC4AF7DB5EE23943C427D93.1A0E0F0393E5FC7A7089552E8BB90C15D9F9AC13&itag=36&url=http%3A%2F%2Fr9---sn-i3b7sn7d.c.youtube.com%2Fvideoplayback%3Fmt%3D1360813931%26itag%3D36%26sver%3D3%26fexp%3D902904%252C901803%252C914036%252C911928%252C920704%252C912806%252C902000%252C922403%252C922405%252C929901%252C913605%252C925006%252C908529%252C920201%252C911116%252C926403%252C910221%252C901451%252C919114%26ms%3Dau%26upn%3DjibP6ZvjXl4%26factor%3D1.25%26key%3Dyt1%26id%3D1d9229a6ccfa63e4%26mv%3Dm%26newshard%3Dyes%26ipbits%3D8%26ip%3D111.67.106.161%26burst%3D40%26algorithm%3Dthrottle-factor%26source%3Dyoutube%26expire%3D1360836986%26cp%3DU0hVRVhOVF9NUENONV9QSFhKOlpqbmZMTXRYMHVP%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire&type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22&quality=small&fallback_host=tc.v13.cache7.c.youtube.com,sig=A79C1538EB3E4B4D2DAD1420BD8188D7B0ED9CB5.6D0EC72728EAE97ED7A5642666FA00F02FF685FD&itag=17&url=http%3A%2F%2Fr9---sn-i3b7sn7d.c.youtube.com%2Fvideoplayback%3Fmt%3D1360813931%26itag%3D17%26sver%3D3%26fexp%3D902904%252C901803%252C914036%252C911928%252C920704%252C912806%252C902000%252C922403%252C922405%252C929901%252C913605%252C925006%252C908529%252C920201%252C911116%252C926403%252C910221%252C901451%252C919114%26ms%3Dau%26upn%3DjibP6ZvjXl4%26factor%3D1.25%26key%3Dyt1%26id%3D1d9229a6ccfa63e4%26mv%3Dm%26newshard%3Dyes%26ipbits%3D8%26ip%3D111.67.106.161%26burst%3D40%26algorithm%3Dthrottle-factor%26source%3Dyoutube%26expire%3D1360836986%26cp%3DU0hVRVhOVF9NUENONV9QSFhKOlpqbmZMTXRYMHVP%26sparams%3Dalgorithm%252Cburst%252Ccp%252Cfactor%252Cid%252Cip%252Cipbits%252Citag%252Csource%252Cupn%252Cexpire&type=video%2F3gpp%3B+codecs%3D%22mp4v.20.3%2C+mp4a.40.2%22&quality=small&fallback_host=tc.v21.cache4.c.youtube.com")
            flashvars[u"url_encoded_fmt_stream_map"]=data
        return flashvars              
def selectVideoQuality(links):
        link = links.get
        video_url = ""
        fmt_value = {
                5: "240p h263 flv container",
                18: "360p h264 mp4 container | 270 for rtmpe?",
                22: "720p h264 mp4 container",
                26: "???",
                33: "???",
                34: "360p h264 flv container",
                35: "480p h264 flv container",
                37: "1080p h264 mp4 container",
                38: "720p vp8 webm container",
                43: "360p h264 flv container",
                44: "480p vp8 webm container",
                45: "720p vp8 webm container",
                46: "520p vp8 webm stereo",
                59: "480 for rtmpe",
                78: "seems to be around 400 for rtmpe",
                82: "360p h264 stereo",
                83: "240p h264 stereo",
                84: "720p h264 stereo",
                85: "520p h264 stereo",
                100: "360p vp8 webm stereo",
                101: "480p vp8 webm stereo",
                102: "720p vp8 webm stereo",
                120: "hd720",
                121: "hd1080"
        }
        hd_quality = 1

        # SD videos are default, but we go for the highest res
        #print video_url
        if (link(35)):
            video_url = link(35)
        elif (link(59)):
            video_url = link(59)
        elif link(44):
            video_url = link(44)
        elif (link(78)):
            video_url = link(78)
        elif (link(34)):
            video_url = link(34)
        elif (link(43)):
            video_url = link(43)
        elif (link(26)):
            video_url = link(26)
        elif (link(18)):
            video_url = link(18)
        elif (link(33)):
            video_url = link(33)
        elif (link(5)):
            video_url = link(5)

        if hd_quality > 1:  # <-- 720p
            if (link(22)):
                video_url = link(22)
            elif (link(45)):
                video_url = link(45)
            elif link(120):
                video_url = link(120)
        if hd_quality > 2:
            if (link(37)):
                video_url = link(37)
            elif link(121):
                video_url = link(121)

        if link(38) and False:
            video_url = link(38)
        for fmt_key in links.iterkeys():

            if link(int(fmt_key)):
                    text = repr(fmt_key) + " - "
                    if fmt_key in fmt_value:
                        text += fmt_value[fmt_key]
                    else:
                        text += "Unknown"

                    if (link(int(fmt_key)) == video_url):
                        text += "*"
            else:
                    print "- Missing fmt_value: " + repr(fmt_key)

        video_url += " | " + 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'


        return video_url

def getYoutube(videoid):

                code = videoid
                linkImage = 'http://i.ytimg.com/vi/'+code+'/default.jpg'
                req = urllib2.Request('http://www.youtube.com/watch?v='+code+'&fmt=18')
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                
                if len(re.compile('shortlink" href="http://youtu.be/(.+?)"').findall(link)) == 0:
                        if len(re.compile('\'VIDEO_ID\': "(.+?)"').findall(link)) == 0:
                                req = urllib2.Request('http://www.youtube.com/get_video_info?video_id='+code+'&asv=3&el=detailpage&hl=en_US')
                                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                                response = urllib2.urlopen(req)
                                link=response.read()
                                response.close()
                flashvars = extractFlashVars(link)

                links = {}

                for url_desc in flashvars[u"url_encoded_fmt_stream_map"].split(u","):
                        url_desc_map = cgi.parse_qs(url_desc)
                        if not (url_desc_map.has_key(u"url") or url_desc_map.has_key(u"stream")):
                                continue

                        key = int(url_desc_map[u"itag"][0])
                        url = u""
                        if url_desc_map.has_key(u"url"):
                                url = urllib.unquote(url_desc_map[u"url"][0])
                        elif url_desc_map.has_key(u"stream"):
                                url = urllib.unquote(url_desc_map[u"stream"][0])

                        if url_desc_map.has_key(u"sig"):
                                url = url + u"&signature=" + url_desc_map[u"sig"][0]
                        links[key] = url
                highResoVid=selectVideoQuality(links)
                return highResoVid     	
def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        contextMenuItems = []
        liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
		
def addNext(formvar,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&formvar="+str(formvar)+"&name="+urllib.quote_plus('Next >')
        ok=True
        liz=xbmcgui.ListItem('Next >', iconImage="http://www.video4khmer.com/templates/3column/images/header/logo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": 'Next >' } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="http://www.video4khmer.com/templates/3column/images/header/logo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def addPlayListLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
		
def LOAD_AND_PLAY_VIDEO(url,name):
        xbmc.executebuiltin("XBMC.Notification(PLease Wait!, Loading video link into XBMC Media Player,5000)")
        ok=True
        print "playlist url="+url
        videoUrl = loadVideos(url,name,True,False)
        if videoUrl == None:
                d = xbmcgui.Dialog()
                d.ok('look',str(url),'Check other links.')
                return False
        elif videoUrl == 'skip':
                return False				
        elif videoUrl == 'ERROR':
                return False
        xbmcPlayer = xbmc.Player()
        xbmcPlayer.play(videoUrl)
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

#url='http://www.khmeraccess.com/video/viewvideo/6604/31end.html'		
sysarg=str(sys.argv[1]) 
if mode==None or url==None or len(url)<1:
        #OtherContent()
        HOME()
       
elif mode==2:
        #d = xbmcgui.Dialog()
        #d.ok('mode 2',str(url),' ingore errors lol')
        INDEX(url)
elif mode==3:
        #sysarg="-1"
        loadVideos(url,name)
elif mode==4:
        #sysarg="-1"
        SEARCH()
elif mode==5:
       Episodes(url,name)
elif mode==6:
       SearchResults(url)
elif mode==7:
       ParseXml(url)
elif mode==8:
       PLAYLIST_VIDEOLINKS(url,name)

	   
xbmcplugin.endOfDirectory(int(sysarg))
