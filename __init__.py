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
__doc__="""Blend product module - Last Updated 8.12.2007"""

__version__='1.0'[11:-2]

import BlendSite, AdminNews, Page, iPage, Homepage, News, Event, Promo, Person, Article, Cluster
from App.ImageFile import ImageFile

misc_ = {
    'logo': ImageFile('images/blend_powered.gif', globals()),
    'edit': ImageFile('images/edit.png', globals()),
    'viewit': ImageFile('images/view.png', globals()),
    'bigview': ImageFile('images/big_view.png', globals()),
    'delete': ImageFile('images/garbage.png', globals()),
    'publish': ImageFile('images/magic-wand2.png', globals()),
    'ipage': ImageFile('images/ipage.gif', globals()),
    'page': ImageFile('images/page.gif', globals()),
    'image': ImageFile('images/image.gif', globals()),
    'homepage': ImageFile('images/homepage.gif', globals()),
    'news': ImageFile('images/news.gif', globals()),
    'promos': ImageFile('images/promos.gif', globals()),       
    'calendar': ImageFile('images/calendar.gif', globals()),    
    'published': ImageFile('images/nav_refresh_green.png', globals()),
    'unpublished': ImageFile('images/nav_refresh_red.png', globals()),
    'lock': ImageFile('images/lock.gif', globals()),
    'unlock': ImageFile('images/unlock.gif', globals()),
    'remove': ImageFile('images/document_error.png', globals()),
    'top': ImageFile('images/navigate_beginning.png', globals()),
    'bottom': ImageFile('images/navigate_end.png', globals()),
    'up': ImageFile('images/navigate_up.png', globals()),
    'down': ImageFile('images/navigate_down.png', globals()),
    'manage': ImageFile('images/gears.png', globals()),     
    'scripts.js': ImageFile('js/scripts.js', globals()),
    'switch.js': ImageFile('js/switch.js', globals()),  
    'cms_styles.css': ImageFile('styles/cms_styles.css', globals()),
    'calendar.js': ImageFile('js/calendar.js', globals()),
    'calendar-setup.js': ImageFile('js/calendar-setup.js', globals()),
    'calendar-win2k-cold-1.css': ImageFile('js/calendar-win2k-cold-1.css', globals()),
    'calendar-en.js': ImageFile('js/lang/calendar-en.js', globals()),
    'validation.js': ImageFile('js/validation.js', globals()),
    'json_request.js': ImageFile('js/json_request.js', globals()), 
    'json_status_messages.js': ImageFile('js/json_status_messages.js', globals()), 
    'prototype.js': ImageFile('js/prototype.js', globals()),
    'selectabletaglist.js': ImageFile('js/selectabletaglist.js', globals()), 
    'table_sorter.js': ImageFile('js/table_sorter.js', globals()), 
    'scriptaculous.js': ImageFile('js/scriptaculous.js', globals()),
    'effects.js': ImageFile('js/effects.js', globals()),
    'lightbox.js': ImageFile('js/lightbox.js', globals()),
    'lightbox.css': ImageFile('styles/lightbox.css', globals()),
    'close.gif': ImageFile('images/close.gif', globals()),
    'closelabel.gif': ImageFile('images/closelabel.gif', globals()),
    'loading.gif': ImageFile('images/loading.gif', globals()),
    'next.gif': ImageFile('images/next.gif', globals()),
    'nextlabel.gif': ImageFile('images/nextlabel.gif', globals()),
    'prev.gif': ImageFile('images/prev.gif', globals()),
    'prevlabel.gif': ImageFile('images/prevlabel.gif', globals()),
    }

def initialize(context):
	try:
		"""This makes the Blend Site object appear in the product list"""
		context.registerClass(BlendSite.BlendSite,
			constructors = (
				BlendSite.manage_addSiteForm,
				BlendSite.manage_addSiteAction,
				),
			icon='images/site.gif' #location of the CMSite icon
			)
		"""This makes the Blend Page object appear in the product list"""
		context.registerClass(Page.Page,
			constructors = (
				Page.manage_addPage,
				Page.manage_addPageAction,
				),
			icon='images/page.gif' #location of the page icon
			)
		"""This makes the Blend iPage object appear in the product list"""
		context.registerClass(iPage.iPage,
			constructors = (
				iPage.manage_addiPage,
				iPage.manage_addiPageAction,
				),
			icon='images/ipage.gif' #location of the iPage icon
			)
		"""This makes the Blend Homepage object appear in the product list"""
		context.registerClass(Homepage.Homepage,
			constructors = (
				Homepage.manage_addHomepage,
				Homepage.manage_addHomepageAction,
				),
			icon='images/homepage.gif' #location of the Homepage icon
			)
		"""This makes the Blend News object appear in the product list"""
		context.registerClass(News.News,
			constructors = (
				News.manage_addNews,
				News.manage_addNewsAction,
				),
			icon='images/news.gif' #location of the News icon
			)
		"""This makes the Blend Event object appear in the product list"""
		context.registerClass(Event.Event,
			constructors = (
				Event.manage_addEvent,
				Event.manage_addEventAction,
				),
			icon='images/calendar.gif' #location of the Event icon
			)
		"""This makes the Blend Promo object appear in the product list"""
		context.registerClass(Promo.Promo,
 			constructors = (
				Promo.manage_addPromo,
				Promo.manage_addPromoAction,
				),
			icon='images/promos.gif' #location of the Event icon
			)
		"""This makes the Blend Admin News object appear in the product list"""
		context.registerClass(AdminNews.AdminNews,
			constructors = (
				AdminNews.manage_addAdminNews,
				AdminNews.manage_addAdminNewsAction,
				),
			icon='images/news.gif' #location of the Event icon
			)  
		"""This makes the Blend Person object appear in the product list"""
		context.registerClass(Person.Person,
			constructors = (
				Person.manage_addPerson,
				Person.manage_addPersonAction,
				),
			icon='images/page.gif' #location of the Event icon
			)
		"""This makes the Blend Article object appear in the product list"""
		context.registerClass(Article.Article,
			constructors = (
				Article.manage_addArticle,
				Article.manage_addArticleAction,
				),
			icon='images/page.gif' #location of the Event icon
			)
		"""This makes the Blend Cluster object appear in the product list"""
		context.registerClass(Cluster.Cluster,
			constructors = (
				Cluster.manage_addCluster,
				Cluster.manage_addClusterAction,
				),
			icon='images/page.gif' #location of the Event icon
			)
	except:
		from sys import exc_info, stderr
		from traceback import format_exception
		from string import join
		
		type,val,tb=exc_info()
		stderr.write(join(format_exception(type, val, tb),''))
		
		del type,val,tb
