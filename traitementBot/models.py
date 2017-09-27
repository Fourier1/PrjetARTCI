# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.


class Asn(models.Model):
    """
    Table de stock des ASN 
    """
    name = models.CharField(max_length=150, verbose_name="ASN")
    code =models.IntegerField(verbose_name="Code ASN")


class IP(models.Model):
    """
    table de stock des IP 
    """
    ipv4 = models.CharField(max_length=100, verbose_name="Adresse ipv4")
    ipv6 = models.CharField(max_length=100, verbose_name="Adresse ipv6")


class Infection(models.Model):
    """
    tables des infections(les virus)
    """
    name = models.CharField(max_length=150, verbose_name="Nom su virus")


class GroupFile(models.Model):
    """
    les dossiers zipper
    """
    name = models.CharField(max_length=200, verbose_name="Nom du dossier")
    url = models.CharField(max_length=200, verbose_name="Chemin du dossier")


class FileZip(models.Model):
    """
    entete du fichier csv
    """
    timestamp = models.DateTimeField()
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    asn = models.IntegerField(unique=True)
    geo = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    hostname = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    infection = models.CharField(max_length=100)
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


class User(models.Model):
    """
    la tables des utilisateurs
    """
    nom = models.CharField(max_length=50, verbose_name="Nom", help_text="Votre nom")
    prenom = models.CharField(max_length=100, verbose_name="Prenom")
    contact = models.CharField(max_length=8, verbose_name="Contact(s)")
    email = models.CharField(max_length=30, verbose_name="E-mail")
    adresse = models.CharField(max_length=30, verbose_name="Adresse")
    date_creation = models.DateField(auto_now_add=True, blank=True, verbose_name="Date de création")
    photo = models.ImageField(upload_to='images', default=0, verbose_name="Choisir une photo")

    def __str__(self):
        """
        description sur un nom du model
        :return: 
        """
        return '%s, %s' % (self.nom, self.prenom)


class Imap(models.Model):
    """
    table de connexion au compte schadow
    """
    url = models.CharField(max_length=50)
    port = models.IntegerField()
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
