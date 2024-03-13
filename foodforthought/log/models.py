from django.db import models

class Log(models.Model):
   recipe_ingredients = models.JSONField();
   recipe_area =  models.JSONField(); 
   recipe_categories = models.JSONField();
   activities = models.JSONField();

    class Meta:
        abstract = True

    def save(self, *args, **kwargs)
        self.__class__.objects.exclude(id=self.id).delete()
        super(Log, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()

