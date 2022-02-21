from django.contrib import admin
from mantaapp.models import Baak, Dahsboard, Mahasiswa, Koordinator, DosenPembimbing, DosenPenguji, Scheduling, DocumentApproval, MeetingManagement, PendaftaranAdministratif


admin.site.site_header =('MANTA')


# Register your models here.
admin.site.register(Dahsboard)
admin.site.register(Baak)
admin.site.register(Mahasiswa)
admin.site.register(Koordinator)
admin.site.register(DosenPembimbing)
admin.site.register(DosenPenguji)
admin.site.register(Scheduling)
admin.site.register(MeetingManagement)
admin.site.register(DocumentApproval)
admin.site.register(PendaftaranAdministratif)
