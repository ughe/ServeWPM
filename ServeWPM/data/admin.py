# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

__all__ = [
    Crawl,
    Crawlhistory,
    FlashCookie,
    HttpRequest,
    HttpResponse,
    Localstorage,
    ProfileCookie,
    SiteVisit,
    Task,
    Xpath,
]
#     HttpRequestCookie,
#     HttpResponseCookie,

# Register your models here.
for m in __all__:
    admin.site.register(m);
