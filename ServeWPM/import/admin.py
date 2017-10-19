# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

__all__ = [
    ImportCrawl,
    ImportCrawlHistory,
    ImportFlashCookie,
    ImportHttpRequest,
    ImportHttpResponse,
    ImportLocalstorage,
    ImportProfileCookie,
    ImportSiteVisit,
    ImportTask,
    ImportXpath,
]
#     HttpRequestCookie,
#     HttpResponseCookie,

# Register your models here.
for m in __all__:
    admin.site.register(m);
