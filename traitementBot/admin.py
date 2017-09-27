# -*- coding:utf-8 -*-

from django.contrib import admin

from .models import Asn, IP, Infection, GroupFile, FileZip, LineFileZip, Imap
# Register your models here.

admin.site.register(Asn)
admin.site.register(IP)
admin.site.register(Infection)
admin.site.register(GroupFile)
admin.site.register(FileZip)
admin.site.register(Imap)
admin.site.register(LineFileZip)