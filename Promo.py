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
"""Blend CPS Promo - Last Updated 2.25.2007"""

__version__='$Revision: 1.0.1 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from urllib import quote
from OFS.ObjectManager import ObjectManager
from DateTime import DateTime


class Promo(SimpleItem, PropertyManager):
    
	"""
	A Blend Promo object
	"""
	
	meta_type = "Blend Promo"

	manage_options = (
	(
		{'label': 'Edit', 'action': 'manage_main',},
		{'label': 'View', 'action': 'manage_view',},
		{'label': 'CMS Edit', 'action': 'promoEditCMS',},
	)
		+PropertyManager.manage_options
		+SimpleItem.manage_options
		)

	def __init__(self,id,title,data,active,tags,created):
		"initialize a new instance of a Blend Promo"
		self.id = id #required
		self.title = title
		self.data = data
		self.active = active
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.created = created

	def manage_editSaveAction(self, title, data, tags, created, RESPONSE=None):
		"Edit Blend Promo object property values"
		self.title = title
		self.data = data
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.created = created
		self._p_changed = 1
		RESPONSE.redirect('promoEditCMS')

	def manage_editZMI(self, title, data, created, RESPONSE=None):
		"Edit CMS Promo product property values"
		self.title = title
		self.data = data
		self.created = created
		self._p_changed = 1
		RESPONSE.redirect('manage_main')

	def manage_active(self, active=1, RESPONSE=None):
		"Activate an Promo"
		self.active = active
		self._p_changed = 1
		RESPONSE.redirect('../../promos_html?size=50')

	def manage_inactive(self, active=0, RESPONSE=None):
		"unActivate an Promo"
		self.active = active
		self._p_changed = 1
		RESPONSE.redirect('../../promos_html?size=50')

	index_html = DTMLFile('dtml/indexPromo', globals())
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	site_header = DTMLFile('dtml/standard_html_header', globals())
	site_footer = DTMLFile('dtml/standard_html_footer', globals())
	manage_main = DTMLFile('dtml/manage_editPromo', globals())	
	promoEditCMS = DTMLFile('dtml/manage_editPromoCMS', globals())
	checkActive = DTMLFile('dtml/manage_promocheckActive', globals())
	delete = DTMLFile('dtml/manage_deletePromo', globals())	

#Constructor pages. Only used when the product is added to a folder.
def manage_addPromoAction(self, id, title='', data='', active=0, tags='', created=DateTime().strftime('%Y/%m/%d'), RESPONSE=None):
	"Add a Blend Promo to a folder"
	id=id.lower()
	id=id.lstrip()
	id=id.rstrip()
	id=id.replace(' ','_')
	self._setObject(id, Promo(id,title,data,active,tags,created))
	RESPONSE.redirect('../../../promos_html?size=50')


manage_addPromo = DTMLFile('dtml/manage_addPromo', globals())

InitializeClass(Promo)
