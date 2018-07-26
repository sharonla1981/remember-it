from django.db import models

class ExternalTool(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    api_id = models.CharField(max_length=32)
    api_key = models.CharField(max_length=32)
    application = models.CharField(max_length=50)

    def __str__(self):
        return self.name