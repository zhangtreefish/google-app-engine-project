AFter vagrant up and vagran ssh and cd, at vagrant$ enter 'python database_setup.py' did not lead to visible response; instead do python, get [GCC 4.8.2] on linux2 and >>>.

 # import the necessary librarie
 -------------------------------
 from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem

# connect to our restaurantMenu.db
---------------------------------
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)

# create a session to interface with the database
------------------------------------------------
DBSession=sessionmaker(bind=engine)

session=DBSession()

# now use session to CREATE, READ, UPDATE, and DELETE
-------------------------------------------
firstRestaurant=Restaurant(name="therapeutic foods")

 session.add(firstRestaurant)

 session.commit()

 # READ
 ------

  session.query(Restaurant).first()  # gets u'therapeutic foods'

  __wsgiref.simple_server__ adapts this __BaseHTTPServer__ interface to the WSGI specification, which is the standard for server-independent Python web applications.

cgihttp server: https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/

what is cgi? http://stackoverflow.com/questions/2089271/i-never-really-understood-what-is-cgi

python and web: http://learnpythonthehardway.org/book/ex50.html

[print("your input is %r") %input ]gives: your input is "mindcraft";
[print("your input is "+input) ]gives: your input is mindcraft; Why?

a script (script being another name for your .py files).

 "Hard coding" means putting some bit of information that should come from the user as a string directly in our source code.

 run python webserver.py inside vagrant directory, got the page; after enter the answer, got:Error code 501.

Message: Unsupported method ('POST').

to install unzip: sudo apt-get install unzip
sudo apt-get update
to rerun python database_setup.py does not update the db; have to delete it, and then rerun.

1. Flask :http://flask.pocoo.org/docs/0.10/quickstart/#url-building
2. when using render_template, place .html in templates subdirectory
3: after implementing JSON for puppies with jasonify and seriallize, 'SQLite objects created in a thread can only be used in that same thread.: by commenting out 'print session.query(Puppy).first().date_birth'
4. serializing datetime.date object: http://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable-in-python
5. errors in commented out code <!-- --> can cause error msgs, too.

sqlalchemy.exc.IntegrityError: (IntegrityError) UNIQUE constraint failed: puppie?? try solving by removing redundant import puppypopulator at manyPuppies.py: worked.

After implementing all-inclusive puppies route, get this:'AssertionError: View function mapping is overwriting an existing endpoint function:puppies': just means that I am reusing the same function name (or view name) puppies.

connecting angular to database: http://stackoverflow.com/questions/19758213/using-database-in-angularjs-where-should-i-write-db-connection-code

After adoptPuppy, gets BuildError: ('adoptPuppy', {'id': 2}, None) even trying to run /puppies/. JSOn still works.Naming of endpoint methods did not match between .html and .py.

For error msg 'Method is not allowed': because I did not say methods =['POST', 'GET'] in def.

Including bootstrap.css.min messes up dropdown . ?

ValueError: View function did not return a response: need 'return'

How To Deploy a Flask Application on an Ubuntu VPS:https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
----

Try to deploy with mod-wsgi: did not succeed

At /c/Users/Treefish: sudo apt-get install libapache2-mod-wsgi python-dev
then: sudo a2enmod wsgi
mkdir so that now we have /c/Users/Treefish/var/www
pip install flask to address flask not a
do 'sudo easy_install sqlalchemy'at treefish level dir
add 'pip install sqlalchemy' in pg_config.sh

------
try cgi:
1. create the following:

#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from yourapplication import app

CGIHandler().run(app)

as file finalProject.cgi, in the same directory as all the other files;

2. add 'ScriptAlias /app C:/Users/Treefish/fullstack/vagrant/finalProject.cgi'(my interpretation to the required 'ScriptAlias /app /path/to/the/application.cgi') to the top of pg_config.sh file

3.then run the app at the directory where the finalProject.py is, by doing: python finalProject.py: still get 'ImportError: No module named sqlalchemy'
4. append 'pip install sqlalchemy' to the end of 'pip install' statements in pg_config.sh
5. repeat the run as step 3 and got the same error.

6.on hosting:https://discussions.udacity.com/t/project-3-web-hosting/17083

7.downloaded google go app engine to treefish/desktop/

https://developers.google.com/+/web/share/interactive

https://developers.google.com/api-client-library/javascript/features/authentication

https://developers.google.com/identity/sign-in/web/sign-in

https://console.developers.google.com

https://my.hostmonster.com/cgi/home

8.at hostmonster/host cpanel: FTP accounts allow you to access your website’s files through a protocol called FTP. Use a third-party FTP program to access your files. To log into your account via FTP, enter “onetreefish.com” as your FTP host, the username, and password.

9.Try heroku:
https://devcenter.heroku.com/articles/getting-started-with-python#introduction, follow:

10.at vagrant$: do 'pip install virtualenv': Successfully installed virtualenv-13.1.2
install toolbelt? Why install git?
Python’s dependency manager, Pip.:
Deploy with heroku: install toolbelt; heroku login;cd to proj dir e.g. cd python-getting-started; heroku create <appname>; virtualenv venv;venv\Scripts\activate.bat: got "bash: venvScriptsactivate.bat: command not found"
12.on 12/15: I did this time at the git prompt: @Treefish (master #) ~ $ heroku login and followed along <https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app>; same error as before!
deleted from requirement.txt.: gunicorn==19.3.0
http://oauth.net/2/
13.explanation of how python apps gets access to server:https://developers.google.com/api-client-library/python/guide/aaa_oauth

14.quick start for flask:http://flask.pocoo.org/docs/0.10/quickstart/:the data a client sent to the server.. In Flask ... is provided by the global request object.The current request method is available by using the method attributee.g.:if request.method == 'POST';To access parameters submitted in the URL (?key=value) you can use the args attribute:,e.g.searchword = request.args.get('key', '')

15.http://stackoverflow.com/questions/13437446/how-to-display-selected-item-in-bootstrap-button-dropdown-title
simle:https://aaronparecki.com/articles/2012/07/29/1/oauth2-simplified

16.https://developers.google.com/identity/, go to Guide/Google Sign-In for server-side apps
17.button: https://developers.google.com/+/web/+1button/#jsapi
18.what is going on: https://discussions.udacity.com/t/can-someone-pelase-explain-highlevel-what-is-going-on-here-i-feel-i-copied-the-code-without-really-understanding-what-went-on-there/21115/2
flask & Alchemy: http://stackoverflow.com/questions/14343740/flask-sqlalchemy-or-sqlalchemy
many-to-many: http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
easy-to-understand requests of python:http://docs.python-requests.org/en/latest/user/quickstart/

19.found misspelled- 'singInCallback' and '#singInButton'!
20.5xx are the codes related to Server error.This is not related to client and the fault is in the webpage/website requested that resides on server.
 for not redirecting: raise FormDataRoutingRedirect(request) , it was redirected to:

  http://localhost:5000/login/#

  auth2.signOut(): why do gdisconnect?
  a similar probelm of automatic sign-in: http://stackoverflow.com/questions/32624007/initiate-google-sign-in-on-button-click
  my redirect should be ...gconnect, right?
  ;
  Migrate a hybrid server-side flow
  21.12/18: address favicon'
  to_json vs json.dump():
  22.Class OAuth2Credentials：to_json, from_json is python methods: https://google-api-python-client.googlecode.com/hg/docs/epy/oauth2client.client.OAuth2Credentials-class.html
  'We can see this object by inspecting the __table__ attribute:

23.>>> User.__table__ ' at http://docs.sqlalchemy.org/en/latest/orm/tutorial.html: where to type to get response?: after 'python database_setup.py', get '2015-12-20 21:46:13,413 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("condition") etc.'
24.app.js does not work:no background of fishes!
25.snow with keyframe: http://designshack.net/articles/css/make-it-snow-on-your-website-with-css-keyframe-animations
snow with jQuery plugin: http://www.somethinghitme.com/2011/10/05/jquery-snowfall-1-5-update-now-with-snow-buildup/
download paint.net to do transparent background, not transparent, th efirst laer is blocking the others.

26.After I added a new column 'description' to class REstaurant, the restaurants page did not render, and complains"no column description'. I deleted the restaurantMenu.db file, and ran 'python database_setup, python manyRestaurants.py' before running 'python final_project.py. It then rendered!  But the new data added were lost!

27.how to populate: http://stackoverflow.com/questions/3538322/many-to-many-data-structure-in-python', no 'ON DELETE CASCADE- so that records referring to a book or author that gets deleted are automatically dropped in turn':menu and condition association is casual, each independent.

how to populate many-to-many:http://stackoverflow.com/questions/25668092/flask-sqlalchemy-many-to-many-insert-data
http://stackoverflow.com/questions/12593421/sqlalchemy-and-flask-how-to-query-many-to-many-relationship

28.TODO: The browser (or proxy) sent a request that this server could not understand.at condition Edit

TODO: menu view for conditions work for Constipation and diabetes but not for gray hair. ??

29.details of oauth2.0: https://tools.ietf.org/html/rfc6749
30. TODO: add new menu Taco Soup,for condition Costipation, appeared 3 times, with restaurant id as '' , 3 ,and 4.
31.TODO: login the app, and then do gdisconnect, shows 'user not connected' if in incognito mode; otherwise: 'failed to revoke token';

32.After adding User class and adding user_id to class Restaurant, MenuItem and Condition, after running python database.setup and manyRestaurants, get this :(OperationalError) table restaurant has no column named user_id u'INSERT INTO restaurant (name, description, user_id) VALUES (?, ?, ?)' ('steam', 'all things steamed', None): similar to problem 26:delete old database file;
33: TODO: it looks like I am loggout while I am logged in. can not find 'login_session["user_id"]''
34:FB app register. Therapeutic Foods, in health and wellness category
TODO: tell app about FB login.
35: dumps vs jasonify: http://stackoverflow.com/questions/7907596/json-dumps-vs-flask-jsonify
data = {"id": str(album.id), "title": album.title}
json.dumps(data): [{"id": "4ea856fd6506ae0db42702dd", "title": "Business"}]
flask.jsonify(**data)
flask.jsonify(id=str(album.id), title=album.title)
36: FB Graph API v2.5: https://developers.facebook.com/docs/graph-api
TODO: FB or even g disconnect not working; debug FB connect: login_session not session; concat str with str, not int-convert by str(int);
37: TODO: need public condition view?
38: to add RSS endpoint: pip install feedparser (exit vagrant first)
to add xml endpoint: pip install dict2xml
39:register Therapeutic Foods at Imgur, with http://localhost:5000 as app url, and http://localhost:5000/oauth2callback as redirect url. Warning: should use https
per https://api.imgur.com/:
pip install imgurpython:Successfully installed imgurpython-1.1.6, per https://github.com/Imgur/imgurpython
https://github.com/Imgur/imgurpython/blob/master/examples/auth.py
ImportError: No module named imgurpython
[1/27/2016: add 'pip install imgurpython' in pg_config.sh per Ben at Forum; fagrant up, vagrant ssh, python auth.py]
examples of using imgur: https://github.com/Imgur/imgurpython/blob/master/examples/upload.py
40.TODO: TypeError: showMenus() takes exactly 1 argument (0 given)?
41: TODO: NoResultFound: for one() for showMenu: delete owner fixed it!
42: trouble deploying at heroku, study https://devcenter.heroku.com/articles/git
Build suceeded, but 'https://powerful-woodland-2492.herokuapp.com/' 'error code=H14 desc="No web processes running,status=503...' have to do "heroku ps:scale web=1", then 'heroku ps:restart'
flash message one screen behind!
An error occurred in the application and your page could not be served. Please try again in a few moments.

If you are the application owner, check your logs for details.
'netstat -a' for the list of active ports

help on heroku: https://devcenter.heroku.com/articles/heroku-local
heroku login
echo "web: python finalProject.py" > Procfile
heroku create
git push heroku master
heroku ps:scale web=1:Scaling dynos... failed;!    No app specified.!    Run this command from an app folder or specify which app to use with --app APP; fork() function is unimplemented on this machine (NotImplementedError)
herolu open

43: TODO:psycopg2==2.5.3 added to requirements, 'pip install -r requirements.txt', got '31mCommand "python setup.py egg_info" failed with error code 1 in c:\users\treefish\appdata\local\temp\pip-build-v26ro9\psycopg2←[0m'

web: python finalProject.py runserver 0.0.0.0:5000 changed to :
web: python manage.py runserver 0.0.0.0:$PORT: run 'heroku local':starting web.1 on port 5000;web.1  | Traceback (most recent call last):TODO??
1/14/2016: install google cloud sdk by GoogleCloudSDKInstaller.exe(795kb);
 install GoogleAppEngine-1.9.30.msi(53.7Mb) to C:\Program Files (x86)\Google\google_appengine\

 Treefish (dev *) fullstack $ git clone https://github.com/udacity/ud858.git
 44. 1)In /fullstack at git bash, create /helloworld;
 2)make helloworld.py and app.yaml and save in /helloworld
 3)at /fullstack at git bash, do 'dev_appserver.py helloworld/',[ says the current Cloud SDK version is: 92.0.0, need to install gcloud app Python Extensions, version 1.9.30, update done!]
 4)http://localhost:8000 now runs the app !
 5)create project at console.google.developer, project name helloworld, project id helloworld-1191.
 6) appcfg.py -A helloworld-1191 update helloworld/: "The authentication flow has completed."
 7)The full URL for your application is http://helloworld-1191.appspot.com/
 45: best beginning flask deployment tutorial:https://exploreflask.com/deployment.html
 46: a good book on python: http://www.jeffknupp.com/blog/2013/11/29/improve-your-python-decorators-explained/
 47 deploy la-cita: https://la-cita.appspot.com/
 48: try to delete la-cita folder inside Lesson2/000, says"action can not be complated, open in another program..."
 49: Remove project. then change version number/file/add existing project/add/run/deploy:then change code, no need to do run again.
 50: implement saveProfile endpoint,got ": __init__() takes exactly 3 arguments (2 given). I created a resourceContainer subclass to be used as the request object, while model's ProfileMiniForm(messages.Message) should be used instead.
 51: After deploying at Google App Engine LAuncher, no need to repeat deploymnet; any change in code is automatically reflected at the api explorer.
"!
52:Deploy by git bash: 0)Create new project at google console developer, app id as lesson2-conf
1) change WEB_CLIENT_ID = 'lesson2-conf' at settings.py;
2)change application: lesson2-conf at app.yaml;
3) per 44. do dev_appserver.py 00_Conference_Central/, front end works;
4) do: appcfg.py -A lesson2-conf update 00_Conference_Central/, success!lesson2-conf/_ah/api/explorere leads to https://apis-explorer.appspot.com/apis-explorer
53: https://cloud.google.com/appengine/docs/python/gettingstartedpython27/usingdatastore
54: entities not saved: the problem was that I updated lesson 3 conference.py file, but not the Lesson3 yaml and app.js file with Web client id, and I was running the apps from Lesson 3 folder; I went back to lesson 2 changed the conference.py, and give a new app name at yaml(lesson-conf), and the entities showed up!
55. TODO: /_ah/spi/ConferenceApi.saveProfile:id_token verification failed: Token is not an id_token (Wrong number of segments)
http://stackoverflow.com/questions/16661109/google-endpoints-api-chrome-extension-returns-none-for-endpoints-get-current-u
56. http://alextechrants.blogspot.co.uk/2013/11/10-common-stumbling-blocks-for.html
57. jenja2 and angular:http://stackoverflow.com/questions/30362950/is-it-possible-to-use-angular-with-the-jinja2-template-engine
