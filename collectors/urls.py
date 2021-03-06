"""collectors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from collectors.collection.urls import api_urls as collection_urls_api
from collectors.comments.urls import api_urls as comment_urls_api
from collectors.user.urls import api_urls as user_urls_api

urlpatterns = [
    url(r'^api/collection/', include(collection_urls_api, namespace='api.collection')),
    url(r'^api/comment/', include(comment_urls_api, namespace='api.comment')),
    url(r'^api/user/', include(user_urls_api, namespace='api.user')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')), 
]
