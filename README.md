#  INSTRUCTIONS : Build a Backend for a website with Django
*Note : You have to install Python first and then follow the commands to set up a Django project. In this project, I run on Pycharm. If not sure, you can learn Django before starting this project. Please read the code Hade and the instructions at the same time, so you can have better comprehension* 
##### Step 1 : Create app  "Home" in Django and add static files .. ####
- We will arrange it like this :
    + Src folder (the root directory of the project)
    + core : code for core applications
    + public :
      + apps
      + media : contains photos 
      + static : remember to load static first
      + templates : This folder includes 3 important things. One is home folder to contain all of your html file. One is product folder to contain the details each of items. The last one is "base.html" file which will be a template for every page of website
- Run this command to add static files : `python manage.py collectstatic`

To understand "static" file can visit the official django website : [static files (images, JavaScript, CSS) in detail] (https://docs.djangoproject.com/en/4.2/howto/static-files/)

##### Step 2 : Add the app in settings.py #####

   - Look at the line "INSTALLED_APP" and add one more line below `    'django.contrib.staticfiles',
` : it means that you already add static file for the app.
  - Declare the app if you want to move to the app by writing down the code `src.public.apps.home.apps.HomeConfig` : This is because we already custom the app, so we need to use the component `HomeConfig`. If you do not custom the app, you just need to add the name of the app.

##### Step3 : Add the path to the app and static file in urls.py #####

(*) remember to import these functions first :

    from django.urls import path,include
    from django.conf.urls.static import static
    from django.conf import settings

(*) and then you add the path. However, remember to type only some of the first letters and then enter to print it out. Do not type by yourself

`    path('', include('src.public.apps.home.urls'), name="app-home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
`
 ##### Step 4 : Django's app configuration  #####

 Let's break down each part :
 
`from django.apps import AppConfig`
AppConfig is configuration application from django.apps module.

`class HomeConfig(AppConfig)`
This class we define configuration for app "home".
The name "HomeConfig" is arbitrary and inherits "AppConfig".

`    default_auto_field = 'django.db.models.BigAutoField'
`
- default is default
- auto_field is a series of integer-based primary key which will increments when having new records.
- BigAutoField is a 64-bit integer. It usually uses when you need a large range of values.

##### Step 5 : Create base.html under templates folder and write the code for it  #####

- This one a common template using for every page of website. In this 
project, the menu on top and the animation including details below will be 
used in all html file, all pages of the website. 
Therefore, we will use these two code lines `{% block content %} {% endblock content %}` in the middle of base.html file to add contents of other html files here
- Remember to add `{% load static %}` to apply css or js to html
- It is compulsory to take note that we should change all href src to the format `src="{% static 'its name' %}""`


##### Step 6 : Add something in views.py to handle http response #####

+ Views to make it possible for your web application to properly process requests and return the most accurate responses
+ Take note : remember to import View from django.views. This is a HTTP method to handle with user requests, having 4 main methods ((e.g., GET, POST, PUT, DELETE))
  + We have 2 ways to define views in Django :
      - function-based views : I seldom see coder using this one for big website because this way often uses for simple website. It is basic processing and rendering
      - class-based views : I usually see coder using this one because it involves more structure for handling complex scenarios.
  + Now, we together break down these code lines :

```python
    class Homeview(View):
       def get(self,request):
            return render(request=request,template_name="home/index.html")
```

   + Later, we will add more classes such as classes for products or login.
   + We class instead of def to help us add more subclass or inheritance ect..

##### Step 7 : OKAY, Let's start to custom other HTML files #####
+   Do you remember we code the line `{% block content %} {% endblock content %}` in base.html file?
    
    --> Correct ! Now, we will insert this html content to that place.
+ You just need to follow the format :
    ```python
    {% extends 'base.html' %} #call to base.html file
    {% load static %} #call static file to add its css or js for html
    {% block title %}HADES SINGAPORE{% endblock title %} #Title for the page
    {% block content %}
        #please place your content here
    {% endblock content%}
  ```
##### Step 8 : Let's add database in models.py  #####
 * Explain : models.py will help owners add and manage their products. For instance, owners of the shop will add one more stock or fix something. 
 * You should fully comprehend the concept of foreign key in SQL to do this. There is a website to show you how it works [W3 School](https://www.w3schools.com/sql/sql_foreignkey.asp). 
 * Okay !! Now, you already know that foreign key is child table and primary key is parent table

 ##### So, which one will be the child table in this project and vice versa ? #####
   
Now, you should image a vast tree with so numerous branches, and one of them either sprouts more child branches or not. Regarding with the strong main branches without sprouting more, we call it primary key. Meanwhile, child branches will serve as foreign key.


Similarly, we will divide elements for child table and parent table for our shop like that. Child table is foreign key and parent table is primary key.

![git version](./media/container-img/a.png)

##### Do you know why "size" is foreign key ? #####

 => Due to consistency, currently admin number 1 add the size named "S", and later admin number 2 add "size" called "Small". As a result, it creates DISCREPANCIES and VARIATIONS in size name. Meanwhile, element "title", for instance, can be different and no need to be consistent. 

- One more thing, you should incorporate __ str__(self) for foreign key 

```python
   def __str__ (self):
       return self.size
```

=> When customers click "Size" category to pick, it will show all options that we already set default (S,M,L,XL). Without __ str__, it will indicate nothing when consumers click it.


##### Step 9 : Of course ! We'll move immediately to admin.py after adding models #####

Why ? This is because admin interface serves as a tool for model  !

- Firstly, you import admin library `from django.contrib import admin`
- Secondly, you import your models by `from src.public.apps.home.models import *` . 
 
*Take note* : to call "models" file, you type "src" and then press enter, choosing the correct one to  make sure exactly. You are no need type by yourself. The component "*" means ALL, and collect ALL in models.py in this case.

##### STEP 10 : How to register our models ? how the code looks like ?    #####

For example :

```python
    class SizeAdmin(admin.ModelAdmin):
        list_display = ['size']
```
=> create class named "SizeAdmin" to manage size category. This class will inherit form `admin.ModelAdmin`. Additionally, `list_display` will display 'size' objects in size field.

##### Next, we define which content will be displayed. OKayy ! Let's go to views.py in app "home"   #####

(^.^) Explain : users click button "Log in", and it will move to Log in page. User clicks the button "T shirt", and it will indicate T-shirt products page. Therefore, our mission in views.py in app "home" is that initialize and code to join models and url correctly.
Due to so many items in this shop, I will go through 3 urls. So, you can follow and code others similarly.

- Firstly, we need to import all essential libraries

The most imperative library, it's compulsory to import in views.py : 

`from django.views import View` => For each View, it is your responsibility to initialize, add database, and return an HttpResponse. 

and then : 

`from django.http import HttpResponse` => return HTTP response 

next :

`from django.shortcuts import render` => render() allows combining available template HTML and one more paragraph to return HttpResponse suitable.

additionally :

`from .models import Items, Img` => We import Items and Img models from models.py

- Secondly, we will code the two easiest functions that is for LOG IN and Home page :

```python
    class Homeview(View):
        def get(self,request):
          return render(request=request,template_name="home/index.html")
```
```python
    class Login(View):
        def get(self, request):
             return render(request=request, template_name="home/login-index.html")
```


+ The first one, GET method, when users click to the register button, for instance, it returns the register template (HTML). This is because the GET method will take data from server.

+ The second one, POST method, when users already filled in their information and press the button register, that information will be sent to database. This is because the POST method will handle a request sent to server.

=> `class HomeView/Login (View)` class named HomeView/Log inherits View from Django's views module.`def get(self,request)` it calls method GET to handle HTTP. `self` indicates that this is the instance of the class. Other languages do not require "this" or "self", but Python requires. `request`,a module of Python, holds HTTP request data, so you can find more detail in Python lessons. 
`return render(request=request, template_name="home/login-index.html")` it renders an HTML template `home/login-index.html` and returns it as an HTTP response.

- Next, we will define view page for one of our products in our shop. There is a wide array of items, so I will select one to explain as an example for you. I opt to deal with the url for Footwear category. 

```python
    class Footwear(View):

    def get(self,request):
        context = {
            'products': Items.objects.all()
        }

        # test code
        products = Items.objects.all()
        for item in products:
            print(item.img_set.first().img.url)
        return render(request=request,template_name="home/product.html", context=context)
```
=> Explain : 

`context` is a dictionary with key `product` containing all items which admin added by using the queryset `Items.objects.all()`. This one holds all instances from model Items.

Everyone know about the loop "for" in Python ? Yes, `for item in products` exactly what it is. We will return each objects from `products`

`print(item.img_set.first().img.url)` : let's break down each component with me

(1)`img_set` followed by the formula `model-name_set`. If you have foreign key `img` in `Items` model that references to `Img` model, Django will create a reverse relationship manager when you set `modelname_set` => reverse lookup help you access to all instances of referencing model.

For example : A model named `McDonald's`and `Burgers`

![git version](.src/public/media/container-img/burger.jpg)

(2)`first()` to collect the first objects from `item.img_set`

(3)`img.url` to access the `url` attribute of instance `img` which associate with the image of each item.

`return render(request=request,template_name="home/product.html", context=context)` : let's break down each part with me

(1)`render` is provided by Django which takes (request objects, template name, a context dictionary)

(2) `request=request` : this one may be redundant because it just helps the code more explicit. The `render` function will consider it as an `argument`. It handles HTTP request objects and render suitable template for it. You can code `return render(my_request, template_name="home/product.html", context=context)`

(3)`template_name="home/product.html"` : it renders the template `home/products.html`

(4)`context=context` : the first letter `context` means dictionary. The second letter context is our dictionary we name it "context". As the code, this context dictionary with the key "products" will be passed to template to render the 

For example :

```python
from django.shortcuts import render

def burger_menu(request):
    burger = {
        'title': 'Beef Burger',
        'chef': 'Mr. Handsome',
        'price': 20,
    }

    context = {'list': burger}

    return render(request, 'burger_menu.html', context)

```

##### STEP 11 : SET UP URL FILE FOR INDIVIDUAL APP-LEVEL #####

hEY YOOO !! Welcome to `urls.py` within the "home" app directory. 

Firstly, let's import mandatory libraries :

`from django.urls import path` : urls must import path from url library of django
`from .views import *` : ' * ' in programming means ALL. We import EVERYTHING from `views.py`

After that, let's code urls patterns for function in `views.py`:

```python
    urlpatterns = [
    path('', Homeview.as_view(),name="index-file"),
    path('footwear/', Footwear.as_view(), name="product-file"),
    path('login/', Login.as_view(), name="login"),
]
```

Let me explain each part :

`'  ' ` : the first empty space, we will name it. This one will be url name on the web

`as_view()` : covert class-based view into a view function

`name = " "` : The name argument gives the URL pattern a name, which is important for reversing URLs in code and templates using the {% url% } HTML template. You link your html template with this url by this way "NAME".

##### QUESTION : *Now, I want it shows a text when users click to register button. What do you do ?* #####

---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
----------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------


                                ANSWER :
    
1) Accessing to login-index.html file, I will put register form into `form` tag
    ``` python
    <form action="done/" method="post" >
            //content//
    </form>
    ```
2) Before accessing to urls.py in your app to declare `done/`, you need to initialize class for that html (`login-index.html`) at views.py in the app :

    ```
   class Login(View):
    def get(self, request):
        return render(request=request, template_name="home/login-index.html")
   ```

3) Now, let's add url for that view :

Moving to urls.py in the app. We will link to that button url `done/` via View in `login-index.html`:

        path('done/', Login.as_view(), name="login-index.html"), 
    
DONE !!!


##### QUESTION : *I want to print out name of all users who already registered. What should I do?* #####

---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
----------------------------------- 5 minute thinking ------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------
---------------------------------- 5 minute thinking -------------------------------

`ANSWER: `

Similarly to the question before, we firstly create a function in views.py and then declare url in urls.py 

1) Code a function in class of that view from views.py for Login form :

```angular2html
class Register(View):
    def get(self, request):
        return render(request=request, template_name="home/login-index.html")
```

This is a fundamental class that defines the view for the Login HTML page. Next, we'll need to write the function to display the names and emails of users after they have registered.

So, what is that function ?

```python
        def post(self, request):
        try:
            name = request.POST['name1']
        except Exception as e:
            print(e)
            name = None

        try:
            email = request.POST['email']
        except Exception as e:
            print(e)
            email = None

        return HttpResponse(f"Name: {name} - Email: {email}")
```


We use " Except as e " instead of " Except" because it helps us print out the specific error what is it.

3) Make sure that we named href of "<a" tag to link to its url :

`					<a href ="{% url 'register-file' %}">Register  </a> `

Here, it names `register-file`

4) Yes, the last step always is declaration its name and url :

`    path('register/', Login.as_view(), name="register-file"),
`

Now, you will clearly understand the name function in the url path.
