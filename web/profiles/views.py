from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import GeneralUserProflie, CompanyUserProfile, Skill, EducationProfile, WorkExperienceProfile
from .serializers import GeneralUserProfileSerializer, CompanyUserProfileSerializer, SkillSerializer, EducationProfileSerializer, WorkExperienceSerializer
# Create your views here.
@api_view(['GET'])
def get_general_user_profile(request, pk):   #display general user profile
    try:
        profile = GeneralUserProflie.objects.get(user=pk)
    except GeneralUserProflie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GeneralUserProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['POST','GET', 'PUT', 'DELETE'])          #this view is for previous education for the job seeker
def user_education_profile(request, pk):
    try:
        profile = EducationProfile.objects.get(user=pk)
    except EducationProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':                #post method for adiing new education record ( might have to move it as a seperate view)
        serializer = EducationProfileSerializer(profile)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':               #get all education records for the logged in user 
        serializer = EducationProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':               #edit specific education record
        serializer = EducationProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':            #delete specific educationrecord
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])    #display company Rep user profile 
def get_company_user_profile(request, pk):
    try:
        profile = CompanyUserProfile.objects.get(user=pk)
    except CompanyUserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CompanyUserProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['GET', 'POST'])              #this will be used to store skills. refinement to be required later 
def skills(request):
    if request.method == 'GET':
       
        skills = Skill.objects.all()
        
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            skill = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)