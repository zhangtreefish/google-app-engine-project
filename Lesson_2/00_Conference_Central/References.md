# **Debuggings**

1. My initial roadblock was inability to truely launch the application from
   Google App Engine (GAE) Launcher, instead I got a "hello world!' default page. The
   right way is to
   -- make sure there is no other app in the launcher
   -- click 'File/Add Existing Application' tab, and
   -- 'browse' to the folder 00_Conference_Central (where the conference
      project is),  click "Add'.
2. The next hurdle was that the google login suspended, my email acknowledged
   in the flash but with the loading icon circling forever. The error message
   was 'can not find property getProfile of undefined'. Using log information
   provided by the GAE launcher, I tried to
   -- initiate some client ids in settings.py
   -- and remove userId for Profile class in models.py
   -- rm models.pyc
   -- rm settings.pyc
   -- refresh app page: login page worked!


# **Helpful Sites**
1. https://github.com/carwin/markdown-styleguide