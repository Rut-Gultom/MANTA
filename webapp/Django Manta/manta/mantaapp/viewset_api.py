from mantaapp.models import Mahasiswa, Dahsboard, Scheduling, DocumentApproval
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from mantaapp.models import PendaftaranAdministratif
from mantaapp.serializers import PendaftaranAdministratifSerializer
from rest_framework import viewsets
from .serializers import PendaftaranAdministratifSerializer
from mantaapp.models import PendaftaranAdministratif
from mantaapp.serializers import PendaftaranAdministratifSerializer
from rest_framework import viewsets
from .serializers import PendaftaranAdministratifSerializer


class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dahsboard.objects.all()
    serializer_class = DashboardSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverViewDashboard(request):
    api_urls = {
        'Announcement List': 'dashboard/announcements',
        'Detail Announcement': 'dashboard/announcements/{id}',
        'Create Announcement': 'dashboard/add-announcements',
        'Update Announcement': 'dashboard/change-announcement/{id}',
        'Delete Announcement': 'dashboard/remove-announcement/{id}',
    }
    return Response(api_urls)

#-------------------------------DASHBOARD----------------------------------------#


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def announcementList(request):
    announcement = Dahsboard.objects.all()
    serializer = DashboardSerializer(announcement, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def announcementDetail(request, pk):
    announcement = Dahsboard.objects.get(id_announcement=pk)
    serializer = DashboardSerializer(announcement, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def addAnnouncement(request):
    serializer = DashboardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def updateAnnouncement(request, pk):
    announcement = Dahsboard.objects.get(id_announcement=pk)
    serializer = DashboardSerializer(instance=announcement, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, {"error_message": "Can not process your request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def deleteAnnouncement(request, pk):
    announcement = Dahsboard.objects.get(id_announcement=pk)
    announcement.delete()
    return Response("Announcement successfully deleted!")

#-------------------------------PENDAFTARAN ADMINISTRATIF----------------------------------------#


class PendaftaranAdministratifViewset(viewsets.ModelViewSet):
    queryset = PendaftaranAdministratif.objects.all()
    serializer_class = PendaftaranAdministratifSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverViewPendaftaranAdministratif(request):
    api_urls = {
        'Login': 'login/user',
        'registration List': 'pendaftaranadministratif/registrations',
        'Detail registration': 'pendaftaranadministratif/registrations/{id}',
        'Create registration': 'pendaftaranadministratif/add-registrations',
        'Change registration': 'pendaftaranadministratif/change-registrations/{id}',
        'Remove registration': 'pendaftaranadministratif/remove-registrations/{id}',
    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def registrationList(request):
    registration = PendaftaranAdministratif.objects.all()
    serializer = PendaftaranAdministratifSerializer(registration, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def registrationDetail(request, pk):
    registration = PendaftaranAdministratif.objects.get(
        registration_id=pk)
    serializer = PendaftaranAdministratifSerializer(registration, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def addregistration(request):
    serializer = PendaftaranAdministratifSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def updateregistration(request, pk):
    registration = PendaftaranAdministratif.objects.get(registration_id=pk)
    serializer = PendaftaranAdministratifSerializer(
        instance=registration, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, {"error_message": "Can not process your request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteregistration(request, pk):
    registration = PendaftaranAdministratif.objects.get(registration_id=pk)
    registration.delete()
    return Response("registration successfully deleted!")


# -------------- SCHEDULING ---------------
class SchedulingViewSet(viewsets.ModelViewSet):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverViewScheduling(request):
    api_urls = {
        'Scheduling List': 'scheduling/list-schedule',
        'Detail Scheduling': 'scheduling/schedulings/{id}',
        'Create Scheduling': 'scheduling/data-add',
        'Update Scheduling': 'scheduling/data-changes/{id}',
        'Delete Scheduling': 'scheduling/data-remove/{id}',
    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def schedulingList(request):
    scheduling = Scheduling.objects.all()
    serializer = SchedulingSerializer(scheduling, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def schedulingDetail(request, pk):
    scheduling = Scheduling.objects.get(id_scheduling=pk)
    serializer = SchedulingSerializer(scheduling, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addScheduling(request):
    serializer = SchedulingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateScheduling(request, pk):
    scheduling = Scheduling.objects.get(id_scheduling=pk)
    serializer = SchedulingSerializer(instance=scheduling, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, {"error_message": "Can not process your request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteScheduling(request, pk):
    scheduling = Scheduling.objects.get(id_scheduling=pk)
    scheduling.delete()
    return Response("Schedule successfully deleted!")

#-------------------------------DATA---------------------------------------#


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverViewData(request):
    api_urls = {
        'Data List': 'data',
        'Detail Data': 'data-user/{id}',
        'Update Data': 'change-data/{id}',
        'Delete Data': 'remove-data/{id}',
    }
    return Response(api_urls)

# menampilkan data


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dataList(request):
    data = Mahasiswa.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dataDetail(request, pk):
    data = Mahasiswa.objects.get(nim=pk)
    serializer = DataSerializer(data, many=False)
    if serializer.is_valid:
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# mengupdate data


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def updateData(request, pk):
    update_data = Mahasiswa.objects.get(nim=pk)
    serializer = DataSerializer(instance=update_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, {"error_message": "Can not process your request"}, status=status.HTTP_400_BAD_REQUEST)

# menghapus data


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def deletedata(request, pk):
    data = Mahasiswa.objects.get(nim=pk)
    data.delete()
    return Response("Data successfully deleted!")

#-------------------------------PROFILE----------------------------------------#
class ViewSet(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = ProfileSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverViewProfile(request):
    api_urls = {
        'Profile': 'profile/{id}',
        'Update Profile': 'profile/change-profile/{id}',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profiles(request):
    profile = Mahasiswa.objects.all()
    serializer = ProfileSerializer(profile, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profileDetail(request,pk):
        profile = Mahasiswa.objects.get(nim=pk)
        serializer = ProfileSerializer(profile, many=False)
        if serializer.is_valid:
                return Response(serializer.data)
        else:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def updateProfile(request, pk):
    profile = Mahasiswa.objects.get(nim=pk)
    serializer = ProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, {"error_message": "Can not process your request"}, status=status.HTTP_400_BAD_REQUEST)


#-------------------------------DOCUMENT APPROVAL----------------------------------------#
class DocumentApprovalViewSet(viewsets.ModelViewSet):
    queryset = DocumentApproval.objects.all()
    serializer_class = DocumentSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverViewDocumentApproval(request):
    api_urls = {
        'Document List': 'documentapproval/documents',
        'Detail Document': 'documentapproval/document/{id}',
        'Create Document': 'documentapproval/add-document/',
        'Update Document': 'documentapproval/change-document/{id}',
        'Delete Document': 'documentapproval/remove-document/{id}',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def documentList(request):
    document = DocumentApproval.objects.all()
    serializer = DocumentSerializer(document, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def documentDetail(request, pk):
    document = DocumentApproval.objects.get(id_document=pk)
    serializer = DocumentSerializer(document, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def addDocument(request):
    serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def updateDocument(request, pk):
    document = DocumentApproval.objects.get(id_document=pk)
    serializer = DocumentSerializer(instance=document, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, {"error_message": "Can not process your request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def deleteDocument(request, pk):
    document = DocumentApproval.objects.get(id_document=pk)
    document.delete()
    return Response("Document successfully deleted!")
