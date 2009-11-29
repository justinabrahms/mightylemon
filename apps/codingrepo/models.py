from django.db import models

class CodeProject(models.Model):
    """
    A model for managing links to sphinx documentation.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    short_desc = models.TextField()
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return "%s" % self.name
