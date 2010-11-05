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
"""Blend CPS Event - Last Updated 2.25.2007"""

__version__='$Revision: 1.0.1 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from urllib import quote
from OFS.ObjectManager import ObjectManager
from DateTime import DateTime


class Event(SimpleItem, PropertyManager):
    
	"""
	A Blend Event object
	"""

	meta_type = "Blend Event"

	manage_options = (
	(
		{'label': 'Edit', 'action': 'manage_main',},
		{'label': 'View', 'action': 'manage_view',},
		{'label': 'CMS Edit', 'action': 'eventEditCMS',},
	)
	+PropertyManager.manage_options
	+SimpleItem.manage_options
	)

	def __init__(self,id,created,active,archive,title,eventtype,subtitle,abstract,data,estart,eend,expiry,tags,contactname,contactphone,contactemail):
		"initialize a new instance of a CMS Event"
		self.id = id #required
		self.created = created
		self.active = active
		self.archive = archive
		self.title = title
		self.eventtype = eventtype
		self.subtitle = subtitle
		self.abstract = abstract
		self.data = data
		self.estart = estart
		self.eend = eend
		self.expiry = expiry
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.contactname = contactname
		self.contactphone = contactphone
		self.contactemail = contactemail

	def manage_editSaveAction(self, created, title, eventtype, subtitle, abstract, data, estart, eend, expiry, tags, contactname, contactphone, contactemail, RESPONSE=None):
		"Edit CMS Event object property values"
		self.created = created
		self.title = title
		self.eventtype = eventtype
		self.subtitle = subtitle
		self.abstract = abstract
		self.data = data
		self.estart = estart
		self.eend = eend
		self.expiry = expiry
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self.contactname = contactname
		self.contactphone = contactphone
		self.contactemail = contactemail
		self._p_changed = 1
		RESPONSE.redirect('eventEditCMS')

	def manage_editZMI(self, created, title, eventtype, subtitle, abstract, data, estart, eend, expiry, contactname, contactphone, contactemail, RESPONSE=None):
		"Edit CMS Event object property values"
		self.created = created
		self.title = title
		self.eventtype = eventtype
		self.subtitle = subtitle
		self.abstract = abstract
		self.data = data
		self.estart = estart
		self.eend = eend
		self.expiry = expiry
		self.contactname = contactname
		self.contactphone = contactphone
		self.contactemail = contactemail
		self._p_changed = 1
		RESPONSE.redirect('manage_main')

	def manage_active(self, active=1, RESPONSE=None):
		"Publish an Event Object"
		self.active = active
		self._p_changed = 1
		RESPONSE.redirect('../../events_html?size=50')

	def manage_inactive(self, active=0, RESPONSE=None):
		"unPublish an Event Object"
		self.active = active
		self._p_changed = 1
		RESPONSE.redirect('../../events_html?size=50')

	def manage_archive(self, archive=1, RESPONSE=None):
		"Archive an Event Object"
		self.archive = archive
		self._p_changed = 1
		RESPONSE.redirect('../../events_html?size=50')

	def manage_unarchive(self, archive=0, RESPONSE=None):
		"unArchive an Event Object"
		self.archive = archive
		self._p_changed = 1
		RESPONSE.redirect('../../events_html?size=50')

	#display pages
	index_html = DTMLFile('dtml/indexEvent', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	site_header = DTMLFile('dtml/standard_html_header', globals())
	site_footer = DTMLFile('dtml/standard_html_footer', globals())
	manage_main = DTMLFile('dtml/manage_editEvent', globals())	
	eventEditCMS = DTMLFile('dtml/manage_editEventCMS', globals())
	checkActive= DTMLFile('dtml/manage_eventcheckPublish', globals())
	checkArchive= DTMLFile('dtml/manage_eventcheckArchive', globals())
	delete = DTMLFile('dtml/manage_deleteEvent', globals())

#Constructor pages. Only used when the product is added to a folder.
def manage_addEventAction(self, id, created=DateTime().strftime('%Y/%m/%d'), active=0, archive=0, title='', eventtype='', subtitle='', abstract='', data='', estart='', eend='', expiry = '', tags='', contactname='', contactphone='', contactemail='', RESPONSE=None):
	"Add a Blend Event Object to a folder"
	id=id.lower()
	id=id.lstrip()
	id=id.rstrip()
	id=id.replace(' ','_')
	self._setObject(id, Event(id,created,active,archive,title,eventtype,subtitle,abstract,data,estart,eend,expiry,tags,contactname,contactphone,contactemail))
	RESPONSE.redirect('../../../events_html?size=50')

manage_addEvent = DTMLFile('dtml/manage_addEvent', globals())

InitializeClass(Event)
