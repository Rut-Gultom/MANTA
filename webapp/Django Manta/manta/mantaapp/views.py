from django.core.files.storage import FileSystemStorage
from django.db.models.fields import files
from django.shortcuts import redirect, render
from django.core import serializers
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from .forms import dahsboardform, emailForm
from django.contrib.auth import authenticate, login, logout
from .forms import formpendaftaran, DocumentForm
from manta.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings
import os
import datetime
# Create your views here.


def login(request):
    return render(request, 'login.html')

# profile


def profile_mhs(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    return render(request, 'profile_mahasiswa.html', {'profile': profile})


def edit_profile(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    if request.method == 'POST':
        uploaded_file = request.FILES.get('profile_photo', None)
        print(uploaded_file)
        if uploaded_file is not None:
            fs = FileSystemStorage()
            old_name, extension = os.path.splitext(uploaded_file.name)
            filename = profile.nim + extension
            n_filename = fs.save("static/" + filename, uploaded_file)
            profile.picture = n_filename
        profile.name = request.POST["name"]
        profile.address = request.POST["address"]
        profile.mobile = request.POST["mobile"]
        profile.email = request.POST["email"]
        profile.save()
        request.session['user'] = serializers.serialize('json', [profile])
        return redirect('/profile-mahasiswa')
    return render(request, 'edit_profilemhs.html', {'profile': profile})


def profile_dospem(request):
    dosenpembimbing = serializers.deserialize('json', request.session['user'])
    print(dosenpembimbing)
    profile = None
    for d in dosenpembimbing:
        profile = d.object
    return render(request, 'profile_dospem.html', {'profile': profile})


def editprofile_dospem(request):
    dosenpembimbing = serializers.deserialize('json', request.session['user'])
    print(dosenpembimbing)
    profile = None
    for d in dosenpembimbing:
        profile = d.object
    if request.method == 'POST':
        uploaded_file = request.FILES.get('profile_photo', None)
        print(uploaded_file)
        if uploaded_file is not None:
            fs = FileSystemStorage()
            old_name, extension = os.path.splitext(uploaded_file.name)
            filename = profile.nidn_pembimbing + extension
            n_filename = fs.save("static/" + filename, uploaded_file)
            profile.picture = n_filename
        profile.name = request.POST["name"]
        profile.address = request.POST["address"]
        profile.mobile = request.POST["mobile"]
        profile.email = request.POST["email"]
        profile.save()
        request.session['user'] = serializers.serialize('json', [profile])
        return redirect('/profile-dospem')
    return render(request, 'editprofile_dospem.html', {'profile': profile})


def profile_dospeng(request):
    dosenpenguji = serializers.deserialize('json', request.session['user'])
    print(dosenpenguji)
    profile = None
    for d in dosenpenguji:
        profile = d.object
    return render(request, 'profile_dosenpenguji.html', {'profile': profile})


def editprofile_dospeng(request):
    dosenpenguji = serializers.deserialize('json', request.session['user'])
    print(dosenpenguji)
    profile = None
    for d in dosenpenguji:
        profile = d.object
    if request.method == 'POST':
        uploaded_file = request.FILES.get('profile_photo', None)
        print(uploaded_file)
        if uploaded_file is not None:
            fs = FileSystemStorage()
            old_name, extension = os.path.splitext(uploaded_file.name)
            filename = profile.nidn_penguji + extension
            n_filename = fs.save("static/" + filename, uploaded_file)
            profile.picture = n_filename
        profile.name = request.POST["name"]
        profile.address = request.POST["address"]
        profile.mobile = request.POST["mobile"]
        profile.email = request.POST["email"]
        profile.save()
        request.session['user'] = serializers.serialize('json', [profile])
        return redirect('/profile-dospeng')
    return render(request, 'editprofile_dospeng.html', {'profile': profile})


def profile_koordinatorTA(request):
    koordinatorTA = serializers.deserialize('json', request.session['user'])
    print(koordinatorTA)
    profile = None
    for k in koordinatorTA:
        profile = k.object
    return render(request, 'profile_koordinatorTA.html', {'profile': profile})


def editprofile_koordinatorTA(request):
    koordinatorTA = serializers.deserialize('json', request.session['user'])
    print(koordinatorTA)
    profile = None
    for k in koordinatorTA:
        profile = k.object
    if request.method == 'POST':
        uploaded_file = request.FILES.get('profile_photo', None)
        print(uploaded_file)
        if uploaded_file is not None:
            fs = FileSystemStorage()
            old_name, extension = os.path.splitext(uploaded_file.name)
            filename = profile.nidn_koordinator + extension
            n_filename = fs.save("static/" + filename, uploaded_file)
            profile.picture = n_filename
        profile.name = request.POST["name"]
        profile.address = request.POST["address"]
        profile.mobile = request.POST["mobile"]
        profile.email = request.POST["email"]
        profile.save()
        request.session['user'] = serializers.serialize('json', [profile])
        return redirect('/profile-koordinatorTA')
    return render(request, 'editprofile_koordinatorTA.html', {'profile': profile})


# mahasiswa
def mahasiswa(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    mahasiswa = Dahsboard.objects.all()
    return render(request, 'mahasiswa.html', {'mahasiswa_announcement': mahasiswa, 'profile': profile})


def pendaftaran_adm(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    return render(request, 'pendaftaran_adm.html', {'profile': profile})


def pendaftaran_adm_next(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    return render(request, 'pendaftaran_adm_next.html', {'profile': profile})


def pendaftaranadmmhs(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    pendaftaran_mahasiswa = PendaftaranAdministratif.objects.all()
    return render(request, 'pendaftaran_adm_mhs.html', {'pendaftaran_mhs': pendaftaran_mahasiswa, 'profile': profile})


def skippendaftaranadmmhs(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    skip_pendaftaran_mahasiswa = PendaftaranAdministratif.objects.all()
    return render(request, 'pendaftaran_adm_mhs.html', {'skip_pendaftaran_mhs': skip_pendaftaran_mahasiswa, 'profile': profile})


def Scheduling_Mahasiswa(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    scheduling = Scheduling.objects.all()
    return render(request, 'Scheduling_Mahasiswa.html', {'Scheduling_Mahasiswa': scheduling, 'profile': profile})


def Scheduling_Edit_Mhs(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    scheduling = Scheduling.objects.all()
    return render(request, 'Scheduling_Edit_Mhs.html', {'Scheduling_Edit_Mhs': scheduling, 'profile': profile})


def meetingmanagementmahasiswa(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    return render(request, 'meeting_management_mahasiswa.html', {'profile': profile})


def documentapprovalmahasiswa1(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    konteks = None
    if request.method == 'POST':
        uploaded_file = request.FILES['pdf']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        DocumentApproval.objects.create(
            file_name=request.POST['file_name'], pdf=name, group_number=request.POST['group_number'], group_members=request.POST['group_members'])
        pesan = "Data berhasil disimpan"
        konteks = {
            'form': DocumentForm(),
            'pesan': pesan,
        }
        return redirect('/document-approval-mahasiswa2', konteks)
    else:
        form = DocumentForm()

        pesan = "Data tidak berhasil disimpan"
        konteks = {
            'form': DocumentForm(),
            'pesan': pesan,
        }

    return render(request, 'documentapproval_mahasiswa1.html', {'profile': profile, 'konteks': konteks})


def documentapprovalmahasiswa2(request):
    documents = DocumentApproval.objects.all()
    konteks = {
        'documents': documents,
    }
    return render(request, 'documentapproval_mahasiswa2.html', konteks)


def delete_document(request, pk):
    DocumentApproval.objects.filter(id_document=pk).delete()
    return redirect('document-approval-mahasiswa2')


# Dosen Pembimbing

def dashboarddospem(request):
    dosenpembimbing = serializers.deserialize('json', request.session['user'])
    print(dosenpembimbing)
    profile = None
    for d in dosenpembimbing:
        profile = d.object
    dospem = Dahsboard.objects.all()
    return render(request, 'dashboard_dospem.html', {'dospem_announcement': dospem, 'profile': profile})


def pendaftaranadmdospem(request):
    dosenpembimbing = serializers.deserialize('json', request.session['user'])
    print(dosenpembimbing)
    profile = None
    for d in dosenpembimbing:
        profile = d.object
    pendaftaranadm_dospem = PendaftaranAdministratif.objects.all()
    return render(request, 'pendaftaran_adm_dospem.html', {'pendaftarandospem': pendaftaranadm_dospem, 'profile': profile})


def Schedulingdosenpembimbing(request):
    dosenpembimbing = serializers.deserialize('json', request.session['user'])
    print(dosenpembimbing)
    profile = None
    for d in dosenpembimbing:
        profile = d.object
    Schedulingdosenpembimbing = Scheduling.objects.all()
    return render(request, 'Scheduling_Dosen_Pembimbing.html', {'Scheduling_Dosen_Pembimbing': Schedulingdosenpembimbing, 'profile': profile})


def meetingmanagementdospem(request):
    dosenpembimbing = serializers.deserialize('json', request.session['user'])
    print(dosenpembimbing)
    profile = None
    for d in dosenpembimbing:
        profile = d.object
    return render(request, 'meeting_management_dopem.html', {'profile': profile})


def documentapprovaldosenpembimbing(request):
    documents = DocumentApproval.objects.all()
    konteks = {
        'documents': documents,
    }
    return render(request, 'documentapproval_dosenpembimbing.html', konteks)


# Dosen Penguji

def dashboarddosenpenguji(request):
    dosenpenguji = serializers.deserialize('json', request.session['user'])
    print(dosenpenguji)
    profile = None
    for d in dosenpenguji:
        profile = d.object
    dospeng = Dahsboard.objects.all()
    return render(request, 'dashboard_dosenpenguji.html', {'dospeng_announcement': dospeng, 'profile': profile})


def SchedulingDosenPenguji(request):
    dosenpenguji = serializers.deserialize('json', request.session['user'])
    print(dosenpenguji)
    profile = None
    for d in dosenpenguji:
        profile = d.object
    SchedulingDosenPenguji = Scheduling.objects.all()
    return render(request, 'Scheduling_Dosen_Penguji.html', {'Scheduling_Dosen_Penguji': SchedulingDosenPenguji, 'profile': profile})


def documentapprovaldosenpenguji(request):
    documents = DocumentApproval.objects.all()

    konteks = {
        'documents': documents,
    }
    return render(request, 'documentapproval_dosenpenguji.html',  konteks)


# Koordinator TA

def koordinator(request):
    koordinatorTA = serializers.deserialize('json', request.session['user'])
    print(koordinatorTA)
    profile = None
    for k in koordinatorTA:
        profile = k.object
    koordinator = Dahsboard.objects.all().order_by('-post_date')
    return render(request, 'koordinator.html', {'koordinatorTA_announcement': koordinator, 'profile': profile})


def pendaftaranadmkoorTA(request):
    koordinatorTA = serializers.deserialize('json', request.session['user'])
    print(koordinatorTA)
    profile = None
    for k in koordinatorTA:
        profile = k.object
    pendaftaranadmkoorTA = PendaftaranAdministratif.objects.all()
    return render(request, 'pendaftaran_adm_koor_TA.html', {'pendaftaran_koorta': pendaftaranadmkoorTA, 'profile': profile})


def SchedulingKoordinatorTA(request):
    koordinatorTA = serializers.deserialize('json', request.session['user'])
    print(koordinatorTA)
    profile = None
    for k in koordinatorTA:
        profile = k.object
    SchedulingKoordinatorTA = Scheduling.objects.all()
    return render(request, 'Scheduling_Koordinator_TA.html', {'Scheduling_Koordinator_TA': SchedulingKoordinatorTA, 'profile': profile})


def meeting_management_KTA(request):
    koordinatorTA = serializers.deserialize('json', request.session['user'])
    print(koordinatorTA)
    profile = None
    for k in koordinatorTA:
        profile = k.object
    return render(request, 'meeting_management_KTA.html', {'profile': profile})


def document_registration(request):
    return render(request, 'document_registration.html')

# login-logout


def masuk(request):
    mahasiswa = Mahasiswa.objects.filter(username=request.POST.get(
        'username'), password=request.POST.get('password'))
    dosenpembimbing = DosenPembimbing.objects.filter(
        username=request.POST.get('username'), password=request.POST.get('password'))
    dosenpenguji = DosenPenguji.objects.filter(username=request.POST.get(
        'username'), password=request.POST.get('password'))
    koordinatorTA = Koordinator.objects.filter(username=request.POST.get(
        'username'), password=request.POST.get('password'))
    baak = Baak.objects.filter(username=request.POST.get(
        'username'), password=request.POST.get('password'))

    if dosenpembimbing:
        request.session['user'] = serializers.serialize(
            'json', dosenpembimbing)
        return redirect('dashboarddospem')
    elif mahasiswa:
        request.session['user'] = serializers.serialize('json', mahasiswa)
        return redirect('mahasiswa')
    elif dosenpenguji:
        request.session['user'] = serializers.serialize('json', dosenpenguji)
        return redirect('dashboarddospenguji')
    elif koordinatorTA:
        request.session['user'] = serializers.serialize('json', koordinatorTA)
        return redirect('koordinator')
    elif baak:
        request.session['user'] = serializers.serialize('json', baak)
        return redirect('baak')
    else:
        return redirect('login')


def logoutUser(request):
    logout(request)
    return redirect('login')


# DASHBOARD

def inputpengumuman(request):
    koordinatorTA = serializers.deserialize('json', request.session['user'])
    print(koordinatorTA)
    profile = None
    for k in koordinatorTA:
        profile = k.object
    if request.method == 'POST':
        id_announcement = request.POST.get('id_announcement')
        title = request.POST.get('title')
        body = request.POST.get('body')
        Dahsboard.objects.create(
            id_announcement=id_announcement, title=title, body=body)
    return render(request, 'announcement.html', {'profile': profile})


def deletepengumuman(request, pk):
    Dahsboard.objects.filter(id_announcement=pk).delete()
    return redirect('koordinator')


def editpengumuman(request, id_peng):
    koordinatorTA = serializers.deserialize('json', request.session['user'])
    print(koordinatorTA)
    profile = None
    for k in koordinatorTA:
        profile = k.object
    koordinator = Dahsboard.objects.filter(id_announcement=id_peng)
    return render(request, 'editpengumuman.html', {'koordinatorTA_announcement': koordinator, 'profile': profile})


def updatepengumuman(request, id_pengumuman):
    koordinator = Dahsboard.objects.get(id_announcement=id_pengumuman)
    form = dahsboardform(request.POST, instance=koordinator)
    if form.is_valid:
        form.save()
        koordinator = Dahsboard.objects.all()
        return redirect('koordinator')


#  Registration

def inputregistrationMhs(request):
    if request.method == 'POST':
        nim = request.POST.get('nim')
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        study_program = request.POST.get('study_program')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        Mahasiswa.objects.create(nim=nim, name=name, username=username, password=password, gender=gender, study_program=study_program,
                                 email=email, mobile=mobile, address=address)
    return render(request, 'dashboard_BAAK.html')


def inputregistrationDosPem(request):
    if request.method == 'POST':
        nidn_pembimbing = request.POST.get('nidn_pembimbing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        DosenPembimbing.objects.create(nidn_pembimbing=nidn_pembimbing, name=name, email=email, address=address, gender=gender,
                                       username=username, password=password, mobile=mobile)
    return render(request, 'dashboard_BAAK.html')


def inputregistrationDosPeng(request):
    if request.method == 'POST':
        nidn_penguji = request.POST.get('nidn_penguji')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        DosenPenguji.objects.create(nidn_penguji=nidn_penguji, name=name, email=email, address=address, gender=gender,
                                    username=username, password=password, mobile=mobile)
    return render(request, 'dashboard_BAAK.html')


def inputregistrationKoordinator(request):
    if request.method == 'POST':
        nidn_koordinator = request.POST.get('nidn_koordinator')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        Koordinator.objects.create(nidn_koordinator=nidn_koordinator, name=name, email=email, address=address, gender=gender,
                                   username=username, password=password, mobile=mobile)
    return render(request, 'dashboard_BAAK.html')


# pendataran administratif

def input_pend_adm(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    if request.method == 'POST':
        registration_id = request.POST.get('registration_id')
        group_number = request.POST.get('group_number')
        group_members = request.POST.get('group_members')
        study_program = request.POST.get('study_program')
        supervisor = request.POST.get('supervisor')
        PendaftaranAdministratif.objects.create(
            registration_id=registration_id, group_number=group_number, group_members=group_members, study_program=study_program, supervisor=supervisor)
    return render(request, 'pendaftaran_adm.html', {'profile': profile})


def deletependaftaran(request, pk):
    PendaftaranAdministratif.objects.filter(registration_id=pk).delete()
    return redirect('pendaftaranadmkoorTA')


def editpendaftaran(request, id_pend):
    pendaftaranadmkoorTA = PendaftaranAdministratif.objects.filter(
        registration_id=id_pend)
    return render(request, 'edit pendaftaran adm.html', {'pendaftaran_koorta': pendaftaranadmkoorTA})


def updatependaftaran(request, id_pend):
    pendaftaranadmkoorTA = PendaftaranAdministratif.objects.get(
        registration_id=id_pend)
    form = formpendaftaran(request.POST, instance=pendaftaranadmkoorTA)
    if form.is_valid:
        form.save()
        pendaftaranadmkoorTA = PendaftaranAdministratif.objects.all()
        return redirect('pendaftaranadmkoorTA')


# Scheduling

def input_sche_edit_mhs(request):
    mahasiswa = serializers.deserialize('json', request.session['user'])
    print(mahasiswa)
    profile = None
    for m in mahasiswa:
        profile = m.object
    if request.method == 'POST':
        id_scheduling = request.POST.get('id_scheduling')
        group_number = request.POST.get('group_number')
        group_member = request.POST.get('group_member')
        activity_name = request.POST.get('activity_name')
        date = request.POST.get('date')
        Scheduling.objects.create(
            id_scheduling=id_scheduling, group_number=group_number, group_member=group_member, activity_name=activity_name, date=date)
    return render(request, 'Scheduling_Edit_Mhs.html', {'profile': profile})


def deletescheduling(request, pk):
    Scheduling.objects.filter(id_scheduling=pk).delete()
    return redirect('SchedulingKoordinatorTA')


def editscheduling(request, id_scheduling):
    SchedulingKoordinatorTA = serializers.deserialize(
        'json', request.session['user'])
    print(SchedulingKoordinatorTA)
    profile = None
    for k in SchedulingKoordinatorTA:
        profile = k.object
    SchedulingKoordinatorTA = Scheduling.objects.filter(
        id_scheduling=id_scheduling)
    return render(request, 'Scheduling_Edit_KTA.html', {'scheduling_koorta': SchedulingKoordinatorTA, 'profile': profile})


def updatescheduling(request, id_scheduling):
    SchedulingKoordinatorTA = Scheduling.objects.get(
        id_scheduling=id_scheduling)
    form = schedulingform(request.POST, instance=SchedulingKoordinatorTA)
    if form.is_valid:
        form.save()
        SchedulingKoordinatorTA = Scheduling.objects.all()
        return redirect('SchedulingKoordinatorTA')


# email
def sendemail(request):
    form = emailForm()
    if request.method == 'POST':
        form = emailForm(request.POST)
        if form.is_valid():
            subject = 'Change Password'
            message = 'To reset your password, please reply to this email by sending your username and new password below. If we can find you in the database, the password will be sent to your email address '
            recipient = form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('change-password')
    return render(request, 'password_reset.html', {'form': form})

# BAAK


def baak(request):
    baak = Dahsboard.objects.all()
    return render(request, 'dashboard_BAAK.html')


def list_dospem(request):
    if request.POST:
        keyword = request.POST['search']
        list_dospem = DosenPembimbing.objects.filter(
            username__contains=keyword)
        return render(request, 'update_data_dospem.html', {'list_dospem': list_dospem})
    else:
        list_dospem = DosenPembimbing.objects.all()
        return render(request, 'update_data_dospem.html', {'list_dospem': list_dospem})


def list_dospeng(request):
    if request.POST:
        keyword = request.POST['search']
        list_dospeng = DosenPenguji.objects.filter(username__contains=keyword)
        return render(request, 'update_data_dospeng.html', {'list_dospeng': list_dospeng})
    else:
        list_dospeng = DosenPenguji.objects.all()
        return render(request, 'update_data_dospeng.html', {'list_dospeng': list_dospeng})


def list_koordinator(request):
    if request.POST:
        keyword = request.POST['search']
        list_koordinator = Koordinator.objects.filter(
            username__contains=keyword)
        return render(request, 'update_data_koordinator.html', {'list_koordinator': list_koordinator})
    else:
        list_koordinator = Koordinator.objects.all()
        return render(request, 'update_data_koordinator.html', {'list_koordinator': list_koordinator})


def list_mahasiswa(request):
    if request.POST:
        keyword = request.POST['search']
        list_mahasiswa = Mahasiswa.objects.filter(username__contains=keyword)
        return render(request, 'update_data_mahasiswa.html', {'list_mahasiswa': list_mahasiswa})
    else:
        list_mahasiswa = Mahasiswa.objects.all()
        return render(request, 'update_data_mahasiswa.html', {'list_mahasiswa': list_mahasiswa})

# Update Delete Data


def deleteDataMhs(request, pk):
    Mahasiswa.objects.filter(nim=pk).delete()
    return redirect('list_mahasiswa')


def editDataMhs(request, id_mhs):
    list_mahasiswa = Mahasiswa.objects.filter(nim=id_mhs)
    return render(request, 'edit_data_mhs.html', {'list_mahasiswa':  list_mahasiswa})


def updateDataMhs(request, id_mhs):
    list_mahasiswa = Mahasiswa.objects.get(nim=id_mhs)
    form = mahasiswaform(request.POST, instance=list_mahasiswa)
    if form.is_valid:
        form.save()
        list_mahasiswa = Mahasiswa.objects.all()
        return redirect('list_mahasiswa')


def deleteDataKoordinator(request, pk):
    Koordinator.objects.filter(nidn_koordinator=pk).delete()
    return redirect('list_koordinator')


def editDataKoordinator(request, id_koordinator):
    list_koordinator = Koordinator.objects.filter(
        nidn_koordinator=id_koordinator)
    return render(request, 'edit_data_koordinator.html', {'list_koordinator':  list_koordinator})


def updateDataKoordinator(request, id_koordinator):
    update_koordinator = Koordinator.objects.get(
        nidn_koordinator=id_koordinator)
    form = koordinatorform(request.POST, instance=update_koordinator)
    if form.is_valid:
        form.save()
        update_koordinator = Koordinator.objects.all()
        return redirect('list_koordinator')


def deleteDataDospem(request, pk):
    DosenPembimbing.objects.filter(nidn_pembimbing=pk).delete()
    return redirect('list_dospem')


def editDataDospem(request, id_dospem):
    list_dospem = DosenPembimbing.objects.filter(nidn_pembimbing=id_dospem)
    return render(request, 'edit_data_dospem.html', {'list_dospem':  list_dospem})


def updateDataDospem(request, id_dospem):
    list_dospem = DosenPembimbing.objects.get(nidn_pembimbing=id_dospem)
    form = dospemform(request.POST, instance=list_dospem)
    if form.is_valid:
        form.save()
        list_dospem = DosenPembimbing.objects.all()
        return redirect('list_dospem')


def deleteDataDospeng(request, pk):
    DosenPenguji.objects.filter(nidn_penguji=pk).delete()
    return redirect('list_dospeng')


def editDataDospeng(request, id_dospeng):
    list_dospeng = DosenPenguji.objects.filter(nidn_penguji=id_dospeng)
    return render(request, 'edit_data_dospeng.html', {'list_dospeng': list_dospeng})


def updateDataDospeng(request, id_dospeng):
    list_dospeng = DosenPenguji.objects.get(nidn_penguji=id_dospeng)
    form = dospengform(request.POST, instance=list_dospeng)
    if form.is_valid:
        form.save()
        list_dospeng = DosenPenguji.objects.all()
        return redirect('list_dospeng')

#MEETING MANAGEMENT
#-------Meeting Management Dosen Pembimbing--------#
def inputmeeting(request):
    if request.method == 'POST':
        id_meeting = request.POST.get('meeting_id')
        group_number = request.POST.get('group_number')
        activity = request.POST.get('activity')
        topic = request.POST.get('topic')
        meeting_result = request.POST.get('meeting_result')
        link_media = request.POST.get('link_media')

        MeetingManagement.objects.create(id_meeting=id_meeting, group_number=group_number, activity=activity,
        topic=topic, meeting_result=meeting_result, link_media=link_media)
    return render(request, 'add_meeting.html')

def meeting_management(request):
    meeting = MeetingManagement.objects.all()
    return render(request, 'meeting_management_dopem.html', {'meets' : meeting})

#-------Meeting management Mahasiswa--------#
def meeting_mhs(request):
    meeting = MeetingManagement.objects.all()
    return render(request, 'meeting_management_mahasiswa.html', {'meetings' : meeting})

#-------Meeting management Dosen Penguji--------#
def meeting_dospeng(request):
    meeting = MeetingManagement.objects.all()
    return render(request, 'meeting_dospeng.html', {'meetings' : meeting})

#-------Meeting management Koordinator TA--------#
def meeting_koordinator(request):
    meeting = MeetingManagement.objects.all()
    return render(request, 'meeting_management_KTA.html', {'meetings' : meeting})
