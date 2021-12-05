from django.db import models
from django.conf import settings
import string
from .utils.utils import Base62
from .validators import valid_URL
# Create your models here.


class Url(models.Model):
    url = models.CharField(max_length=10000,validators=[valid_URL])
    short_code = models.CharField(max_length=10, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def save(self, *args,**kwargs):
        valid_URL(self.url)
        try:
            last = Url.objects.latest('id')
            new_code = Base62.encode(last.id)
        except Exception as e:
            new_code = Base62.encode(0)
        self.short_code = new_code
        super(Url,self).save(*args,**kwargs)

   
    
    def get(self, short_code):
        id = Base62.decode(short_code)
        return self.objects.get(id)
    
    
    def logscount(self):
        return self.hitslog_set.count()
    
    
    
class HitsLog(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)