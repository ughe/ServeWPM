# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

__all__ = [
    Crawl,
    Crawlhistory,
    FlashCookies,
    HttpRequests,
    HttpResponses,
    Localstorage,
    ProfileCookies,
    SiteVisits,
    Task,
    Xpath,
]
#     HttpRequestCookie,
#     HttpResponseCookie,

# Register your models here.
for m in __all__:
    admin.site.register(m);
