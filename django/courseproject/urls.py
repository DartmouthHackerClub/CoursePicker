from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import courseapp.views
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^courseproject/', include('courseproject.foo.urls')),
    (r'^get_search/', courseapp.views.get_search),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
