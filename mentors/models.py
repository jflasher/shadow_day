from django.db import models
from rest_framework import serializers


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name       


class Industry(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name	


class Degree(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name	


class Mentor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')    
    company = models.ForeignKey(Company, related_name="mentors")
    industry = models.ForeignKey(Industry, related_name="mentors")
    degree = models.ForeignKey(Degree, related_name="mentors")

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name[0])


class MentorSerializer(serializers.ModelSerializer):
    company = serializers.RelatedField()
    industry = serializers.RelatedField()
    degree = serializers.RelatedField()

    class Meta:
        model = Mentor


class CompanySerializer(serializers.ModelSerializer):
    mentors = MentorSerializer(many=True)

    class Meta:
        model = Company


class IndustrySerializer(serializers.ModelSerializer):
    mentors = MentorSerializer(many=True)

    class Meta:
        model = Industry


class DegreeSerializer(serializers.ModelSerializer):
    mentors = MentorSerializer(many=True)

    class Meta:
        model = Degree