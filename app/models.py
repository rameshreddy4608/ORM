from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100)
    
    def __self__(self):
        return self.topic_name

class Web_page(models.Model):
    topic_nane=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField()

    def __self__(self):
        return self.name


class Access_Records(models.Model):
    name=models.ForeignKey(Web_page,on_delete=models.CASCADE)
    date=models.DateField()