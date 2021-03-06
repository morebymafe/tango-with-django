import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'TWDproject.settings')

import django
django.setup()
from rango import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 128},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 8},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views": 32}
    ]

    django_pages = [
        {"title": "Official django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 64},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 16},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 4}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "bottlepy.org/docs/dev/",
         "views": 2},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 2}
    ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}}

    # End of dictionaries

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    # Print out the categories we have added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(">> {0} ~ {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
