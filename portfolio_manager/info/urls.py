from info import views
from info.views_webpage import my_view_lang,my_view_lang_en,my_view_lang_pl, robots_txt
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    r'contentwebpage',
    views.ContentWebPageViewSet
)

urlpatterns = [
    path("",my_view_lang_en,name='index'),
    path("pl",my_view_lang_pl,name='lang_pl'),
    path("en",my_view_lang_en,name='lang_en'),
    path("api/",include(router.urls)),
    path("robots.txt",robots_txt)
]
