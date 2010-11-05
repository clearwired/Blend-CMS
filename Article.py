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
"""Blend CM Article - Last Updated 8.12.2007"""

__version__='$Revision: 1.0.1 $'[11:-2]

from Globals import DTMLFile, HTMLFile, InitializeClass
from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from urllib import quote
from OFS.ObjectManager import ObjectManager
from DateTime import DateTime

class Article(SimpleItem,PropertyManager):

	"""
	A Blend Article object
	"""

	meta_type = "Blend Article"

	manage_options = (
		(
			{'label': 'Edit', 'action': 'manage_main',},
			{'label': 'View', 'action': 'manage_view',},
			{'label': 'CMS Edit', 'action': 'articleEditCMS',},
		)
		+PropertyManager.manage_options
		+SimpleItem.manage_options
		)
	
	def __init__(self,id,title,pubdate,expiry,author1,author2,author3,author4,author5,cat,abstract,data,electronic,metakeywords,metadescription,created,tags):
		"initialize a new instance of a Blend Article"
		self.id = id #required
		self.title = title
		self.pubdate = pubdate
		self.expiry = expiry
		self.author1 = author1
		self.author2 = author2
		self.author3 = author3
		self.author4 = author4
		self.author5 = author5
		self.cat = cat
		self.abstract = abstract
		self.data = data
		self.electronic = electronic
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.created = created
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()

	def manage_editSaveAction(self,title,pubdate,expiry,author1,author2,author3,author4,author5,cat,abstract,data,electronic,metakeywords,metadescription,created,tags,RESPONSE=None):
		"Edit Blend Article product property values"
		self.title = title
		self.pubdate = pubdate
		self.expiry = expiry
		self.author1 = author1
		self.author2 = author2
		self.author3 = author3
		self.author4 = author4
		self.author5 = author5
		self.cat = cat
		self.abstract = abstract
		self.data = data
		self.electronic = electronic
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.created = created
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
		self._p_changed = 1
		RESPONSE.redirect('articleEditCMS')

	def manage_editZMI(self,title,pubdate,expiry,author1,author2,author3,author4,author5,abstract,data,electronic,metakeywords,metadescription,created,tags,RESPONSE=None):
		"Edit Blend Article property values"
		self.title = title
		self.pubdate = pubdate
		self.expiry = expiry
		self.author1 = author1
		self.author2 = author2
		self.author3 = author3
		self.author4 = author4
		self.author5 = author5
		self.abstract = abstract
		self.data = data
		self.electronic = electronic
		self.metakeywords = metakeywords
		self.metadescription = metadescription
		self.created = created
		self.tags = tags
		self.tags = tags.strip()
		self.tags = tags.capitalize()
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
	def publishCat(self):
		for x in self.cat:
			return x

	def getCatItems(self):
		return self.cat

	def manage_publishCatItem(self,item):
		"Create publish cat"
		self.cat.append(item)
		self._p_changed = 1

	def removeCatItem(self,item):
		self.cat.remove(item)
		self._p_changed = 1
			
	index_html = DTMLFile('dtml/indexArticle', globals())
	cms_edit_header = DTMLFile('dtml/edit_cms_header', globals())
	cms_header = DTMLFile('dtml/standard_cms_header', globals())
	cms_footer = DTMLFile('dtml/standard_cms_footer', globals())
	manage_main = DTMLFile('dtml/manage_editArticle', globals())
	articleEditCMS = DTMLFile('dtml/manage_editArticleCMS', globals())
	articleAddFile = DTMLFile('dtml/manage_addArticleFile', globals())
	articleDeleteFile = DTMLFile('dtml/manage_deleteArticleFile', globals())
	delete = DTMLFile('dtml/manage_deleteArticle', globals())

#Constructor pages. Only used when the product is added to a folder.
	
def manage_addArticleAction(self,id,title='',pubdate='',expiry='',author1='',author2='',author3='',author4='',author5='',cat='',abstract='',data='',electronic='',metakeywords='',metadescription='',created=DateTime().strftime('%Y/%m/%d'),tags='',RESPONSE=None):
	"Add a Blend Article to a folder"
	id=id.lower()
	id=id.lstrip()
	id=id.rstrip()
	id=id.replace(' ','_')
	self._setObject(id, Article(id,title,pubdate,expiry,author1,author2,author3,author4,author5,cat,abstract,data,electronic,metakeywords,metadescription,created,tags))
	RESPONSE.redirect('../../../articles_html?size=50')


manage_addArticle = DTMLFile('dtml/manage_addArticle', globals())

InitializeClass(Article)
