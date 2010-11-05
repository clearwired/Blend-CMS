Simple User Folder

 Copyright (c) 2004-2006 Simplistix Ltd 
 Copyright (c) 2001-2003 New Information Paradigms Ltd

 This Software is released under the MIT License:
 http://www.opensource.org/licenses/mit-license.html 
 See license.txt for more details.

 Installation

  The Simple User Folder is installed as a normal Python Product for
  Zope.

  Unpack the .tar.gz into the Products folder of you're Zope
  installation's INSTANCE_HOME and then restart Zope.

  To add a Simple User Folder, simply navigate to the required
  location and select 'Simple User Folder' from the add list.  If a
  user folder already exists at that location, you will need to delete
  it first.  You will need to be logged in as the Emergency User to
  perform these actions at the root of your ZODB.

  It is always wise to develop and thoroughly test any support methods
  that your Simple User Folder will use before replacing an existing
  user folder.

  If at all possible, create an empty folder and thoroughly test your
  Simple User Folder instance there before using it elsewhere. This is
  particularly important if your Simple User Folder instance is to be
  used at the root of your ZODB, as if it doesn't behave as expected,
  you will have log log in as the Emergency User to correct any
  problems.

 Configuration

  The following methods need to be added in an object from which the
  Simple User Folder can acquire them. This is usually the Contents
  tab of the Simple User Folder instance.

  Alternatively, you can subclass the SimpleUserFolder class and
  implement these methods there.

   def addUser(name, password, roles)

    This adds a user. It should raise an exception if the user already
    exists.

    name
     
      a string specifying the user's name
 
    password

      a string containing the user's password.  This method must
      perform any encryption of the password that is required.

    roles

      a list of strings identifying the roles to be stored for this
      user. This list may be empty.

   def editUser(name, password, roles)

    This edits a user. It should raise an exception if the user does
    not exist.

    name
     
      a string specifying the user's name.  This identifies the user
      to be edited and so this method cannot be used to rename users.
 
    password

      a string containing the user's password or None.  If the
      password is None, the user's password should not be changed.
      This method must perform any encryption of the password that is
      required.
      

    roles

      a list of strings identifying the roles to be stored for this
      user. This list may be empty.

   def deleteUser(name)

    This deletes a user. It should raise an exception if the user does
    not exist.

   def getUserIds()

    This should return a list of user names contained in this user
    folder. Each username should be a string.

    Note: If this method is implemented with a Z SQL Method, then the
          method should return results only a 'name' column.  One row
          should be returned for each user.  See the tests for
          examples.

   def getUserDetails(name)

    This should return something that behaves like a dictionary with
    keys and values as follows:

    password

      a string containing the password for the user.  This value must
      either be in clear text or encrypted in such a way that
      AccessControl.AuthEnconding.pw_validate can encrypt a password
      supplied in the HTTP request to match it.

      pw_validate can currently handle passwords encypted using the
      following schemes:

      SSHA 
      SHA 
      CRYPT 
      MYSQL

      Further schemes can be registered using the
      AccessControl.AuthEnconding.registerScheme function.

      As an example, if you wanted to enable a user to be able to log
      in with the password 'mypassword' but you wanted to store the
      password in a SHA encrypted form, getUserDetails would need to
      return '{SHA}kd/Z3bQZiv/FwZTNjObTOP3kcOI=' for the value of the
      'password' key.

      NB: Zope's support for encrypted passwords is underdocumented
      but relatively simple. A thorough reading of the
      AccessControl.AuthEnconding module should give any required
      information. 

    roles

      a list of strings identifying the roles for the user. This list
      may be empty.

    Any others keys in the returned dictionary will be made available
    through the user's __getitem__ interface. See the tests for
    examples.

    If no user exists for the name supplied, None should be returned.

    NB: If your SimpleUserFolder appears to not be working, it may
        mean that an exception is being raised as a result of your
        getUserDetails method. Consult the event log for your Zope
        instance and look for log entries of the form:
        "SimpleUserFolder Error getting user"

    Note: If this method is implemented with a Z SQL Method, then the
          method should return results with 'name', 'password' and
          'role' columns. One row should be returned for each role the
          user has.  See the tests for examples.  Any other columns in
          the first row returned will be made available through the
          user's __getitem__ interface. See the tests for examples.
    
 Testing

  The tests can be run by running the all_tests.py script in the
  SimpleUserFolder/tests directory or using the test runner that comes
  with your version of Zope.

  
                
