from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from .models import Mentor, MentorSerializer, Company, CompanySerializer, \
    Industry, IndustrySerializer, Degree, DegreeSerializer

###
# Mentors
###
class MentorsView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        mentors = Mentor.objects.all()
        serializer = MentorSerializer(mentors)
        return Response(serializer.data)


###
# Companies
###
class CompaniesView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies)
        return Response(serializer.data)


###
# Industry
###
class IndustriesView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        industries = Industry.objects.all()
        serializer = IndustrySerializer(industries)
        return Response(serializer.data)


###
# Degrees
###
class DegreesView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        degrees = Degree.objects.all()
        serializer = DegreeSerializer(degrees)
        return Response(serializer.data)


###
# Search
###
class SearchView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        params = request.QUERY_PARAMS
        industry = params.get('industry')
        degree = params.get('degree')
        company = params.get('company')
        print "Incoming search for \nCompany: %s\nIndustry: %s\nDegree:%s" % \
            (company, industry, degree)

        # Search all the things using some fanciness based on inputs
        if company is not None:
            kwargs['company__name'] = company
        if degree is not None:
            kwargs['degree__name'] = degree
        if industry is not None:
            kwargs['industry__name'] = industry
        mentors = Mentor.objects.filter(**kwargs)
        serializer = MentorSerializer(mentors)
        return Response(serializer.data)