# -*- coding:utf-8 -*-

from django.db import models


# Create your models here.


class Asn(models.Model):
    """
    Table de stock des ASN 
    """
    name = models.CharField(max_length=150, verbose_name="ASN", unique=True)
    code = models.IntegerField(verbose_name="Code ASN", unique=True)


class IP(models.Model):
    """
    table de stock des IP 
    """
    ipv4 = models.CharField(max_length=100, verbose_name="Adresse ipv4", unique=True)
    ipv6 = models.CharField(max_length=100, verbose_name="Adresse ipv6", blank=True, unique=True)


class Infection(models.Model):
    """
    tables des infections(les virus)
    """
    name = models.CharField(max_length=150, verbose_name="Nom su virus", unique=True)


class GroupFile(models.Model):
    """
    les dossiers zipper
    """
    name = models.CharField(max_length=200, verbose_name="Nom du dossier")
    url = models.CharField(max_length=200, verbose_name="Chemin du dossier")


class FileZip(models.Model):
    """
    fichier csv
    """
    name = models.CharField(max_length=200, verbose_name="Nom du dossier")
    url = models.CharField(max_length=200, verbose_name="Chemin du dossier")
    groupFile = models.ForeignKey(GroupFile, related_name="filezips", on_delete=models.PROTECT)


class LineFileZip(models.Model):
    """
    ligne du fichier csv
    """
    # asn = models.IntegerField()
    # ip = models.CharField(max_length=100)
    # infection = models.CharField(max_length=100)

    infection = models.ForeignKey(Infection, on_delete=models.CASCADE, related_name="linefilezips")
    ip = models.ForeignKey(IP, on_delete=models.CASCADE, related_name="linefilezips")
    asn = models.ForeignKey(Asn, on_delete=models.CASCADE, related_name="linefilezips")

    fileZip = models.ForeignKey(FileZip, related_name="linefilezips", on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    port = models.IntegerField()
    geo = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    hostname = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    agent = models.CharField(max_length=200)
    ic_ip = models.CharField(max_length=100)
    ic_port = models.IntegerField()
    ic_asn = models.IntegerField()
    ic_geo = models.CharField(max_length=50)
    ic_dns = models.CharField(max_length=100)
    count = models.IntegerField()
    proxy = models.CharField(max_length=100)
    application = models.CharField(max_length=50)
    p0f_genre = models.CharField(max_length=50)
    p0f_detail = models.CharField(max_length=50)
    machine_name = models.CharField(max_length=50)
    id1 = models.IntegerField()
    naics = models.IntegerField()
    sic = models.IntegerField()
    cc_naics = models.IntegerField()
    cc_sic = models.IntegerField()
    sector = models.CharField(max_length=100)
    cc_sector = models.CharField(max_length=100)
    ssl_cipher = models.CharField(max_length=100)
    family = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    public_source = models.CharField(max_length=100)


class Imap(models.Model):
    """
    table de connexion au compte schadow
    """
    url = models.CharField(max_length=50)
    port = models.IntegerField()
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
