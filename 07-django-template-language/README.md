# VIEWS


### TO RUN

1. python3 -m venv venv

2. source venv/bin/activate

3. pip install -r requirements42.txt

4. python3 manage.py runserver
This will start the server locally. By default, the server will run at http://127.0.0.1:8000/.

#### Access Your Views in a Web Browser:

Now, you can visit the URLs you've defined for your views.

Go to http://127.0.0.1:8000/views/funky/ to see the result of the funky view.

Visit http://127.0.0.1:8000/views/danger/?guess=test for the danger view (this uses query parameters).

Try http://127.0.0.1:8000/views/game/?guess=test for the game view.

For the rest view, use http://127.0.0.1:8000/views/rest/test/.

Access http://127.0.0.1:8000/views/bounce/ to be redirected to https://www.dj4e.com/simple.htm.

#### Class-Based Views (CBVs):

For the class-based views (CBVs) like MainView and RestMainView, they are already mapped in urls.py:

http://127.0.0.1:8000/views/main/ for MainView

http://127.0.0.1:8000/views/restmain/test/ for RestMainView

6. deactivate
