"""manta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from mantaapp import views, viewset_api
from django.conf.urls import url
from mantaapp.viewset_api import *
from rest_framework import routers
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mantaapp.urls_api')),
    path('', views.login, name='login'),
    path('login', views.masuk, name='masuk'),
    path('logout', views.logoutUser, name='logout'),

    # mahasiswa

    path('profile-mahasiswa', views.profile_mhs, name='profile_mahasiswa'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path('document-approval-mahasiswa1', views.documentapprovalmahasiswa1,
         name='document-approval-mahasiswa1'),
    path('document-approval/add-document', views.documentapprovalmahasiswa1,
         name='document-approval-mahasiswa1'),
    path('document-approval-mahasiswa2', views.documentapprovalmahasiswa2,
         name='document-approval-mahasiswa2'),
    path('document-approval/delete-document/<str:pk>',
         views.delete_document, name='deletedocument'),
    path('dashboard-mahasiswa', views.mahasiswa, name='mahasiswa'),
    path('pendaftaran_adm', views.input_pend_adm, name='pendaftaran_adm'),
    path('pendaftaran_adm_next', views.pendaftaran_adm_next,
         name='pendaftaran_adm_next'),
    path('pendaftaran-adm-mhs', views.pendaftaranadmmhs,
         name='pendaftaran_adm_mhs'),
    path('skip-pendaftaran-adm-mhs', views.pendaftaranadmmhs,
         name='skip-pendaftaran_adm_mhs'),
    path('Scheduling-Mahasiswa', views.Scheduling_Mahasiswa,
         name='Scheduling_Mahasiswa'),
    path('Scheduling_Edit_Mhs', views.input_sche_edit_mhs,
         name='Scheduling_Edit_Mhs'),
    path('meeting-management-mahasiswa', views.meetingmanagementmahasiswa,
         name='meeting management mahasiswa'),
    path('registration-mhs', views.inputregistrationMhs, name='registration_mhs'),

    # dosenpembimbing
    path('profile-dospem', views.profile_dospem,
         name='profile_dosen_pembimbing'),
    path('edit-profile-dospem', views.editprofile_dospem,
         name='edit_profile_dosenpembimbing'),
    path('dashboard-dospem', views.dashboarddospem, name='dashboarddospem'),
    path('pendaftaran-adm-dospem', views.pendaftaranadmdospem,
         name='pendaftaranadmdospem'),
    path('Scheduling-dosen-pembimbing', views.Schedulingdosenpembimbing,
         name='Schedulingdosenpembimbing'),
    path('meeting-management-dospem', views.meetingmanagementdospem,
         name='meetingmanagementdospem'),
    path('document-approval-dosenpembimbing', views.documentapprovaldosenpembimbing,
         name='document approval dosen pembimbing'),
    path('registration_dospem', views.inputregistrationDosPem,
         name='registration_dospem'),

    # dosenpenguji
    path('profile-dospeng', views.profile_dospeng, name='profile_dosen_penguji'),
    path('edit-profile-dospeng', views.editprofile_dospeng,
         name='edit_profile_dosenpenguji'),
    path('dashboard-dospenguji', views.dashboarddosenpenguji,
         name='dashboarddospenguji'),
    path('Scheduling-Dosen-Penguji', views.SchedulingDosenPenguji,
         name='SchedulingDosenPenguji'),
    path('document-approval-dosenpenguji', views.documentapprovaldosenpenguji,
         name='document approval dosen penguji'),
    path('registration-dospeng', views.inputregistrationDosPeng,
         name='registration_dospeng'),

    # koordinatorTA
    path('profile-koordinatorTA', views.profile_koordinatorTA,
         name='profile_koordinatorTA'),
    path('edit-profile-koordinatorTA', views.editprofile_koordinatorTA,
         name='edit_profile_koordinatorTA'),
    path('add', views.inputpengumuman, name='announcement'),
    path('dashboard-koordinator-TA', views.koordinator, name='koordinator'),
    path('pendaftaran-adm-koor-TA', views.pendaftaranadmkoorTA,
         name='pendaftaranadmkoorTA'),
    path('Scheduling-Koordinator-TA', views.SchedulingKoordinatorTA,
         name='SchedulingKoordinatorTA'),
    path('meeting-management-KTA', views.meeting_management_KTA,
         name='meeting_management_KTA'),

    # Baak
    path('dashboard-baak', views.baak, name='baak'),
    path('registration-koordinator', views.inputregistrationKoordinator,
         name='registration-koordinator'),
    path('update-data', views.list_mahasiswa, name='list_mahasiswa'),
    path('update-data-koordinator',
         views.list_koordinator, name='list_koordinator'),
    path('update-data-dospem', views.list_dospem, name='list_dospem'),
    path('update-data-dospeng', views.list_dospeng, name='list_dospeng'),
    # edit delete update mahasiswa
    path('edit-mhs/<str:id_mhs>', views.editDataMhs, name="editDataMhs"),
    path('update-mhs/<str:id_mhs>', views.updateDataMhs, name="updateDataMhs"),
    path('delete-mhs/<str:pk>', views.deleteDataMhs, name="deleteDataMhs"),
    # edit delete update koordinator
    path('edit-koordinator/<str:id_koordinator>',
         views.editDataKoordinator, name="editDataKoordinator"),
    path('update-koordinator/<str:id_koordinator>',
         views.updateDataKoordinator, name="updateDataKoordinator"),
    path('delete-koordinator/<str:pk>',
         views.deleteDataKoordinator, name="deleteDataKoordinator"),
    # edit delete update dosen pembimbing
    path('edit-dospem/<str:id_dospem>',
         views.editDataDospem, name="editDataDospem"),
    path('update-dospem/<str:id_dospem>',
         views.updateDataDospem, name="updateDataDospem"),
    path('delete-dospem/<str:pk>', views.deleteDataDospem, name="deleteDataDospem"),
    # edit delete update dosen penguji
    path('edit-dospeng/<str:id_dospeng>',
         views.editDataDospeng, name="editDataDospeng"),
    path('update-dospeng/<str:id_dospeng>',
         views.updateDataDospeng, name="updateDataDospeng"),
    path('delete-dospeng/<str:pk>',
         views.deleteDataDospeng, name="deleteDataDospeng"),

    # Dashboard
    path('edit/<int:id_peng>', views.editpengumuman, name="editpengumuman"),
    path('update/<int:id_pengumuman>',
         views.updatepengumuman, name="updatepengumuman"),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        views.deletepengumuman, name="deletepengumuman"),

    # pendaftaran administratif
    path('edit-pend/<int:id_pend>', views.editpendaftaran, name="editpendaftaran"),
    path('update-pend/<int:id_pend>',
         views.updatependaftaran, name="updatependaftaran"),
    url(r'^delete-pend/(?P<pk>[0-9]+)/$',
        views.deletependaftaran, name="deletependaftaran"),

    # Scheduling
    path('edit-sche/<int:id_scheduling>',
         views.editscheduling, name="editscheduling"),
    path('update-sche/<int:id_scheduling>',
         views.updatescheduling, name="updatescheduling"),
    url(r'^delete-sche/(?P<pk>[0-9]+)/$',
        views.deletescheduling, name="deletescheduling"),

    # email
    path('change-password', views.sendemail, name='change-password'),
    path('success-send-email', views.sendemail, name='succes_send_email'),

    # Meeting management
    path('add-meeting', views.inputmeeting, name="add_meeting"),
    path('meeting-management-dospem', views.meeting_management,
         name='meetingmanagementdospem'),
    path('meeting-management-mhs', views.meeting_mhs,
         name='meetingmanagementmhs'),
    path('meeting-management-dospeng', views.meeting_koordinator,
         name='meetingmanagementdospeng'),
    path('meeting-management-koordinator', views.meeting_dospeng,
         name='meetingmanagementkoordinator'),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
