from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Somali_German_Dictionary(models.Model):
    '''
    This is our model for Somali and German words and their English equivalents.
    '''
    somali =  models.CharField('Somali',max_length=100,null=False)
    english =  models.CharField('English',max_length=100,null=True,blank=True)
    German =  models.CharField('German',max_length=100,null=True,blank=True)


    def __str__(self):
        ''' This returns a string listing the contents of a dictionary entry. '''
        return (self.somali + " = " + self.english + " = " + str(self.German))