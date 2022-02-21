# Generated by Django 3.2.7 on 2022-01-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Baak',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'baak',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dahsboard',
            fields=[
                ('id_announcement', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=100, null=True)),
                ('body', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=400, null=True)),
                ('post_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dahsboard',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentApproval',
            fields=[
                ('id_document', models.AutoField(primary_key=True, serialize=False)),
                ('no_document', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('file_name', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=100)),
                ('group_number', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('group_members', models.CharField(max_length=200)),
                ('pdf', models.CharField(max_length=300)),
                ('status', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
            ],
            options={
                'db_table': 'document_approval',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DosenPembimbing',
            fields=[
                ('nidn_pembimbing', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('picture', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'dosen_pembimbing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DosenPenguji',
            fields=[
                ('nidn_penguji', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('picture', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'dosen_penguji',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Koordinator',
            fields=[
                ('nidn_koordinator', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=200)),
                ('email', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=100)),
                ('address', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=200)),
                ('gender', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('username', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('password', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=100)),
                ('picture', models.CharField(blank=True, db_collation='utf8mb3_unicode_ci', max_length=200, null=True)),
                ('mobile', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
            ],
            options={
                'db_table': 'koordinator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('nim', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=200)),
                ('username', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=100)),
                ('password', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('gender', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('study_program', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('email', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=100)),
                ('mobile', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('address', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=200)),
                ('picture', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=200)),
                ('id_profile', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
            ],
            options={
                'db_table': 'mahasiswa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MeetingManagement',
            fields=[
                ('id_meeting', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('group_number', models.CharField(max_length=50)),
                ('activity', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
                ('meeting_result', models.CharField(max_length=300)),
                ('link_media', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'meeting_management',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PendaftaranAdministratif',
            fields=[
                ('registration_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('group_number', models.CharField(max_length=200)),
                ('group_members', models.CharField(max_length=200)),
                ('study_program', models.CharField(max_length=200)),
                ('supervisor', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pendaftaran_administratif',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scheduling',
            fields=[
                ('id_scheduling', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50, primary_key=True, serialize=False)),
                ('group_number', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
                ('group_member', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=200)),
                ('activity_name', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=200)),
                ('date', models.CharField(db_collation='utf8mb3_unicode_ci', max_length=50)),
            ],
            options={
                'db_table': 'scheduling',
                'managed': False,
            },
        ),
    ]
