from django.db import models

class TalkLink(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    url = models.URLField()

    def __unicode__(self):
        return "%s" % self.name


class Conference(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
        return "%s" % self.name

class Talk(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    date = models.DateField()
    short_description = models.TextField()
    links = models.ManyToManyField(TalkLink, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.name
