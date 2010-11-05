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
"""Blend CPS Homepage - Last Updated 2.25.2007"""
 
__version__='$Revision: 1.0.1 $'[11:-2] 
 
from Globals import DTMLFile, HTMLFile, InitializeClass 
from AccessControl import ClassSecurityInfo 
from OFS.SimpleItem import SimpleItem 
from OFS.PropertyManager import PropertyManager 
from urllib import quote 
from OFS.ObjectManager import ObjectManager 
from DateTime import DateTime 
 
 
class Homepage(SimpleItem, PropertyManager): 
     
	""" 
	A Blend Homepage object 
	""" 

	meta_type = "Blend Homepage" 
	index_html = None 
	"docstring" 

	manage_options = ( 
	( 
		{'label': 'Edit', 'action': 'manage_main',},
		{'label': 'View', 'action': 'manage_view',}, 
		{'label': 'CMS Edit', 'action': 'homepageEditCMS',}, 
	) 
	+PropertyManager.manage_options 
	+SimpleItem.manage_options 
	) 
	 
	def __init__(self,id,primaryimg,metakeywords,metadescription,hPromoPosA,hPromoPosB,hPromoPosC,hPromoPosD,hPromoPosE,hPromoPosF,title,seotitle,data,active,locked,created): 
		"initialize a new instance of a CMS Homepage" 
		self.id = id #required 
		self.primaryimg = primaryimg 
		self.metakeywords = metakeywords 
		self.metadescription = metadescription 
		self.hPromoPosA = hPromoPosA
		self.hPromoPosB = hPromoPosB
		self.hPromoPosC = hPromoPosC
		self.hPromoPosD = hPromoPosD
		self.hPromoPosE = hPromoPosE
		self.hPromoPosF = hPromoPosF
		self.title = title
		self.seotitle = seotitle
		self.data = data 
		self.active = active 
		self.locked = locked
		self.created = created 
 
	def manage_editSaveAction(self,primaryimg,metakeywords,metadescription,hPromoPosA,hPromoPosB,hPromoPosC,hPromoPosD,hPromoPosE,hPromoPosF,title,seotitle,data,created,RESPONSE=None): 
		"Edit CS Homepage product property values" 
		self.primaryimg = primaryimg 
		self.metakeywords = metakeywords 
		self.metadescription = metadescription 
		self.hPromoPosA = hPromoPosA
		self.hPromoPosB = hPromoPosB
		self.hPromoPosC = hPromoPosC
		self.hPromoPosD = hPromoPosD
		self.hPromoPosE = hPromoPosE
		self.hPromoPosF = hPromoPosF
		self.title = title 
		self.seotitle = seotitle
		self.data = data 
		self.created = created 
		self._p_changed = 1 
		RESPONSE.redirect('homepageEditCMS') 
 
	def manage_editViewAction(self,primaryimg,title,seotitle,metakeywords,metadescription,hPromoPosA,hPromoPosB,hPromoPosC,hPromoPosD,hPromoPosE,hPromoPosF,data,created,RESPONSE=None): 
		"Edit CMS Homepage product property values" 
		self.primaryimg = primaryimg 
		self.metakeywords = metakeywords 
		self.metadescription = metadescription 
		self.hPromoPosA = hPromoPosA
		self.hPromoPosB = hPromoPosB
		self.hPromoPosC = hPromoPosC
		self.hPromoPosD = hPromoPosD
		self.hPromoPosE = hPromoPosE
		self.hPromoPosF = hPromoPosF
		self.title = title 
		self.seotitle = seotitle
		self.data = data 
		self.created = created 
		self._p_changed = 1 
		RESPONSE.redirect('index_html')
 
	def manage_editZMI(self, title, seotitle, data, created, RESPONSE=None): 
		"Edit CMS Homepage product property values" 
		self.title = title 
		self.seotitle = seotitle
		self.data = data 
		self.created = created 
		self._p_changed = 1 
		RESPONSE.redirect('manage_main') 
 
	def manage_active(self, active=1, RESPONSE=None): 
		"Publish a Homepage" 
		self.active = active 
		self._p_changed = 1 
		RESPONSE.redirect('../../homepage_html') 
 
	def manage_inactive(self, active=0, RESPONSE=None): 
		"unPublish a Homepage" 
		self.active = active 
		self._p_changed = 1 
		RESPONSE.redirect('../../homepage_html') 
 
    #lock and unlock homepages 
	def lockId(self, locked=1, RESPONSE=None): 
		"Edit CS Homepage product property values"
		self.locked = locked 
		self._p_changed = 1 
		RESPONSE.redirect('homepageEditCMS') 
 
	def unlockId(self, locked=0, RESPONSE=None): 
		"unPublish an iPage" 
		self.locked = locked 
		self._p_changed = 1 
		RESPONSE.redirect('homepageEditCMS')
 
	#homepage view       
	__call__ = DTMLFile('dtml/indexHomepage', globals()) 
	"docstring" 
 
	index_html = DTMLFile('dtml/indexHomepage', globals()) 
	"docstring"

	#display pages
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	manage_main = DTMLFile('dtml/manage_editHomepage', globals())
	homepageEditCMS = DTMLFile('dtml/manage_editHomepageCMS', globals())
	HomecheckActive = DTMLFile('dtml/manage_homepagecheckActive', globals())
	checkLock = DTMLFile('dtml/manage_checkLock', globals())
	delete = DTMLFile('dtml/manage_deleteHomepage', globals())
 
#Constructor pages. Only used when the product is added to a folder. 
	 
def manage_addHomepageAction(self, id, primaryimg='',metakeywords='', metadescription='', hPromoPosA='', hPromoPosB='', hPromoPosC='', hPromoPosD='', hPromoPosE='',hPromoPosF='', title='', seotitle='', data='', active=0, locked=1, created=DateTime().strftime('%Y/%m/%d'), RESPONSE=None): 
	"Add a Blend Homepage to a folder"
	id=id.lower()
	id=id.lstrip()
	id=id.rstrip()
	id=id.replace(' ','_')
	self._setObject(id, Homepage(id,primaryimg,metakeywords,metadescription,hPromoPosA,hPromoPosB,hPromoPosC,hPromoPosD,hPromoPosE,hPromoPosF,title,seotitle,data,active,locked,created)) 
	RESPONSE.redirect('../../../homepage_html') 


manage_addHomepage = DTMLFile('dtml/manage_addHomepage', globals()) 
 
InitializeClass(Homepage) 
