##############################################################################
#
# Copyright (c) 2005-2008 Clearwired Web Services, LLC. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
"""Blend CPS Container - Last Updated 2.25.2007"""

__version__='$Revision: 1.0.0 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from OFS.Folder import Folder, ObjectManager, PropertyManager, FindSupport
from AccessControl import ClassSecurityInfo
from App.ImageFile import ImageFile
import Acquisition


class BlendSite(Folder):

	"""
	A Blend CMS Object

	"""
	meta_type = "Blend Site"
	index_html = None
	"docstring"

	manage_options = (
		{'label': 'Contents', 'action': 'manage_main',},
		{'label': 'CMS View', 'action': 'indexCMS',},
		{'label': 'Site View', 'action': 'index_html',},
		{'label': 'CMS Edit', 'action': 'siteEdit',},
		{'label': 'Security', 'action': 'manage_access',},
		{'label': 'Properties', 'action': 'manage_propertiesForm',},
	)

	def __init__(self, id, metakeywords, metadescription, title, clientaddress, clientcity, clientstate, clientzip, clientphone1, clientphone2, clientemail, eventTypes, newsTypes, clusterTypes, siteTags, prefix, suffix, workgroup, timezone):
		self.id = id
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.title = title
		self.clientaddress = clientaddress
		self.clientcity = clientcity
		self.clientstate = clientstate
		self.clientzip = clientzip
		self.clientphone1 = clientphone1
		self.clientphone2 = clientphone2
		self.clientemail = clientemail
		self.eventTypes = eventTypes
		self.newsTypes = newsTypes
		self.clusterTypes = clusterTypes
		self.siteTags = siteTags
		self.prefix = prefix
		self.suffix = suffix
		self.workgroup = workgroup
		self.timezone = timezone

	def manage_editSaveAction(self, metakeywords, metadescription, title, clientaddress, clientcity, clientstate, clientzip, clientphone1, clientphone2, clientemail, eventTypes, newsTypes, clusterTypes, siteTags, prefix, suffix, workgroup, timezone, RESPONSE=None):
		"Edit CMS Site properties"
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.title = title
		self.clientaddress = clientaddress
		self.clientcity = clientcity
		self.clientstate = clientstate
		self.clientzip = clientzip
		self.clientphone1 = clientphone1
		self.clientphone2 = clientphone2
		self.clientemail = clientemail
		self.eventTypes = eventTypes
		self.newsTypes = newsTypes
		self.clusterTypes = clusterTypes
		self.siteTags = siteTags
		self.prefix = prefix
		self.suffix = suffix
		self.workgroup = workgroup
		self.timezone = timezone
		self._p_changed = 1
		RESPONSE.redirect('siteEdit')

	def manage_editViewAction(self, metakeywords, metadescription, title, clientaddress, clientcity, clientstate, clientzip, clientphone1, clientphone2, clientemail, eventTypes, newsTypes, clusterTypes, siteTags, prefix, suffix, workgroup, timezone, RESPONSE=None):
		"Edit CMS Site properties"
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.title = title
		self.clientaddress = clientaddress
		self.clientcity = clientcity
		self.clientstate = clientstate
		self.clientzip = clientzip
		self.clientphone1 = clientphone1
		self.clientphone2 = clientphone2
		self.clientemail = clientemail
		self.eventTypes = eventTypes
		self.newsTypes = newsTypes
		self.clusterTypes = clusterTypes
		self.siteTags = siteTags
		self.prefix = prefix
		self.suffix = suffix
		self.workgroup = workgroup
		self.timezone = timezone
		self._p_changed = 1
		RESPONSE.redirect('cms')

	def manage_editSaveSetup(self, metakeywords, metadescription, RESPONSE=None):
		"Edit CMS Site properties"
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self._p_changed = 1
		RESPONSE.redirect('setup_html')
		
	#manage tags
	def buildTags(self, item):
		taglist = item
		tagfreq = [taglist.count(p) for p in taglist]
		dictionary = dict(zip(taglist, tagfreq))
		return dictionary
	
	#build tags efficiently - NOT IMPLEMENTED - 32907
	def theTagDict(self, item):
		taglist = item
		taglist = taglist.sort(cmp)
		for i in taglist:
			tagdict[i] = taglist.get(i, 0) + 1
			return tagdict
		
	def scrubTags(self, tag):
		tag = tag.rstrip()
		tag = tag.lstrip()
		tag = tag.upper()
		return tag

	def displayTags(self, tag):
		tag = tag.rstrip()
		tag = tag.lstrip()
		tag = tag.upper()
		return tag

	def manage_editExtFile(self, title, descr, RESPONSE=None):
		self.title = title
		self.descr = descr
		RESPONSE.redirect('../../images_html')
		
	__call__ = DTMLFile('dtml/indexBlend', globals())
	"docstring"

	#display pages
	content_html = DTMLFile('dtml/indexContent', globals())
	mydocs_html = DTMLFile('dtml/indexMydocs', globals())
	users_html = DTMLFile('dtml/indexUsers', globals())
	addUser_html = DTMLFile('dtml/manage_addUser', globals())
	editUser_html = DTMLFile('dtml/manage_editUser', globals())
	deleteUser_html = DTMLFile('dtml/manage_deleteUser', globals())
	viewUser_html = DTMLFile('dtml/manage_viewUser', globals())
	adminNews_html = DTMLFile('dtml/wells/adminNewsWell', globals())
	page_html = DTMLFile('dtml/wells/pageWell', globals())
	ipage_html = DTMLFile('dtml/wells/ipageWell', globals())
	people_html = DTMLFile('dtml/wells/peopleWell', globals())
	articles_html = DTMLFile('dtml/wells/articleWell', globals())
	clusters_html = DTMLFile('dtml/wells/clusterWell', globals())
	images_html = DTMLFile('dtml/wells/imageWell', globals())
	files_html = DTMLFile('dtml/wells/fileWell', globals())
	news_html = DTMLFile('dtml/wells/newsWell', globals())
	events_html = DTMLFile('dtml/wells/eventWell', globals())
	promos_html = DTMLFile('dtml/wells/promoWell', globals())
	homepage_html = DTMLFile('dtml/wells/homepageWell', globals())
	users_html = DTMLFile('dtml/cmsUsers', globals())
	setup_html = DTMLFile('dtml/cmsSetup', globals())
	help_html = DTMLFile('dtml/cmsHelp', globals())
	quickadd_html = DTMLFile('dtml/quickAdd', globals())
	pagePublish1_html = DTMLFile('dtml/manage_pagePublish1', globals())
	pagePublish2_html = DTMLFile('dtml/manage_pagePublish2', globals())
	pagePublish3_html = DTMLFile('dtml/manage_pagePublish3', globals())
	pagePublish4_html = DTMLFile('dtml/manage_pagePublish4', globals())
	doPublish1 = DTMLFile('dtml/manage_doPublish1', globals())
	doPublish2 = DTMLFile('dtml/manage_doPublish2', globals())
	doRemove = DTMLFile('dtml/manage_doRemove', globals())
	doRemovePage = DTMLFile('dtml/manage_doRemovePage', globals())
	doMoveUp = DTMLFile('dtml/manage_doMoveUp', globals())
	doMoveDown = DTMLFile('dtml/manage_doMoveDown', globals())
	doMoveTop = DTMLFile('dtml/manage_doMoveTop', globals())
	doMoveBottom = DTMLFile('dtml/manage_doMoveBottom', globals())
	doMoveUpPage = DTMLFile('dtml/manage_doMoveUpPage', globals())
	doMoveDownPage = DTMLFile('dtml/manage_doMoveDownPage', globals())
	doMoveTopPage = DTMLFile('dtml/manage_doMoveTopPage', globals())
	doMoveBottomPage = DTMLFile('dtml/manage_doMoveBottomPage', globals())
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	publish_header = DTMLFile('dtml/publish_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	standard_error_message = DTMLFile('dtml/standard_error_message', globals())
	cms_error_header = DTMLFile('dtml/cms_error_header', globals())
	siteEdit = DTMLFile('dtml/manage_editSite', globals())
	addImage = DTMLFile('dtml/manage_addExtImage', globals())
	addPersonImage = DTMLFile('dtml/manage_addExtImagePerson', globals())
	addArticleFile = DTMLFile('dtml/manage_addExtFileArticle', globals())
	articleUploadSuccess = DTMLFile('dtml/manage_addArticleSuccess', globals())
	addFile = DTMLFile('dtml/manage_addExtFile', globals())
	deleteImage = DTMLFile('dtml/manage_deleteImage', globals())
	deleteFile = DTMLFile('dtml/manage_deleteFile', globals())
	configure = DTMLFile('dtml/manage_configure', globals())
	
	#CMS edit screens for ExtImage and ExtFile
	imageEditCMS = DTMLFile('dtml/manage_editImageCMS', globals())
	fileEditCMS = DTMLFile('dtml/manage_editFileCMS', globals())
	editImage = DTMLFile('dtml/manage_editExtImage', globals())
	editFile = DTMLFile('dtml/manage_editExtFile', globals())
	

#Constructor pages. Only used when the product is added to a folder.
def manage_addSiteAction(self, id, metakeywords='', metadescription='', title='', clientaddress='', clientcity='', clientstate='', clientzip='', clientphone1='', clientphone2='', clientemail='',eventTypes='', newsTypes='', clusterTypes='', siteTags='', prefix='', suffix='', workgroup='', timezone='', RESPONSE=None):
	"Add a Blend Site to a folder"
	newSite = BlendSite(id, metakeywords, metadescription, title, clientaddress, clientcity, clientstate, clientzip, clientphone1, clientphone2, clientemail, eventTypes, newsTypes, clusterTypes, siteTags, prefix, suffix, workgroup, timezone)
	self._setObject(id, newSite)
	RESPONSE.redirect('../../blend/configure')

manage_addSiteForm = DTMLFile('dtml/manage_addSite', globals())

InitializeClass(BlendSite)