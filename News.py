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
"""Blend CPS News - Last Updated 2.25.2007"""

__version__='$Revision: 1.0.1 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from urllib import quote
from OFS.ObjectManager import ObjectManager
from DateTime import DateTime


class News(SimpleItem, PropertyManager):
    
	"""
	A Blend News object
	"""
	
	meta_type = "Blend News"

	manage_options = (
		(
			{'label': 'Edit', 'action': 'manage_main',},
			{'label': 'View', 'action': 'manage_view',},
			{'label': 'CMS Edit', 'action': 'newsEditCMS',},
		)
		+PropertyManager.manage_options
		+SimpleItem.manage_options
		)

	def __init__(self,id,created,active,archive,title,newstype,subtitle,abstract,data,tags,newsdate,expiry,contactname,contactphone,contactemail):
		"initialize a new instance of a CS Page"
		self.id = id
		self.created = created
		self.active = active
		self.archive = archive
		self.title = title
		self.newstype = newstype
		self.subtitle = subtitle
		self.abstract = abstract
		self.data = data
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.newsdate = newsdate
		self.expiry = expiry
		self.contactname = contactname
		self.contactphone = contactphone
		self.contactemail = contactemail

	def manage_editSaveAction(self,created,title,newstype,subtitle,abstract,data,tags,newsdate,expiry,contactname,contactphone,contactemail, RESPONSE=None):
		"Edit CMS News object property values"
		self.created = created
		self.title = title
		self.newstype = newstype
		self.subtitle = subtitle
		self.abstract = abstract
		self.data = data
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.newsdate = newsdate
		self.expiry = expiry
		self.contactname = contactname
		self.contactphone = contactphone
		self.contactemail = contactemail
		self._p_changed = 1
		RESPONSE.redirect('newsEditCMS')

	def manage_editZMI(self,created,title,newstype,subtitle,abstract,data,newsdate,expiry,contactname,contactphone,contactemail, RESPONSE=None):
		"Edit CMS News object property values"
		self.created = created   
		self.title = title
		self.newstype = newstype
		self.subtitle = subtitle
		self.abstract = abstract
		self.data = data
		self.newsdate = newsdate
		self.expiry = expiry
		self.contactname = contactname
		self.contactphone = contactphone
		self.contactemail = contactemail
		self._p_changed = 1
		RESPONSE.redirect('manage_main')

	def manage_active(self, active=1, RESPONSE=None):
		"Publish an News Object"
		self.active = active
		self._p_changed = 1
		RESPONSE.redirect('../../news_html?size=50')

	def manage_inactive(self, active=0, RESPONSE=None):
		"unPublish an News Object"
		self.active = active
		self._p_changed = 1
		RESPONSE.redirect('../../news_html?size=50')

	def manage_archive(self, archive=1, RESPONSE=None):
		"Archive an News Object"
		self.archive = archive
		self._p_changed = 1
		RESPONSE.redirect('../../news_html?size=50')

	def manage_unarchive(self, archive=0, RESPONSE=None):
		"unArchive an News Object"
		self.archive = archive
		self._p_changed = 1
		RESPONSE.redirect('../../news_html?size=50')

	#display pages
	index_html = DTMLFile('dtml/indexNews', globals())
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	manage_main = DTMLFile('dtml/manage_editNews', globals())	
	newsEditCMS = DTMLFile('dtml/manage_editNewsCMS', globals())
	checkActive= DTMLFile('dtml/manage_newscheckPublish', globals())
	checkArchive= DTMLFile('dtml/manage_newscheckArchive', globals())
	delete = DTMLFile('dtml/manage_deleteNews', globals())	

#Constructor pages. Only used when the product is added to a folder.
def manage_addNewsAction(self, id, created=DateTime().strftime('%Y/%m/%d'), active=0, archive=0, title='', newstype = '', subtitle='', abstract='', data='', tags='', newsdate='', expiry ='', contactname='', contactphone='', contactemail='', RESPONSE=None):
	"Add a Blend News object to a folder"
	id=id.lower()
	id=id.replace(' ','_')
	self._setObject(id, News(id,created,active,archive,title,newstype,subtitle,abstract,data,tags,newsdate,expiry,contactname,contactphone,contactemail))
	RESPONSE.redirect('../../../news_html?size=50')

manage_addNews = DTMLFile('dtml/manage_addNews', globals())

InitializeClass(News)
