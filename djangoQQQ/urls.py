from django.conf.urls import url,include
from django.contrib import admin

from resume.views import myResumeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),

    url(r'^resume$', myResumeView.as_view(), name='resume'),

]