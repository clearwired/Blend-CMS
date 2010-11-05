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
"""Blend CPS Index Page - Last Updated 2.25.2007"""

__version__='$Revision: 1.0.1 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from urllib import quote
from OFS.ObjectManager import ObjectManager
from DateTime import DateTime


class iPage(SimpleItem, PropertyManager):
    
	"""
	A Blend Index Page object
	"""
	
	meta_type = "Blend iPage"

	manage_options = (
		(
			{'label': 'Edit', 'action': 'manage_main',},
			{'label': 'View', 'action': 'manage_view',},
			{'label': 'CMS Edit', 'action': 'ipageEditCMS',},
		)
		+PropertyManager.manage_options
		+SimpleItem.manage_options
		)
	
	def __init__(self,id,primaryimg,metakeywords,metadescription,title,seotitle,data,disPos,iPromoPosA,iPromoPosB,iPromoPosC,iPromoPosD,iPromoPosE,iPromoPosF,created,container,published,tags,template='default', primaryimgcaption=''):
		"initialize a new instance of a CMS iPage"
		self.id = id #required
		self.primaryimg = primaryimg
		self.primaryimgcaption = primaryimgcaption
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.title = title
		self.seotitle = seotitle
		self.data = data
		self.disPos = disPos
		self.iPromoPosA = iPromoPosA
		self.iPromoPosB = iPromoPosB
		self.iPromoPosC = iPromoPosC
		self.iPromoPosD = iPromoPosD
		self.iPromoPosE = iPromoPosE
		self.iPromoPosF = iPromoPosF
		self.created = created
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.container = []
		self.published = published
		self.template = template
            
	def manage_editSaveAction(self,primaryimg,metakeywords,metadescription, title, seotitle, data, disPos,iPromoPosA,iPromoPosB,iPromoPosC,iPromoPosD,iPromoPosE,iPromoPosF,created,tags,template='default', primaryimgcaption='', RESPONSE=None):
		"Edit CMS iPage product property values"
		self.primaryimg = primaryimg
		self.primaryimgcaption = primaryimgcaption
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.title = title
		self.seotitle = seotitle
		self.data = data
		self.disPos = disPos
		self.iPromoPosA = iPromoPosA
		self.iPromoPosB = iPromoPosB
		self.iPromoPosC = iPromoPosC
		self.iPromoPosD = iPromoPosD
		self.iPromoPosE = iPromoPosE
		self.iPromoPosF = iPromoPosF
		self.created = created
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.template = template
		self._p_changed = 1
		RESPONSE.redirect('ipageEditCMS')

	def manage_publish(self, published=1, RESPONSE=None):
		"Publish an iPage"
		self.published = published
		self._p_changed = 1
		RESPONSE.redirect('../../ipage_html?size=50')

	def manage_unpublish(self, published=0, RESPONSE=None):
		"unPublish an iPage"
		self.published = published
		self._p_changed = 1
		RESPONSE.redirect('../../ipage_html?size=50')

	def manage_ipagePosition(self, id,title,disPos, created, RESPONSE=None):
		"Edit CMS iPage product property values"
		self.id = id
		self.title = title
		self.disPos = disPos
		self.created = created
		self._p_changed = 1
		RESPONSE.redirect('../../ipage_html?size=50')

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

	def manage_editZMI(self, title, seotitle, data, created, published, RESPONSE=None):
		"Edit CS iPage product property values"
		self.title = title
		self.seotitle = seotitle
		self.data = data
		self.created = created
		self.published = published
		self._p_changed = 1

	#site view
	index_html = DTMLFile('dtml/indexiPage', globals())

	#cms header and footer
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())

	#edit the ipage object
	manage_main = DTMLFile('dtml/manage_editiPage', globals())
	ipageEditCMS = DTMLFile('dtml/manage_editiPageCMS', globals())

	#publish pages
	checkPublish = DTMLFile('dtml/manage_ipagecheckPublish', globals())

	#delete the ipage object
	deleteiPage = DTMLFile('dtml/manage_deleteiPage', globals())

#Constructor pages. Only used when the product is added to a folder.
def manage_addiPageAction(self, id,primaryimg='', metakeywords='', metadescription='',title='', seotitle='', data='', disPos='', iPromoPosA='', iPromoPosB='', iPromoPosC='', iPromoPosD='', iPromoPosE='', iPromoPosF='', created=DateTime().strftime('%Y/%m/%d'), published=0, container=[], tags='', RESPONSE=None):
	"Add a Blend iPage to a folder"
	id=id.lower()
	id=id.lstrip()
	id=id.rstrip()
	id=id.replace(' ','_')
	self._setObject(id, iPage(id,primaryimg,metakeywords,metadescription,title, seotitle, data,disPos,iPromoPosA,iPromoPosB,iPromoPosC,iPromoPosD,iPromoPosE,iPromoPosF,created,container,published,tags))
	RESPONSE.redirect('../../../ipage_html?size=50')


manage_addiPage = DTMLFile('dtml/manage_addiPage', globals())

InitializeClass(iPage)
