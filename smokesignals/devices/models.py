from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.fields import UUIDField


# Create your models here.
class Device(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(_('Name'), max_length=200)
    uuid = UUIDField()

    def __unicode__(self):
        return "{0}: {1}".format(self.title, self.owner)

    def get_absolute_url(self):
        return reverse('devices:detail', kwargs={'pk': self.pk})
