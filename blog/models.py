from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=RichTextField(blank=True,null=True)
    #body=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    # def summary(self):
    #     return self.body[:1000]
        
    def pretty_date(self):
        return self.pub_date.strftime(' %b %e %Y ')
