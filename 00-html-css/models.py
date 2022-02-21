# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dahsboard(models.Model):
    id_pengumuman = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    body = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dahsboard'


class DataJadwal(models.Model):
    id_jadwal = models.CharField(db_column='ID_Jadwal', primary_key=True, max_length=20)  # Field name made lowercase.
    nim = models.ForeignKey('Mahasiswa', models.DO_NOTHING, db_column='NIM', blank=True, null=True)  # Field name made lowercase.
    nama_kegiatan = models.CharField(db_column='Nama_Kegiatan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tanggal = models.DateField(db_column='Tanggal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_jadwal'


class DataMahasiswa(models.Model):
    password = models.CharField(db_column='Password', primary_key=True, max_length=50)  # Field name made lowercase.
    nim = models.ForeignKey('Mahasiswa', models.DO_NOTHING, db_column='NIM', blank=True, null=True)  # Field name made lowercase.
    artefak = models.CharField(db_column='Artefak', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kelompok = models.CharField(db_column='Kelompok', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_mahasiswa'


class DataPengumuman(models.Model):
    id_pengumuman = models.CharField(db_column='ID_Pengumuman', primary_key=True, max_length=20)  # Field name made lowercase.
    nim = models.ForeignKey('Mahasiswa', models.DO_NOTHING, db_column='NIM', blank=True, null=True)  # Field name made lowercase.
    nama_pengumuman = models.CharField(db_column='Nama_Pengumuman', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tanggal = models.DateField(db_column='Tanggal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_pengumuman'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentApproval(models.Model):
    id_document = models.AutoField(primary_key=True)
    no_document = models.IntegerField(blank=True, null=True)
    nama_file = models.CharField(max_length=50, blank=True, null=True)
    file_dokumen = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document approval'


class DosenPembimbing(models.Model):
    nidn = models.CharField(db_column='NIDN', primary_key=True, max_length=50)  # Field name made lowercase.
    nama_dosen = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dosen_pembimbing'


class DosenPenguji(models.Model):
    nidn = models.CharField(db_column='NIDN', primary_key=True, max_length=50)  # Field name made lowercase.
    nama_dosen = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dosen_penguji'


class KoordinatorTa(models.Model):
    id_ta = models.CharField(db_column='ID_TA', primary_key=True, max_length=20)  # Field name made lowercase.
    nidn = models.CharField(db_column='NIDN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nama = models.CharField(max_length=50, blank=True, null=True)
    jenis_kelamin = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'koordinator_ta'


class Mahasiswa(models.Model):
    nim = models.CharField(db_column='NIM', primary_key=True, max_length=20)  # Field name made lowercase.
    no_kelompok = models.CharField(db_column='No_Kelompok', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nama_mahasiswa = models.CharField(db_column='Nama_Mahasiswa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=50, blank=True, null=True)
    prodi = models.CharField(db_column='Prodi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alamat = models.CharField(db_column='Alamat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=50, blank=True, null=True)
    jenis_kelamin = models.CharField(db_column='Jenis_Kelamin', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mahasiswa'


class MeetingManagement(models.Model):
    id_meeting = models.AutoField(primary_key=True)
    no_kelompok = models.IntegerField(blank=True, null=True)
    nama_kegiatan = models.CharField(max_length=50, blank=True, null=True)
    hasil_meeting = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_management'


class Nilai(models.Model):
    no_kelompok = models.CharField(db_column='No_Kelompok', primary_key=True, max_length=20)  # Field name made lowercase.
    nidn = models.CharField(db_column='NIDN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    jumlah_nilai = models.CharField(db_column='Jumlah_Nilai', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nilai'


class PendaftaranAdministratif(models.Model):
    id_pendaftaran = models.AutoField(primary_key=True)
    no_kelompok = models.IntegerField(blank=True, null=True)
    nama_anggota = models.CharField(max_length=50, blank=True, null=True)
    dosen_pembimbing = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pendaftaran_administratif'


class Person(models.Model):
    nim = models.CharField(db_column='NIM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_person = models.CharField(primary_key=True, max_length=50)
    nama = models.CharField(max_length=50, blank=True, null=True)
    prodi = models.CharField(max_length=50, blank=True, null=True)
    angkatan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Scheduling(models.Model):
    id_scheduling = models.AutoField(primary_key=True)
    no_kelompok = models.IntegerField(blank=True, null=True)
    nama_anggota = models.CharField(max_length=50, blank=True, null=True)
    nama_kegiatan = models.CharField(max_length=50, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scheduling'


class User(models.Model):
    username = models.CharField(db_column='Username', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'
