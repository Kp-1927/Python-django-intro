from django.urls import path
from .views import test_api,test_json_api,test_html_page,test_hello_name,test_html_for_page,home_page,about_page

urlpatterns=[
    path("test-api/",test_api,name="test_api"),
    path("test-json-api/",test_json_api,name="test_json_api"),
    path("test-html-page/",test_html_page,name="test_html_page"),
    path("test-html-for-page/", test_html_for_page, name="test_html_for_page"),
    path("test-hello-name/<name>",test_hello_name,name="test_hello_name"),
    path("home-page/",home_page,name="home_page"),
    path("about-page/",about_page,name="about_page")
]