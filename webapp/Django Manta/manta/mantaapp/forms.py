from django import forms
from .models import *


class dahsboardform(forms.ModelForm):
    class Meta:
        model = Dahsboard
        fields = "__all__"


class formpendaftaran(forms.ModelForm):
    class Meta:
        model = PendaftaranAdministratif
        fields = ["registration_id", "group_number",
                  "group_members", "study_program", "supervisor"]


class schedulingform(forms.ModelForm):
    class Meta:
        model = Scheduling
        fields = ["id_scheduling", "group_number",
                  "group_member", "activity_name", "date"]


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentApproval
        fields = ["group_number", "group_members", "file_name", "pdf"]

        widgets = {
            'group_number': forms.NumberInput({'class': 'form-control'}),
            'group_members': forms.TextInput({'class': 'form-control'}),
            'file_name': forms.TextInput({'class': 'form-control'}),
            'pdf': forms.FileInput({'class': 'form-control'})

        }


class emailForm(forms.Form):
    email = forms.EmailField(max_length=200)


class mahasiswaform(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ["name", "username", "password"]


class koordinatorform(forms.ModelForm):
    class Meta:
        model = Koordinator
        fields = ["name", "username", "password"]


class dospengform(forms.ModelForm):
    class Meta:
        model = DosenPenguji
        fields = ["name", "username", "password"]


class dospemform(forms.ModelForm):
    class Meta:
        model = DosenPembimbing
        fields = ["name", "username", "password"]

