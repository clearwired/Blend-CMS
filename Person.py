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
"""Blend CM Person - Last Updated 7.30.2007"""

__version__='$Revision: 1.0.1 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from urllib import quote
from OFS.ObjectManager import ObjectManager
from DateTime import DateTime
	 
class Person(SimpleItem, PropertyManager):
    
	"""
	A Blend Person object
	"""

	meta_type = "Blend Person"

	manage_options = (
		(
			{'label': 'Edit', 'action': 'manage_main',},                
			{'label': 'View', 'action': 'manage_view',},
			{'label': 'CMS Edit', 'action': 'personEditCMS',},
		)
		+PropertyManager.manage_options
		+SimpleItem.manage_options
		)
	
	def __init__(self,id,created,salut,other_salut,person_title,disPos,title,postitle,shortdesc,PromoPosA,PromoPosB,PromoPosC,PromoPosD,PromoPosE,PromoPosF,fname,lname,midname,cat,primary_email,secondary_email,office_phone,office_phone_ext,alternatephone1,alternatephone2,group,data,assistant_name,assistant_phone,assistant_phone_ext,assistant_email,tags,seotitle,metakeywords,metadescription):
		"initialize a new instance of a Blend Person"
		self.id = id #required
		self.created = created
		self.salut = salut
		self.other_salut = other_salut
		self.person_title = person_title
		self.disPos = disPos
		self.title = title
		self.postitle = postitle
		self.shortdesc = shortdesc
		self.PromoPosA = PromoPosA
		self.PromoPosB = PromoPosB
		self.PromoPosC = PromoPosC
		self.PromoPosD = PromoPosD
		self.PromoPosE = PromoPosE
		self.PromoPosF = PromoPosF
		self.fname = fname
		self.lname = lname
		self.midname = midname
		self.cat = cat
		self.primary_email = primary_email
		self.secondary_email = secondary_email
		self.office_phone = office_phone
		self.office_phone_ext = office_phone_ext
		self.alternatephone1 = alternatephone1
		self.alternatephone2 = alternatephone2
		self.group = group
		self.data = data
		self.assistant_name = assistant_name
		self.assistant_phone = assistant_phone
		self.assistant_phone_ext = assistant_phone_ext
		self.assistant_email = assistant_email
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.seotitle = seotitle
		self.metakeywords = metakeywords
		self.metadescription = metadescription

	def manage_editSaveAction(self,salut,other_salut,person_title,postitle,shortdesc,PromoPosA,PromoPosB,PromoPosC,PromoPosD,PromoPosE,PromoPosF,disPos,title,fname,lname,midname,cat,primary_email,secondary_email,office_phone,office_phone_ext,alternatephone1,alternatephone2,group,data,assistant_name,assistant_phone,assistant_phone_ext,assistant_email,tags,seotitle,metakeywords,metadescription, RESPONSE=None):
		"Edit Blend Person property values"
		self.salut = salut
		self.other_salut = other_salut
		self.person_title = person_title
		self.disPos = disPos
		self.title = title
		self.postitle = postitle
		self.shortdesc=shortdesc
		self.PromoPosA = PromoPosA
		self.PromoPosB = PromoPosB
		self.PromoPosC = PromoPosC
		self.PromoPosD = PromoPosD
		self.PromoPosE = PromoPosE
		self.PromoPosF = PromoPosF
		self.fname = fname
		self.lname = lname
		self.midname = midname
		self.cat = cat
		self.primary_email = primary_email
		self.secondary_email = secondary_email
		self.office_phone = office_phone
		self.office_phone_ext = office_phone_ext
		self.alternatephone1 = alternatephone1
		self.alternatephone2 = alternatephone2
		self.group = group
		self.data = data
		self.assistant_name = assistant_name
		self.assistant_phone = assistant_phone
		self.assistant_phone_ext = assistant_phone_ext
		self.assistant_email = assistant_email
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.seotitle = seotitle
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self._p_changed = 1
		RESPONSE.redirect('personEditCMS')

	def manage_editZMI(self, title, seotitle, data, created, RESPONSE=None):
		"Edit Blend Person property values"
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

	index_html = DTMLFile('dtml/indexPerson', globals())
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	manage_main = DTMLFile('dtml/manage_editPerson', globals())
	personEditCMS = DTMLFile('dtml/manage_editPersonCMS', globals())
	personAddPhoto = DTMLFile('dtml/manage_addPersonPhoto', globals())
	personDeletePhoto = DTMLFile('dtml/manage_deletePersonPhoto', globals())
	delete = DTMLFile('dtml/manage_deletePerson', globals())

#Constructor pages. Only used when the product is added to a folder.
	
def manage_addPersonAction(self, id, created=DateTime().strftime('%Y/%m/%d'), salut='', other_salut='', person_title = '', disPos='0', title='', postitle = '', shortdesc='', PromoPosA = '', PromoPosB = '', PromoPosC = '',  PromoPosD = '',  PromoPosE = '',  PromoPosF = '', fname='', lname='', midname='', cat='', primary_email='', secondary_email='', office_phone='', office_phone_ext='', alternatephone1='', alternatephone2='', group='', data='', assistant_name='', assistant_phone='', assistant_email='', assistant_phone_ext='', tags='', seotitle='', metakeywords='', metadescription='', RESPONSE=None):
	"Add a Blend Person to a folder"
	id=id.lower()
	id=id.lstrip()
	id=id.rstrip()
	id=id.replace(' ','_')
	self._setObject(id, Person(id,salut,created,other_salut,person_title,disPos,title,postitle,shortdesc,PromoPosA,PromoPosB,PromoPosC,PromoPosD,PromoPosE,PromoPosF,fname,lname,midname,cat,primary_email,secondary_email,office_phone,office_phone_ext,alternatephone1,alternatephone2,group,data,assistant_name,assistant_phone,assistant_phone_ext,assistant_email,tags,seotitle,metakeywords,metadescription))
	RESPONSE.redirect('../../../people_html?size=50')


manage_addPerson = DTMLFile('dtml/manage_addPerson', globals())

InitializeClass(Person)
