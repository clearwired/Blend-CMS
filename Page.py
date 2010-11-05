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
"""Blend CM Page - Last Updated 2.25.2007"""

__version__='$Revision: 1.0.1 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from urllib import quote
from OFS.ObjectManager import ObjectManager
from DateTime import DateTime
	 
class Page(SimpleItem, PropertyManager):
    
	"""
	A Blend Page object
	"""

	meta_type = "Blend Page"

	manage_options = (
		(
			{'label': 'Edit', 'action': 'manage_main',},                
			{'label': 'View', 'action': 'manage_view',},
			{'label': 'CMS Edit', 'action': 'pageEditCMS',},
		)
		+PropertyManager.manage_options
		+SimpleItem.manage_options
		)
	
	def __init__(self,id,primaryimg,title,seotitle,metakeywords,metadescription,data,PromoPosA,PromoPosB,PromoPosC,PromoPosD,PromoPosE,PromoPosF,created,tags,container,template='default', primaryimgcaption=''):
		"initialize a new instance of a CMS Page"
		self.id = id #required
		self.primaryimg = primaryimg
		self.primaryimgcaption = primaryimgcaption
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.title = title
		self.seotitle = seotitle
		self.data = data
		self.PromoPosA = PromoPosA
		self.PromoPosB = PromoPosB
		self.PromoPosC = PromoPosC
		self.PromoPosD = PromoPosD
		self.PromoPosE = PromoPosE
		self.PromoPosF = PromoPosF
		self.created = created
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.upper()
		self.container = []
		self.template = template

	def manage_editSaveAction(self, primaryimg, title, seotitle, metakeywords, metadescription, data, PromoPosA, PromoPosB, PromoPosC, PromoPosD, PromoPosE, PromoPosF, created, tags, template='default', primaryimgcaption='', RESPONSE=None):
		"Edit CMS Page product property values"
		self.primaryimg = primaryimg
		self.primaryimgcaption = primaryimgcaption
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.title = title
		self.seotitle = seotitle
		self.data = data
		self.PromoPosA = PromoPosA
		self.PromoPosB = PromoPosB
		self.PromoPosC = PromoPosC
		self.PromoPosD = PromoPosD
		self.PromoPosE = PromoPosE
		self.PromoPosF = PromoPosF
		self.created = created
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.upper()
		self.template = template
		self._p_changed = 1
		RESPONSE.redirect('pageEditCMS')

	def manage_editZMI(self, title, seotitle, data, created, RESPONSE=None):
		"Edit CMS Page product property values"
		self.title = title
		self.seotitle = seotitle
		self.data = data
		self.created = created
		self._p_changed = 1
		RESPONSE.redirect('manage_main')

	#functions for manipulating dictionaries  
	def getDictItems(self,m):
		return m.items()

	def getDictKeys(self,m):
		return m.keys()

	def getDictValues(self,m):
		return m.values()

	#functions for managing published objects
	def publishNav(self):
		for x in self.container:
			return x

	def getListItems(self):
		return self.container

	def manage_publishItems(self,item):
		"Create publish container"
		self.container.append(item)
		self._p_changed = 1

	def removeItem(self,item):
		self.container.remove(item)
		self._p_changed = 1

	#functions for ordering published objects
	def moveItemUp(self,item):
		if item >= 1:
			page = item - 1
		else:
			page = 0
			addl = item + 1
			self.container[addl:page] = self.container[page:item]
			del self.container[page]
			self._p_changed = 1

	def moveItemDown(self,item):
		page = item + 1
		addl = item + 2
		self.container[addl:page] = self.container[item:page]
		del self.container[item]
		self._p_changed = 1

	def moveItemTop(self,item):
		page = self.container[0:item]
		for x in page:
			self.container.append(x)
		del self.container[0:item]
		self._p_changed = 1

	def moveItemBottom(self,item):
		self.container.append(item)
		self.container.remove(item)
		self._p_changed = 1

	index_html = DTMLFile('dtml/indexPage', globals())
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	manage_main = DTMLFile('dtml/manage_editPage', globals())
	pageEditCMS = DTMLFile('dtml/manage_editPageCMS', globals())
	delete = DTMLFile('dtml/manage_deletePage', globals())

#Constructor pages. Only used when the product is added to a folder.
	
def manage_addPageAction(self, id, primaryimg='', metadescription='', metakeywords='', title='', seotitle='', data='', PromoPosA='', PromoPosB='', PromoPosC='', PromoPosD='', PromoPosE='', PromoPosF='', created=DateTime().strftime('%Y/%m/%d'), tags='', container=[], RESPONSE=None):
	"Add a Blend Page to a folder"
	id=id.lower()
	id=id.lstrip()
	id=id.rstrip()
	id=id.replace(' ','_')
	self._setObject(id, Page(id,primaryimg, metakeywords, metadescription, title, seotitle, data,PromoPosA, PromoPosB, PromoPosC, PromoPosD, PromoPosE, PromoPosF, created, tags, container))
	RESPONSE.redirect('../../../page_html?size=50')


manage_addPage = DTMLFile('dtml/manage_addPage', globals())

InitializeClass(Page)
