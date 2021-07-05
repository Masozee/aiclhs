from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

# Create your models here.
class Event(models.Model):
    Judul = models.CharField(max_length=100)
    Slug = models.SlugField(default='', editable=False, max_length=140)
    Mulai = models.DateTimeField()
    Selesai = models.DateTimeField(blank=True)
    Lokasi = models.TextField(blank=True)
    Link = models.URLField(blank=True)
    Keterangan = models.TextField(blank=True)

    def __str__(self):
        return self.Judul

    class Meta:
        verbose_name = ("Acara")
        verbose_name_plural = ("Acara")

    def save(self, *args, **kwargs):
        value = self.Judul
        self.Slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def waktu(self):
        return self.Mulai.strftime('%d-%B-%Y')
               

class Pembicara(models.Model):
    Nama = models.CharField(max_length=100)
    Slug = models.SlugField(default='', editable=False, max_length=140)
    Pekerjaan = models.CharField(max_length=100)
    Deskripsi_singkat = models.TextField(blank=True)
    Foto = models.ImageField(upload_to='web/')
    Email = models.EmailField(blank=True)
    Facebook = models.URLField(blank=True)
    Twitter = models.URLField(blank=True)
    Linkedin = models.URLField(blank=True)
    Instagram = models.URLField(blank=True)
    Keterangan = models.TextField(blank=True)

    def __str__(self):
        return self.Nama

    class Meta:
        verbose_name = ("Pembicara")
        verbose_name_plural = ("Pembicara")

    def save(self, *args, **kwargs):
        value = self.Nama
        self.Slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)            

class ListPembicara(models.Model):
    Acara = models.ForeignKey(Event, on_delete=models.PROTECT)
    Pembicara = models.ForeignKey(Pembicara, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.Acara) + ' - ' + str(self.Pembicara)

    class Meta:
        verbose_name = ("Daftar Pembicara")
        verbose_name_plural = ("Daftar Pembicara")       

class Artikel(models.Model):
    Judul = models.CharField(max_length=150)
    Slug = models.SlugField(default='', editable=False, max_length=140)
    Tanggal = models.DateField(null=True)
    Isi = HTMLField()
    tags = TaggableManager()

    def __str__(self):
        return self.Judul

    class Meta:
        verbose_name = ("Artikel")
        verbose_name_plural = ("Artikel")

    def save(self, *args, **kwargs):
        value = self.Judul
        self.Slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)        