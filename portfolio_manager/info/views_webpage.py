from info.serializers import ContentWebPageSerializer
from info.models import ContentWebPage

#for rendering in html
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def page_not_found_view(request, exception):
    return render(request,'404.html',status=404)



def my_view_lang(request,lang):

    #finding name "navbarlinks" in models to find, which pages we are going to show
    navbarlinks_name:str = "navbarlinks"

    
    navbarlinks_model:ContentWebPage = get_object_or_404(ContentWebPage,name=navbarlinks_name,language=lang)
    navbarlinks:dict = ContentWebPageSerializer(navbarlinks_model).data

    pages:list [str] = list(navbarlinks['content'].keys())

    nav_names:dict = {

    }

    nav_names["nav"]=navbarlinks["content"]

    context = {
        page:"" for page in pages
    }

    for page in pages:
        content_page:dict = ContentWebPage.objects.filter(name=page,language=lang).values().first()
        if content_page:
            context[page] = content_page
            
    #merging two dicts
    context = context | nav_names
    return render(request, "index.html", context)



def my_view_lang_en(request):

    return my_view_lang(request,lang="en")

def my_view_lang_pl(request):

    return my_view_lang(request,lang="pl")

