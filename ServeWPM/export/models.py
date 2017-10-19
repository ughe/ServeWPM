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
    crawl_id = models.IntegerField(primary_key=True)
    # crawl_id = models.IntegerField(blank=True, null=True)
    command = models.TextField(blank=True, null=True)
    arguments = models.TextField(blank=True, null=True)
    bool_success = models.IntegerField(blank=True, null=True)
    dtg = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CrawlHistory'


class Crawl(models.Model):
    id = models.IntegerField(primary_key=True, db_column='crawl_id')
    # crawl_id = models.IntegerField(blank=True, null=True)
    task = models.ForeignKey('Task', models.DO_NOTHING)
    browser_params = models.TextField()
    screen_res = models.TextField(blank=True, null=True)
    ua_string = models.TextField(blank=True, null=True)
    finished = models.BooleanField()
    start_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crawl'


class FlashCookies(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    crawl_id = models.IntegerField()
    visit_id = models.IntegerField()
    domain = models.CharField(max_length=500, blank=True, null=True)
    filename = models.CharField(max_length=500, blank=True, null=True)
    local_path = models.CharField(max_length=1000, blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flash_cookies'


class HttpRedirects(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    crawl_id = models.IntegerField()
    visit_id = models.IntegerField()
    old_channel_id = models.TextField(blank=True, null=True)
    new_channel_id = models.TextField(blank=True, null=True)
    is_temporary = models.BooleanField()
    is_permanent = models.BooleanField()
    is_internal = models.BooleanField()
    is_sts_upgrade = models.BooleanField()
    time_stamp = models.TextField()

    class Meta:
        managed = False
        db_table = 'http_redirects'


class HttpRequests(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    crawl_id = models.IntegerField()
    visit_id = models.IntegerField()
    url = models.TextField()
    top_level_url = models.TextField(blank=True, null=True)
    method = models.TextField()
    referrer = models.TextField()
    headers = models.TextField()
    channel_id = models.TextField()
    is_xhr = models.NullBooleanField(db_column='is_XHR')  # Field name made lowercase.
    is_frame_load = models.NullBooleanField()
    is_full_page = models.NullBooleanField()
    is_third_party_channel = models.NullBooleanField()
    is_third_party_window = models.NullBooleanField()
    triggering_origin = models.TextField(blank=True, null=True)
    loading_origin = models.TextField(blank=True, null=True)
    loading_href = models.TextField(blank=True, null=True)
    req_call_stack = models.TextField(blank=True, null=True)
    content_policy_type = models.IntegerField()
    post_body = models.TextField(blank=True, null=True)
    time_stamp = models.TextField()

    class Meta:
        managed = False
        db_table = 'http_requests'


class HttpResponses(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    crawl_id = models.IntegerField()
    visit_id = models.IntegerField()
    url = models.TextField()
    method = models.TextField()
    referrer = models.TextField()
    response_status = models.IntegerField()
    response_status_text = models.TextField()
    is_cached = models.BooleanField()
    headers = models.TextField()
    channel_id = models.TextField()
    location = models.TextField()
    time_stamp = models.TextField()
    content_hash = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'http_responses'


class Localstorage(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    crawl_id = models.IntegerField()
    page_url = models.CharField(max_length=500)
    scope = models.TextField(blank=True, null=True)
    key = models.TextField(db_column='KEY', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localStorage'


class ProfileCookies(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    crawl_id = models.IntegerField()
    visit_id = models.IntegerField()
    basedomain = models.TextField(db_column='baseDomain', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    expiry = models.IntegerField(blank=True, null=True)
    accessed = models.IntegerField(blank=True, null=True)
    creationtime = models.IntegerField(db_column='creationTime', blank=True, null=True)  # Field name made lowercase.
    issecure = models.IntegerField(db_column='isSecure', blank=True, null=True)  # Field name made lowercase.
    ishttponly = models.IntegerField(db_column='isHttpOnly', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profile_cookies'


class SiteVisits(models.Model):
    id = models.IntegerField(primary_key=True, db_column='visit_id')
    # visit_id = models.IntegerField(blank=True, null=True)
    crawl_id = models.IntegerField()
    site_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'site_visits'


class Task(models.Model):
    id = models.IntegerField(primary_key=True, db_column='task_id')
    # task_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    manager_params = models.TextField()
    openwpm_version = models.TextField()
    browser_version = models.TextField()

    class Meta:
        managed = False
        db_table = 'task'


class Xpath(models.Model):
    # id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    xpath = models.CharField(max_length=500)
    absolute_xpath = models.CharField(max_length=500, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xpath'
        unique_together = (('name', 'url'),)
