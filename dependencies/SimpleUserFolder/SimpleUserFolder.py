# Copyright (c) 2004-2006 Simplistix Ltd
# Copyright (c) 2001-2003 New Information Paradigms Ltd
#
# This Software is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.html
# See license.txt for more details.

ManageUsersPermission = 'Manage users'
ViewManagementPermission = 'View management screens'

from AccessControl import ClassSecurityInfo
from AccessControl.User import BasicUserFolder
from Globals import InitializeClass
from OFS.ObjectManager import ObjectManager
from Shared.DC.ZRDB.Results import Results
from sys import exc_info
from User import User

import logging

logger = logging.getLogger('event.SimpleUserFolder')

def addSimpleUserFolder(self,REQUEST=None):
    """Add a SimpleUserFolder to a container as acl_users"""
    ob=SimpleUserFolder()
    self._setObject('acl_users', ob)
    if REQUEST is not None:
        return self.manage_main(self,REQUEST)

class SimpleUserFolder(ObjectManager,BasicUserFolder):

    meta_type="Simple User Folder"

    security = ClassSecurityInfo()

    manage_options=(
        ({'label':'Users', 'action':'manage_main_users',
         'help':('OFSP','User-Folder_Contents.stx')},)
        + ObjectManager.manage_options[0:1]
        + BasicUserFolder.manage_options[2:]
        )

    security.declareProtected(ViewManagementPermission,'manage_main')
    manage_main = ObjectManager.manage_main
    
    security.declareProtected(ManageUsersPermission,'manage_main_users')
    manage_main_users = BasicUserFolder.manage_main

    def manage_afterAdd(self,item,container):
        ObjectManager.manage_afterAdd(self,item,container)
        BasicUserFolder.manage_afterAdd(self,item,container)

    def manage_beforeDelete(self,item,container):
        BasicUserFolder.manage_beforeDelete(self,item,container)    
        ObjectManager.manage_beforeDelete(self,item,container)

    security.declareProtected(ManageUsersPermission,'getUserNames')
    def getUserNames(self):
        """Return a list of usernames"""
        getUserNames = getattr(self,'getUserIds',None)
        if getUserNames is None:
            return []
        names = getUserNames()
        if isinstance(names,Results):
            # extract names from the multiple rows returned
            names = [n.name for n in names]
        return names

    security.declareProtected(ManageUsersPermission,'getUser')
    def getUser(self,name):
        """Return the named user object or None"""
        try:
            getUser = getattr(self,'getUserDetails',None)
            if getUser is None:
                return None
            dict = getUser(name=name)
            if not dict:
                return None
            if isinstance(dict,Results):
                result = dict
                dict = {}
                roles = []
                keys = result.names()
                row = result[0]
                for key in keys:
                    dict[key.lower()]=row[key]
                for row in result:
                    role = row.role
                    if role:
                        roles.append(role)
                dict['roles']=roles
            dict['name']=name
            return User(dict)
        except:
            logger.error('Error getting user %r',name,
                         exc_info=True)
            return None

    security.declareProtected(ManageUsersPermission,'getUser')
    def getUsers(self):
        """Return a list of user objects"""
        return map(self.getUser,self.getUserNames())
        
    def _doAddUser(self, name, password, roles, domains, **kw):
        """Create a new user. The 'password' will be the
           original input password, unencrypted. This
           method is responsible for performing any needed encryption."""
        
        if kw:
            raise ValueError, 'keyword arguments passed to _doAddUser'
        
        if domains:
            raise ValueError, 'Simple User Folder does not support domains'

        addUser = getattr(self,'addUser',None)
        if addUser is None:
            raise UnconfiguredException, 'Addition of users has not been configured'
        
        addUser(name=name,password=password,roles=roles)

    def _doChangeUser(self, name, password, roles, domains, **kw):
        """Modify an existing user. The 'password' will be the
           original input password, unencrypted. The implementation of this
           method is responsible for performing any needed encryption."""

        if kw:
            raise ValueError, 'keyword arguments passed to _doChangeUser'
        
        if domains:
            raise ValueError, 'Simple User Folder does not support domains'

        changeUser = getattr(self,'editUser',None)
        if changeUser is None:
            raise UnconfiguredException, 'Editing of users has not been configured'

        changeUser(name=name,password=password,roles=roles)

    def _doDelUsers(self, names):
        """Delete one or more users."""
        
        delUser = getattr(self,'deleteUser',None)
        if delUser is None:
            raise UnconfiguredException, 'Deleting of users has not been configured'
        
        for name in names:
            delUser(name=name)

InitializeClass(SimpleUserFolder)

class UnconfiguredException (Exception):
    """Exception raised when a SimpleUserFolder needs configuration"""
    pass
