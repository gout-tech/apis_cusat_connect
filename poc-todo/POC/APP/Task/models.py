from django.db import models
from django.utils.translation import ugettext_lazy as _
from APP.Users.models import User


class UserTasks(models.Model):
    STATUS_CHOICES = (
        (1, _("to do")),
        (2, _("done")),
    )
    description = models.CharField(_('description'), max_length=300, blank=True)
    state = models.IntegerField(choices=STATUS_CHOICES, default=1)
    user_id = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Tasks"
