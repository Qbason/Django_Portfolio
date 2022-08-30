from multiprocessing import context
from info import serializers

from info.models import ContentWebPage


#for rendering in html
from django.shortcuts import render

def my_view_lang(request,lang):

    pages = ["whoami","cv","contact"]
    lang_dict = {
        "en":{
                "whoami":"Whoami?",
                "cv":"CV",
                "contact":"Contact",
            },
        "pl":{
                "whoami":"Kim jestem?",
                "cv":"CV",
                "contact":"Kontakt"}
        }
    nav_names = {

    }
    nav_names["nav"]=lang_dict[lang]
    context = {
        page:"" for page in pages
    }
    print(nav_names)

    for page in pages:
        content_page = ContentWebPage.objects.filter(name=page,language=lang).values().first()
        if content_page:
            context[page] = content_page

    context = context | nav_names
    return render(request, "index.html", context)


def my_view_lang_en(request):

    return my_view_lang(request,lang="en")

def my_view_lang_pl(request):

    return my_view_lang(request,lang="pl")

