from mantaapp.models import *
from rest_framework import serializers
from mantaapp.models import PendaftaranAdministratif


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dahsboard
        fields = ['id_announcement', 'title', 'body']


class PendaftaranAdministratifSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendaftaranAdministratif
        fields = ['registration_id', 'group_number', 'group_members',
                  'study_program', 'supervisor']


class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = ['id_scheduling', 'group_number',
                  'group_member', 'activity_name', 'date']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ['nim', 'name', 'address', 'mobile', 'email', 'picture']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentApproval
        fields = ['id_document', 'group_number',
                  'group_members', 'file_name', 'pdf']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = "__all__"
