from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):

    created_at = models.DateTimeField(_("Data Criação"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Data Modificação"), auto_now=True)

    class Meta:
        abstract = True
