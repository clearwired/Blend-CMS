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
"""Blend CPS Admistrator News - Last Updated 2.25.2007"""

__version__='$Revision: 1.0.1 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from urllib import quote
from OFS.ObjectManager import ObjectManager
from DateTime import DateTime


class AdminNews(SimpleItem, PropertyManager):
    
	"""
	A Blend Admin News object
	"""
	
	meta_type = "Blend Admin News"

	manage_options = (
            (
                {'label': 'Edit', 'action': 'manage_main',},                
                {'label': 'View', 'action': 'manage_view',},
                {'label': 'CMS Edit', 'action': 'adminNewsEditCMS',},
            )
        +PropertyManager.manage_options
	    +SimpleItem.manage_options
            )
	
	def __init__(self,id,title,data,author,active,tags,created):
		"initialize a new instance of a Blend Admin News"
		self.id = id #required
		self.title = title
		self.author = author
		self.data = data
		self.active = active
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.created = created

	def manage_editSaveAction(self, title, data, author, active, tags, created, RESPONSE=None):
		"Edit CMS Admin News object property values"
		self.title = title
		self.data = data
		self.author = author
		self.active = active
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.created = created
		self._p_changed = 1
		RESPONSE.redirect('adminNewsEditCMS')

	def manage_editZMI(self, title, author, data, created, RESPONSE=None):
		"Edit CMS Admin News product property values"
		self.title = title
		self.author = author            
		self.data = data
		self.created = created
		self._p_changed = 1
		RESPONSE.redirect('manage_main')             

	index_html = DTMLFile('dtml/indexAdminNews', globals())
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	news_header = DTMLFile('dtml/news_cms_header', globals())
	site_header = DTMLFile('dtml/standard_html_header', globals())
	site_footer = DTMLFile('dtml/standard_html_footer', globals())
	manage_main = DTMLFile('dtml/manage_editAdminNews', globals())
	adminNewsEditCMS = DTMLFile('dtml/manage_editAdminNewsCMS', globals())
	checkActive = DTMLFile('dtml/manage_adminNewscheckActive', globals())
	delete = DTMLFile('dtml/manage_deleteAdminNews', globals())

#Constructor pages. Only used when the product is added to a folder.
	
def manage_addAdminNewsAction(self, id, title='', data='', author='', active=0, tags='', created=DateTime().strftime('%Y/%m/%d'),RESPONSE=None):
	"Add a Blend Admin News to a folder"
	id=id.lower()
	id=id.lstrip()
	id=id.rstrip()
	id=id.replace(' ','_')
	self._setObject(id, AdminNews(id,title,data,author,active,tags,created))
	RESPONSE.redirect('../../../adminNews_html')
            
     
manage_addAdminNews = DTMLFile('dtml/manage_addAdminNews', globals())


InitializeClass(AdminNews)
