# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Crawlhistory(models.Model):
    crawl = models.ForeignKey('Crawl', on_delete=models.PROTECT)
    command = models.TextField()
    arguments = models.TextField()
    bool_success = models.IntegerField()
    dtg = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'CrawlHistory'


class Crawl(models.Model):
    task = models.ForeignKey('Task', models.PROTECT)
    browser_params = models.TextField()
    screen_res = models.TextField()
    ua_string = models.TextField()
    finished = models.BooleanField()
    start_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'crawl'


class FlashCookie(models.Model):
    crawl = models.ForeignKey('Crawl', on_delete=models.PROTECT)
    visit = models.ForeignKey('SiteVisit', on_delete=models.PROTECT)
    domain = models.CharField(max_length=500)
    filename = models.CharField(max_length=500)
    local_path = models.CharField(max_length=1000)
    key = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'flash_cookies'


class HttpRequest(models.Model):
    crawl = models.ForeignKey('Crawl', on_delete=models.PROTECT)
    visit = models.ForeignKey('SiteVisit', on_delete=models.PROTECT)
    url = models.TextField()
    top_level_url = models.TextField()
    method = models.TextField()
    referrer = models.TextField()
    headers = models.TextField()
    is_xhr = models.NullBooleanField(db_column='is_XHR')  # Field name made lowercase.
    is_frame_load = models.NullBooleanField()
    is_full_page = models.NullBooleanField()
    is_third_party_channel = models.NullBooleanField()
    is_third_party_window = models.NullBooleanField()
    triggering_origin = models.TextField()
    loading_origin = models.TextField()
    loading_href = models.TextField()
    req_call_stack = models.TextField()
    content_policy_type = models.IntegerField()
    post_body = models.TextField()
    time_stamp = models.TextField()

    class Meta:
        managed = False
        db_table = 'http_requests'


class HttpResponse(models.Model):
    crawl = models.ForeignKey('Crawl', on_delete=models.PROTECT)
    visit = models.ForeignKey('SiteVisit', on_delete=models.PROTECT)
    url = models.TextField()
    method = models.TextField()
    referrer = models.TextField()
    response_status = models.IntegerField()
    response_status_text = models.TextField()
    is_cached = models.BooleanField()
    headers = models.TextField()
    location = models.TextField()
    time_stamp = models.TextField()
    content_hash = models.TextField()

    class Meta:
        managed = False
        db_table = 'http_responses'


class Localstorage(models.Model):
    crawl = models.ForeignKey('Crawl', on_delete=models.PROTECT)
    page_url = models.CharField(max_length=500)
    scope = models.TextField()
    key = models.TextField(db_column='KEY')  # Field name made lowercase.
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'localStorage'


class ProfileCookie(models.Model):
    crawl = models.ForeignKey('Crawl', on_delete=models.PROTECT)
    visit = models.ForeignKey('SiteVisit', on_delete=models.PROTECT)
    basedomain = models.TextField(db_column='baseDomain')  # Field name made lowercase.
    name = models.TextField()
    value = models.TextField()
    host = models.TextField()
    path = models.TextField()
    expiry = models.IntegerField()
    accessed = models.IntegerField()
    creationtime = models.IntegerField(db_column='creationTime')  # Field name made lowercase.
    issecure = models.IntegerField(db_column='isSecure')  # Field name made lowercase.
    ishttponly = models.IntegerField(db_column='isHttpOnly')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profile_cookies'


class SiteVisit(models.Model):
    crawl = models.ForeignKey('Crawl', on_delete=models.PROTECT)
    site_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'site_visits'


class Task(models.Model):
    start_time = models.DateTimeField()
    manager_params = models.TextField()
    openwpm_version = models.TextField()
    browser_version = models.TextField()

    class Meta:
        managed = False
        db_table = 'task'


class Xpath(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    xpath = models.CharField(max_length=500)
    absolute_xpath = models.CharField(max_length=500)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'xpath'
        unique_together = (('name', 'url'),)
