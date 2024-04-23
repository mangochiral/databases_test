# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Drug(models.Model):
    drug_name = models.TextField(db_column='Drug_name', blank=True, null=True)
    drug_id = models.BigIntegerField(db_column='Drug_id', primary_key=True)
    brands_id = models.ForeignKey('Brandtype',on_delete=models.CASCADE, db_column='brand_id')


    class Meta:
        managed = False
        db_table = 'drug'
        app_label = 'home'  # Add the app label here

class Pubmed(models.Model):
    pmid = models.BigIntegerField(db_column='PubMed ID',primary_key=True)
    abstract_data = models.TextField(db_column='Abstract',  blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'references_data'
        app_label = 'home'  # Add the app label here
        
class Conditionstype(models.Model):
    con_type = models.TextField(db_column='condition_name', blank=True, null=True)
    con_id = models.BigIntegerField(db_column='condition_id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'condition_type'
        app_label = 'home'  # Add the app label here

class Brandtype(models.Model):
    brand_name1 = models.TextField(db_column='brand_name1', blank=True, null=True)
    brand_name2 = models.TextField(db_column='brand_name2', blank=True, null=True)
    brand_name3 = models.TextField(db_column='brand_name3', blank=True, null=True)
    brand_id = models.BigIntegerField(db_column='brand_id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'brand'
        app_label = 'home'  # Add the app label here