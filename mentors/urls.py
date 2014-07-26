from django.conf.urls import patterns, url
from .views import MentorsView, CompaniesView, DegreesView, IndustriesView, SearchView

urlpatterns = patterns('todo.views',

    url(r'^mentors$', MentorsView.as_view()),
    url(r'^degrees$', DegreesView.as_view()),
    url(r'^industries$', IndustriesView.as_view()),
    url(r'^companies$', CompaniesView.as_view()),
    url(r'^search$', SearchView.as_view()),
)