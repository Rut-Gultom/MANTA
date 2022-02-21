from django.urls import path, include
from rest_framework.viewsets import ViewSet
from mantaapp import viewset_api
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # dashboard
    path('dashboard/announcements',
         viewset_api.announcementList, name='announcement-list'),
    path('dashboard/announcements/<str:pk>',
         viewset_api.announcementDetail, name="announcement-detail"),
    path('dashboard/add-announcements',
         viewset_api.addAnnouncement, name="announcement-create"),
    path('dashboard/change-announcement/<str:pk>',
         viewset_api.updateAnnouncement, name="updat-announcement"),
    path('dashboard/remove-announcement/<str:pk>',
         viewset_api.deleteAnnouncement, name="delete-announcement"),

    # pendaftaran adm
    path('pendaftaranadministratif/registrations',
         viewset_api.registrationList, name='registration-list'),
    path('pendaftaranadministratif/registrations/<str:pk>',
         viewset_api.registrationDetail, name="registration-detail"),
    path('pendaftaranadministratif/add-registrations',
         viewset_api.addregistration, name="registration-add"),
    path('pendaftaranadministratif/change-registrations/<str:pk>',
         viewset_api.updateregistration, name="registration-update"),
    path('pendaftaranadministratif/remove-registrations/<str:pk>',
         viewset_api.deleteregistration, name="registration-delete"),

    # scheduling
    path('scheduling/list-schedule',
         viewset_api.schedulingList, name='scheduling-list'),
    path('scheduling/schedulings/<str:pk>',
         viewset_api.schedulingDetail, name="scheduling-detail"),
    path('scheduling/data-add', viewset_api.addScheduling,
         name="scheduling-create"),
    path('scheduling/data-changes/<str:pk>',
         viewset_api.updateScheduling, name="scheduling-update"),
    path('scheduling/data-remove/<str:pk>',
         viewset_api.deleteScheduling, name="scheduling-delete"),

    # data
    path('data', viewset_api.dataList, name='data-list'),
    path('data-user/<str:pk>', viewset_api.dataDetail, name="data-detail"),
    path('change-data/<str:pk>', viewset_api.updateData, name="update-data"),
    path('remove-data/<str:pk>', viewset_api.deletedata, name="delete-data"),

    # profile
    path('user/profile', viewset_api.profiles, name="profile-users"),
    path('user/profile/<str:pk>', viewset_api.profileDetail, name="profile-detail"),
    path('user/profile/profile-change/<str:pk>',
         viewset_api.updateProfile, name="profile-update"),

    # document approval
    path('document-approval/list-documents',
         viewset_api.documentList, name="document-list"),
    path('document-approval/document/<str:pk>',
         viewset_api.documentDetail, name="documentapproval-detail"),
    path('document-approval/document-add',
         viewset_api.addDocument, name="documentapproval-create"),
    path('document-approval/document-change/<str:pk>',
         viewset_api.updateDocument, name="documentapproval-update"),
    path('document-approval/document-remove/<str:pk>',
         viewset_api.deleteDocument, name="documentapproval-delete")
]
