from django.db import models
from sorl.thumbnail.fields import ImageWithThumbnailsField

class Technology(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = "technologies"

    def __unicode__(self):
        return "%s" % (self.name,)

class Photo(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = ImageWithThumbnailsField(upload_to="portfolio/",
                                     thumbnail={'size': (460, 250),
                                                'options': ('crop', 'upscale')})

    def __unicode__(self):
        return "%s" % (self.name,)

class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    role = models.CharField(max_length=255)
    technologies = models.ManyToManyField(Technology)
    photos = models.ManyToManyField(Photo, through='ProjectPhotoOrganizer')
    short_description = models.TextField()
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    @property
    def ordered_photos(self):
        return self.photos.order_by('projectphotoorganizer__order')

    class Meta:
        ordering = ('order',)
    
    def __unicode__(self):
        return "%s" % (self.name,)
    

class ProjectPhotoOrganizer(models.Model):
    photo = models.ForeignKey(Photo)
    project = models.ForeignKey(Project)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)
