from django.db import models

class Blogpost(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    posttitle = models.TextField(db_column='PostTitle', blank=True, null=True)  # Field name made lowercase.
    postcontent = models.TextField(db_column='PostContent', blank=True, null=True)  # Field name made lowercase.
    author = models.TextField(db_column='Author')  # Field name made lowercase.
    publishedon = models.DateTimeField(db_column='PublishedOn', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.

    class Meta:
        db_table = 'Blogpost'