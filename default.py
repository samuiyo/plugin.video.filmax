#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

#from future.standard_library import install_aliases
#install_aliases()

import os
import re
import sys
import math
import unicodedata
#import html as html_ps

try:
	import urllib.parse
	#from urllib.parse import urlparse, urlencode
	from urllib.request import urlopen, Request
	#from urllib.error import HTTPError
except:
	import urllib
	import urlparse
#import HTMLParser
#parser = HTMLParser.HTMLParser()
from resources.lib.urlselector import cineurlselector
	
addonID = xbmcaddon.Addon('plugin.video.filmax')
media = addonID.getAddonInfo('path')+"/resources/media"
APP_NAME = addonID.getAddonInfo('name')

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
try:
	args = urllib.parse.parse_qs(sys.argv[2][1:])
except:
#	import urlparse
	args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')
language = xbmc.getInfoLabel('System.Language')

# Localized strings
T_SHOWTIME=33001
T_PREMIERE=33002
T_PROYECTS=33003
T_SINOPSYS=33004
T_SEARCH_M=33005
T_SEARCH_D=33006
T_SEARCH_A=33007
T_NO_RESUL=33008
T_INFO_MEN=33009

SEL_CINE = addonID.getSetting('SEL_CINE')
if SEL_CINE == " ":
	addonID.openSettings()
	SEL_CINE = addonID.getSetting('SEL_CINE')

listing = []


def get_localized_string(code):
	dev = addonID.getLocalizedString(code)
#	dev = html_ps.unescape(dev.encode('utf-8'))
	dev = dev.encode("utf-8")
	return dev

def change_date_format(pt):
	pt = pt.replace("'",' ').split(' ') #viernes 15 d'abril del 2013
	if language == 'Catalan':
		if pt[3] == "gener": ptmonth = "01"
		if pt[3] == "febrer": ptmonth = "02"
		if pt[3] == "març": ptmonth = "03"
		if pt[3] == "abril": ptmonth = "04"
		if pt[3] == "maig": ptmonth = "05"
		if pt[3] == "juny": ptmonth = "06"
		if pt[3] == "juliol": ptmonth = "07"
		if pt[3] == "agost": ptmonth = "08"
		if pt[3] == "setembre": ptmonth = "09"
		if pt[3] == "octubre": ptmonth = "10"
		if pt[3] == "novembre": ptmonth = "11"
		if pt[3] == "desembre": ptmonth = "12"
	else:
		if pt[3] == "enero": ptmonth = "01"
		if pt[3] == "febrero": ptmonth = "02"
		if pt[3] == "marzo": ptmonth = "03"
		if pt[3] == "abril": ptmonth = "04"
		if pt[3] == "mayo": ptmonth = "05"
		if pt[3] == "junio": ptmonth = "06"
		if pt[3] == "julio": ptmonth = "07"
		if pt[3] == "agosto": ptmonth = "08"
		if pt[3] == "septiembre": ptmonth = "09"
		if pt[3] == "octubre": ptmonth = "10"
		if pt[3] == "noviembre": ptmonth = "11"
		if pt[3] == "diciembre": ptmonth = "12"
	
	#pt = datetime.strptime(pt, '%A %d de %B del %Y').strftime('%Y-%m-%d')
	if len(pt[1]) < 2: pt[1] = "0" + pt[1]
	premiered = pt[5] + "-" + ptmonth + "-" + pt[1]
	return premiered

def build_url(query):
	try:
		return base_url + '?' + urllib.parse.urlencode(query)
	except:
		return base_url + '?' + urllib.urlencode(query)

def get_clean_wSearch(ws):
	ws = ws.replace('ñ','ena2').replace('ç','ce2').replace('_','').replace(' ','_')
	ws = ''.join((c for c in unicodedata.normalize('NFD', unicode(ws)) if unicodedata.category(c) != 'Mn'))
	ws = re.sub('[^A-Za-z0-9_]+', '', ws)
	return ws

def get_showtime_list(url):
	#xbmcgui.Dialog().ok(APP_NAME, SEL_CINE, url)
	xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(APP_NAME, SEL_CINE.split('. ',1)[-1], 5000, addonID.getAddonInfo('icon')))
	
	try:
		req = Request(url)
		html = urlopen(req).read().decode('iso-8859-1').encode('utf-8')
	except:
		html = urllib.urlopen(url).read().decode('iso-8859-1').encode("utf-8")
	
	html = [line for line in html.split('\n') if "<div class='cartellera'>" in line]
	html = re.sub(r"<div class='cartellera'>", r'\n<div>', ''.join(html))
	html = re.sub(r"<br/><img title=[^>]*>", r'', html)
	html = re.sub(r"<div class='versio apcartellera'>[^</div>]*</div>", r'', html)
	html = re.sub(r"<div class='spacer'></div>[^\n]*\n", r'\n', html)
	html = re.sub(r"""<div class='spacer'></div><p class="clear">.*</p>""", r'', html)
#	html = parser.unescape(html.decode('utf-8').strip())
#	html = html_ps.unescape(html.strip())
#	html = html.encode("utf-8")
	
	query = """<div><div class='poster'.+?title="(.+?)".+?href='(.+?)'.+?src='(.+?)'>.+?</span>.+?<br/>(.+?)<br/>(.+?)<br/></div>.+?<table><tr>(.+?)</tr></table>"""
	films = re.compile(query, re.DOTALL).findall(html)
	
	#print (html)
	#print (films)
	#print (countfilms)
	
	for f in films:
		title = f[0]
		url = urlbase + f[1]
		movieID = re.sub(r"/img/pel/thumb/([0-9].*)t.jpg", r'\1' , f[2])
		image = urlbase + "/img/pel/full/" + movieID + "f.jpg"
#		director = f[3]
		genere = f[3]
		seconds = int(re.sub('[^0-9]', '', f[4]))*60
		proyects = re.sub(r"<td><span class='[^']*'>", r'\n', f[5])
		proyects = re.sub(r"(.*)([0-9][0-9])/([0-9][0-9])</span><[^>]*>", r'[COLOR lightskyblue]\1\2/\3[/COLOR]\n·', proyects)
		proyects = re.sub(r'<[^>]*>', r' ', proyects)
		proyects = proyects.replace('.',':').replace(': ','. ').replace('  ',' ')#.replace('  ',' ')
		
		try:
			req = Request(url)
			html = urlopen(req).read().decode('iso-8859-1').encode('utf-8')
		except:
			html = urllib.urlopen(url).read().decode('iso-8859-1').encode("utf-8")
		
		html = [line for line in html.split('\n') if "<span class='up'>" in line]
		html = re.sub(r"<span class='up'>IDIOMA</span>[^>]*>", r'', ''.join(html))
		
		if not 'iframe' in html and not CAST_FILT_LEN in html:
			#opts = '[x] Trailer\n[x] Cast'
			query = ".+?</span>(.+?)<br.+?</span>.+?<br.+?</span>.+?<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br"
			movies = re.findall(query, html)
			
			for m in movies:
				premiered = change_date_format(m[0].strip().lower())
				cast = []
				plot = get_localized_string(T_SINOPSYS)+':\n'+m[3].strip()+'\n\n'+get_localized_string(T_PROYECTS)+':'+proyects
				utrailer = ''
				
				list_item = xbmcgui.ListItem(label='[I][LIGHT]'+title+' †[/LIGHT][/I]')
				list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
				list_item.setInfo('video', { 'title': title, 'premiered': premiered, 'genre': genere, 'duration': seconds, 'mpaa': m[1].strip(), 'director': m[2].strip(), 'cast': cast, 'plot': plot })
				list_item.addContextMenuItems([ (get_localized_string(T_INFO_MEN), 'Action(Info)') ])
				list_item.setProperty('IsPlayable', 'false')
				
				k_url = utrailer
				
				listing.append((k_url, list_item, False))
			
		elif not 'iframe' in html and CAST_FILT_LEN in html:
			#opts = '[x] Trailer\n[v] Cast'
			query = ".+?</span>(.+?)<br.+?</span>.+?<br.+?</span>.+?<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br"
			movies = re.findall(query, html)
			
			for m in movies:
				premiered = change_date_format(m[0].strip().lower())
				cast = m[3].strip()[:-4].replace('  ',' ').split(', ')
				plot = get_localized_string(T_SINOPSYS)+':\n'+m[4].strip()+'\n\n'+get_localized_string(T_PROYECTS)+':'+proyects
				utrailer = ''
				
				list_item = xbmcgui.ListItem(label='[I][LIGHT]'+title+' †[/LIGHT][/I]')
				list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
				list_item.setInfo('video', { 'title': title, 'premiered': premiered, 'genre': genere, 'duration': seconds, 'mpaa': m[1].strip(), 'director': m[2].strip(), 'cast': cast, 'plot': plot })
				list_item.addContextMenuItems([ (get_localized_string(T_INFO_MEN), 'Action(Info)') ])
				list_item.setProperty('IsPlayable', 'false')
				
				k_url = utrailer
				
				listing.append((k_url, list_item, False))
			
		elif 'iframe'in html and not CAST_FILT_LEN in html:
			#opts = '[v] Trailer\n[x] Cast'
			query = ".+?</span>(.+?)<br.+?</span>.+?<br.+?</span>.+?<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?iframe:'(.+?)',boxid:"
			movies = re.findall(query, html)
			
			for m in movies:
				premiered = change_date_format(m[0].strip().lower())
				cast = []
				plot = get_localized_string(T_SINOPSYS)+':\n'+m[3].strip()+'\n\n'+get_localized_string(T_PROYECTS)+':'+proyects
				utrailer = re.sub(r".*/"+movieID+"/(.*)", r'plugin://plugin.video.youtube/play/?video_id=\1', m[4])
				
				list_item = xbmcgui.ListItem(label=title, path=utrailer)
				list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
				list_item.setInfo('video', { 'title': title, 'premiered': premiered, 'genre': genere, 'duration': seconds, 'mpaa': m[1].strip(), 'director': m[2].strip(), 'cast': cast, 'plot': plot })
				list_item.addContextMenuItems([ (get_localized_string(T_INFO_MEN), 'Action(Info)') ])
				list_item.setProperty('IsPlayable', 'true')
				
				k_url = utrailer
				
				listing.append((k_url, list_item, False))
			
		else:
			#opts = '[v] Trailer\n[v] Cast'
			query = ".+?</span>(.+?)<br.+?</span>.+?<br.+?</span>.+?<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?iframe:'(.+?)',boxid:"
			movies = re.findall(query, html)
			
			for m in movies:
				premiered = change_date_format(m[0].strip().lower())
				cast = m[3].strip()[:-4].replace('  ',' ').split(', ')
				plot = get_localized_string(T_SINOPSYS)+':\n'+m[4].strip()+'\n\n'+get_localized_string(T_PROYECTS)+':'+proyects
				utrailer = re.sub(r".*/"+movieID+"/(.*)", r'plugin://plugin.video.youtube/play/?video_id=\1', m[5])
				
				list_item = xbmcgui.ListItem(label=title, path=utrailer)
				list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
				list_item.setInfo('video', { 'title': title, 'premiered': premiered, 'genre': genere, 'duration': seconds, 'mpaa': m[1].strip(), 'director': m[2].strip(), 'cast': cast, 'plot': plot })
				list_item.addContextMenuItems([ (get_localized_string(T_INFO_MEN), 'Action(Info)') ])
				list_item.setProperty('IsPlayable', 'true')
				
				#k_url = '{0}?action=play&video={1}'.format(base_url, utrailer)
				k_url = utrailer
				
				listing.append((k_url, list_item, False))
			
	if len(listing) < 1:
		list_item = xbmcgui.ListItem(label=get_localized_string(T_SHOWTIME)+': '+get_localized_string(T_NO_RESUL), path='')
		k_url = ''
		listing.append((k_url, list_item, False))
	
	return listing

def get_premiere_list(url):
	try:
		req = Request(url)
		html = urlopen(req).read().decode('iso-8859-1').encode('utf-8')
	except:
		html = urllib.urlopen(url).read().decode('iso-8859-1').encode("utf-8")
	
	html = html.split("<div id='llistat-pelicules'>", 1)[-1]
	html = html.split('<div id="dreta">', 1)[0]
	html = html.replace('\t','').replace('\r','').replace('\n','')
	html = re.sub(r"<div class='cover'>", r"\n<div class='cover'>", html)
	html = [line for line in html.split('\n') if "<div class='cover'>" in line]
	html = '\n'.join(html)
#	html = parser.unescape(html.decode('utf-8').strip())
#	html = html_ps.unescape(html.strip())
#	html = html.encode("utf-8")
	
	query = """.+?title='(.+?)'.+?#no' (.+?)><.+?src='(.+?)' alt"""
	movies = re.compile(query, re.DOTALL).findall(html)
	
	for m in movies:
		title = m[0]
		if 'iframe' in m[1]:
			utrailer = re.sub(r".*/trailer/(.*)',boxid.*", r'plugin://plugin.video.youtube/play/?video_id=\1', m[1])
		else:
			utrailer = ""
		
		image = urlbase+m[2]
		
		if utrailer != '':
			list_item = xbmcgui.ListItem(label=title, path=utrailer)
			list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
			list_item.setInfo('video', { 'title': title })
			list_item.setProperty('IsPlayable', 'true')
		else:
			list_item = xbmcgui.ListItem(label='[I][LIGHT]'+title+' †[/LIGHT][/I]')
			list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
			list_item.setInfo('video', { 'title': title })
			list_item.setProperty('IsPlayable', 'false')
		
		k_url = utrailer
		
		listing.append((k_url, list_item, False))
		
	if len(listing) < 1:
		list_item = xbmcgui.ListItem(label=get_localized_string(T_PREMIERE)+': '+get_localized_string(T_NO_RESUL), path='')
		k_url = ''
		listing.append((k_url, list_item, False))
	
	return listing

def get_search_list(url):
	try:
		req = Request(url)
		html = urlopen(req).read().decode('iso-8859-1').encode('utf-8')
	except:
		html = urllib.urlopen(url).read().decode('iso-8859-1').encode("utf-8")
	
	html = html.split('<div id="esquerra">', 1)[-1]
	html = html.split('<div id="dreta">', 1)[0]
	html = [line for line in html.split('\n') if "<div class='cartellera'>" in line]
	html = re.sub(r"<div class='cartellera'>", r'\n<div>', ''.join(html))
	html = [line for line in html.split('\n') if not "<div class='versio apcartellera'>" in line]
	html = re.sub(r"<div>", r'\n<div>', ''.join(html))
	html = re.sub(r"<br/><img title=[^>]*>", r'', html)
	html = re.sub(r"<div class='spacer'></div>[^\n]*\n", r'\n', html)
#	html = parser.unescape(html.decode('utf-8').strip())
#	html = html_ps.unescape(html.strip())
#	html = html.encode("utf-8")
	
	query = """<div><div class='poster'.+?title="(.+?)".+?href='(.+?)'.+?src='(.+?)'>.+?</span><strong>(.+?)</strong><br/>.+?<br/><strong>(.+?)<br/></strong>+?</div></div>"""
	films = re.compile(query, re.DOTALL).findall(html)
	
	for f in films:
		title = f[0]
		url = urlbase + f[1]
		movieID = re.sub(r"/img/pel/thumb/([0-9].*)t.jpg", r'\1' , f[2])
		image = urlbase + "/img/pel/full/" + movieID + "f.jpg"
#		director = f[3]
		ygt = f[4].split('. ')
		if len(ygt) < 3:
			continue
		else:
			year = ygt[0]
			genere = ygt[1]
			time = ygt[2]
		seconds = int(re.sub('[^0-9]', '', time))*60
		
		try:
			req = Request(url)
			html = urlopen(req).read().decode('iso-8859-1').encode('utf-8')
		except:
			html = urllib.urlopen(url).read().decode('iso-8859-1').encode("utf-8")
		
		html = [line for line in html.split('\n') if "<span class='up'>" in line]
		html = re.sub(r"<span class='up'>", r'<span>', ''.join(html))
		
		if not 'iframe' in html and not CAST_FILT_LEN in html:
			#opts = '[x] Trailer\n[x] Cast'
			query = ".+?</span>(.+?)<br.+?</span>.+?<br.+?</span>.+?<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>.+?<br.+?</span>(.+?)<br"
			movies = re.findall(query, html)
			
			for m in movies:
				premiered = change_date_format(m[0].strip().lower())
				cast = []
				plot = get_localized_string(T_SINOPSYS)+':\n'+m[3].strip()+'\n\n'+'[I]('+m[0].strip()+')[/I]'
				utrailer = ''
				
				list_item = xbmcgui.ListItem(label='[I][LIGHT]'+title+' †[/LIGHT][/I]')
				list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
				list_item.setInfo('video', { 'title': title, 'premiered': premiered, 'genre': genere, 'duration': seconds, 'mpaa': m[1].strip(), 'director': m[2].strip(), 'cast': cast, 'plot': plot })
				list_item.addContextMenuItems([ (get_localized_string(T_INFO_MEN), 'Action(Info)') ])
				list_item.setProperty('IsPlayable', 'false')
				
				k_url = utrailer
				
				listing.append((k_url, list_item, False))
			
		elif not 'iframe' in html and CAST_FILT_LEN in html:
			#opts = '[x] Trailer\n[v] Cast'
			query = ".+?</span>(.+?)<br.+?</span>.+?<br.+?</span>.+?<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br"
			movies = re.findall(query, html)
			
			for m in movies:
				premiered = change_date_format(m[0].strip().lower())
				cast = m[3].strip()[:-4].replace('  ',' ').split(', ')
				plot = get_localized_string(T_SINOPSYS)+':\n'+m[4].strip()+'\n\n'+'[I]('+m[0].strip()+')[/I]'
				utrailer = ''
				
				list_item = xbmcgui.ListItem(label='[I][LIGHT]'+title+' †[/LIGHT][/I]')
				list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
				list_item.setInfo('video', { 'title': title, 'premiered': premiered, 'genre': genere, 'duration': seconds, 'mpaa': m[1].strip(), 'director': m[2].strip(), 'cast': cast, 'plot': plot })
				list_item.addContextMenuItems([ (get_localized_string(T_INFO_MEN), 'Action(Info)') ])
				list_item.setProperty('IsPlayable', 'false')
				
				k_url = utrailer
				
				listing.append((k_url, list_item, False))
			
		elif 'iframe' in html and not CAST_FILT_LEN in html:
			#opts = '[v] Trailer\n[x] Cast'
			query = ".+?</span>(.+?)<br.+?</span>.+?<br.+?</span>.+?<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?iframe:'(.+?)',boxid:"
			movies = re.findall(query, html)
			
			for m in movies:
				premiered = change_date_format(m[0].strip().lower())
				cast = []
				plot = get_localized_string(T_SINOPSYS)+':\n'+m[3].strip()+'\n\n'+'[I]('+m[0].strip()+')[/I]'
				utrailer = re.sub(r".*/"+movieID+"/(.*)", r'plugin://plugin.video.youtube/play/?video_id=\1', m[4])
				
				list_item = xbmcgui.ListItem(label=title, path=utrailer)
				list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
				list_item.setInfo('video', { 'title': title, 'premiered': premiered, 'genre': genere, 'duration': seconds, 'mpaa': m[1].strip(), 'director': m[2].strip(), 'cast': cast, 'plot': plot })
				list_item.addContextMenuItems([ (get_localized_string(T_INFO_MEN), 'Action(Info)') ])
				list_item.setProperty('IsPlayable', 'true')
				
				k_url = utrailer
				
				listing.append((k_url, list_item, False))
			
		else:
			#opts = '[v] Trailer\n[v] Cast'
			query = ".+?</span>(.+?)<br.+?</span>.+?<br.+?</span>.+?<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?</span>(.+?)<br.+?iframe:'(.+?)',boxid:"
			movies = re.findall(query, html)
			
			for m in movies:
				premiered = change_date_format(m[0].strip().lower())
				cast = m[3].strip()[:-4].replace('  ',' ').split(', ')
				plot = get_localized_string(T_SINOPSYS)+':\n'+m[4].strip()+'\n\n'+'[I]('+m[0].strip()+')[/I]'
				utrailer = re.sub(r".*/"+movieID+"/(.*)", r'plugin://plugin.video.youtube/play/?video_id=\1', m[5])
				
				list_item = xbmcgui.ListItem(label=title, path=utrailer)
				list_item.setArt({ 'fanart': addonID.getAddonInfo('fanart'), 'thumb': image, 'poster': image })
				list_item.setInfo('video', { 'title': title, 'premiered': premiered, 'genre': genere, 'duration': seconds, 'mpaa': m[1].strip(), 'director': m[2].strip(), 'cast': cast, 'plot': plot })
				list_item.addContextMenuItems([ (get_localized_string(T_INFO_MEN), 'Action(Info)') ])
				list_item.setProperty('IsPlayable', 'true')
				
				#k_url = '{0}?action=play&video={1}'.format(base_url, utrailer)
				k_url = utrailer
				
				listing.append((k_url, list_item, False))
			
	if len(listing) < 1:
		list_item = xbmcgui.ListItem(label=foldername+': '+get_localized_string(T_NO_RESUL), path='')
		k_url = ''
		listing.append((k_url, list_item, False))
	
	return listing

try:
	mode = args.get('mode', None)
except (SyntaxError, TypeError) as e:
	xbmc.log(msg='Error: %s' % str(e), level=xbmc.LOGERROR)

#os.path.join('assets', 'star-full.svg')
urlbase = "https://www.publicine.net"

if mode is None:
	url = build_url({'mode': 'folder', 'foldername': get_localized_string(T_SHOWTIME)})
	li = xbmcgui.ListItem(get_localized_string(T_SHOWTIME))
	li.setArt({'fanart': addonID.getAddonInfo('fanart'), 'icon': media+'/30001.jpg', 'thumb': media+'/30001.jpg', 'poster': media+'/30001p.jpg'})
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	
	url = build_url({'mode': 'folder', 'foldername': get_localized_string(T_PREMIERE)})
	li = xbmcgui.ListItem(get_localized_string(T_PREMIERE))
	li.setArt({'fanart': addonID.getAddonInfo('fanart'), 'icon': media+'/30001.jpg', 'thumb': media+'/30002.jpg', 'poster': media+'/30002p.jpg'})
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	
	url = build_url({'mode': 'folder', 'foldername': get_localized_string(T_SEARCH_M)})
	li = xbmcgui.ListItem(get_localized_string(T_SEARCH_M))
	li.setArt({'fanart': addonID.getAddonInfo('fanart'), 'icon': media+'/30001.jpg', 'thumb': media+'/30005.jpg', 'poster': media+'/30005p.jpg'})
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	
	url = build_url({'mode': 'folder', 'foldername': get_localized_string(T_SEARCH_D)})
	li = xbmcgui.ListItem(get_localized_string(T_SEARCH_D))
	li.setArt({'fanart': addonID.getAddonInfo('fanart'), 'icon': media+'/30001.jpg', 'thumb': media+'/30006.jpg', 'poster': media+'/30006p.jpg'})
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	
	url = build_url({'mode': 'folder', 'foldername': get_localized_string(T_SEARCH_A)})
	li = xbmcgui.ListItem(get_localized_string(T_SEARCH_A))
	li.setArt({'fanart': addonID.getAddonInfo('fanart'), 'icon': media+'/30001.jpg', 'thumb': media+'/30007.jpg', 'poster': media+'/30007p.jpg'})
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	
	xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
	foldername = args['foldername'][0]
	
	if foldername == get_localized_string(T_SHOWTIME):
		if language == 'Catalan':
			urllang = "/cartellera-cinema"
			CAST_FILT_LEN = "INTÈRPRETS"
		else:
			urllang = "/cartelera-cine"
			CAST_FILT_LEN = "REPARTO"
		urlcine = cineurlselector(SEL_CINE)
		url = urlbase + urllang + urlcine
		
		listing = get_showtime_list(url)

		# Add list to Kodi.
		xbmcplugin.addDirectoryItems(addon_handle, listing, len(listing))
		xbmcplugin.endOfDirectory(handle=addon_handle, succeeded=True)
	
	if foldername == get_localized_string(T_PREMIERE):
		if language == 'Catalan':
			urllang = "/properes-estrenes"
		else:
			urllang = "/proximos-estrenos"
		url = urlbase + urllang
		
		listing = get_premiere_list(url)

		# Add list to Kodi.
		xbmcplugin.addDirectoryItems(addon_handle, listing, len(listing))
		xbmcplugin.endOfDirectory(handle=addon_handle, succeeded=True)
	
	if foldername == get_localized_string(T_SEARCH_M):
		while True:
			wSearch = xbmcgui.Dialog().input(foldername+':', type=xbmcgui.INPUT_ALPHANUM)
			if len(wSearch) > 3:
				wSearch = get_clean_wSearch(wSearch)
		
				if language == 'Catalan':
					urllang = "/cerca/titol/"
					CAST_FILT_LEN = "INTÈRPRETS"
				else:
					urllang = "/busca/titol/"
					CAST_FILT_LEN = "REPARTO"
				url = urlbase + urllang + wSearch
		
				listing = get_search_list(url)
				
				# Add list to Kodi.
				xbmcplugin.addDirectoryItems(addon_handle, listing, len(listing))
				xbmcplugin.endOfDirectory(handle=addon_handle, succeeded=True)
				
				break
			
			if wSearch == '':
				break
		
	if foldername == get_localized_string(T_SEARCH_D):
		while True:
			wSearch = xbmcgui.Dialog().input(foldername+':', type=xbmcgui.INPUT_ALPHANUM)
			
			if len(wSearch) > 3:
				wSearch = get_clean_wSearch(wSearch)
		
				if language == 'Catalan':
					urllang = "/cerca/director/"
					CAST_FILT_LEN = "INTÈRPRETS"
				else:
					urllang = "/busca/director/"
					CAST_FILT_LEN = "REPARTO"
				url = urlbase + urllang + wSearch
		
				listing = get_search_list(url)
				
				# Add list to Kodi.
				xbmcplugin.addDirectoryItems(addon_handle, listing, len(listing))
				xbmcplugin.endOfDirectory(handle=addon_handle, succeeded=True)
				
				break
			
			if wSearch == '':
				break
		
	if foldername == get_localized_string(T_SEARCH_A):
		while True:
			wSearch = xbmcgui.Dialog().input(foldername+':', type=xbmcgui.INPUT_ALPHANUM)
			
			if len(wSearch) > 3:
				wSearch = get_clean_wSearch(wSearch)
				
				if language == 'Catalan':
					urllang = "/cerca/interprets/"
					CAST_FILT_LEN = "INTÈRPRETS"
				else:
					urllang = "/busca/interprets/"
					CAST_FILT_LEN = "REPARTO"
				url = urlbase + urllang + wSearch
				
				listing = get_search_list(url)
				
				# Add list to Kodi.
				xbmcplugin.addDirectoryItems(addon_handle, listing, len(listing))
				xbmcplugin.endOfDirectory(handle=addon_handle, succeeded=True)
				
				break
			
			if  wSearch == '':
				break
				#xbmc.executebuiltin('xbmc.Container.Update(plugin://plugin.video.filmax,replace)')
				#xbmc.executebuiltin('xbmc.ActivateWindow(Home)')
				#dialog.close(all,true)
		
