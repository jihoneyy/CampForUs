# Generated by Django 3.1.7 on 2021-04-02 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campsite',
            fields=[
                ('campsite_id', models.AutoField(primary_key=True, serialize=False)),
                ('campsite_name', models.CharField(max_length=30)),
                ('lineintro', models.CharField(blank=True, max_length=100, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('featureNmV', models.TextField(blank=True, db_column='featureNmV', null=True)),
                ('indutyV', models.CharField(blank=True, db_column='indutyV', max_length=200, null=True)),
                ('lctCI', models.CharField(blank=True, db_column='lctCl', max_length=50, null=True)),
                ('doNm', models.CharField(blank=True, db_column='doNm', max_length=20, null=True)),
                ('sigunguNm', models.CharField(blank=True, db_column='sigunguNm', max_length=20, null=True)),
                ('addr1', models.CharField(blank=True, max_length=50, null=True)),
                ('addr2', models.CharField(blank=True, max_length=30, null=True)),
                ('mapX', models.CharField(blank=True, db_column='mapX', max_length=20, null=True)),
                ('mapY', models.CharField(blank=True, db_column='mapY', max_length=20, null=True)),
                ('tel', models.CharField(blank=True, max_length=300, null=True)),
                ('homepage', models.TextField(blank=True, null=True)),
                ('resveUrl', models.TextField(blank=True, db_column='resveUrl', null=True)),
                ('resveCl', models.CharField(blank=True, db_column='resveCl', max_length=100, null=True)),
                ('gnrlSiteCo', models.CharField(db_column='gnrlSiteCo', max_length=5)),
                ('autoSiteCo', models.CharField(db_column='autoSiteCo', max_length=5)),
                ('glampSiteCo', models.CharField(db_column='glampSiteCo', max_length=5)),
                ('caravSiteCo', models.CharField(db_column='caravSiteCo', max_length=5)),
                ('tooltip', models.TextField(blank=True, null=True)),
                ('glampInnerFclty', models.CharField(blank=True, db_column='glampInnerFclty', max_length=100, null=True)),
                ('caravInnerFclty', models.CharField(blank=True, db_column='caravInnerFclty', max_length=100, null=True)),
                ('operPdCl', models.CharField(blank=True, db_column='operPdCl', max_length=50, null=True)),
                ('operDeCl', models.CharField(blank=True, db_column='operDeCl', max_length=30, null=True)),
                ('trlerAcmpnyAt', models.CharField(db_column='trlerAcmpnyAt', max_length=5)),
                ('brazierCl', models.CharField(blank=True, db_column='brazierCl', max_length=20, null=True)),
                ('sbrsEtc', models.CharField(blank=True, db_column='sbrsEtc', max_length=200, null=True)),
                ('posblFcltyCl', models.CharField(blank=True, db_column='posblFcltyCl', max_length=300, null=True)),
                ('posblFcltyEtc', models.CharField(blank=True, db_column='posblFcltyEtc', max_length=300, null=True)),
                ('clturEventAt', models.CharField(db_column='clturEventAt', max_length=5)),
                ('clturEvent', models.CharField(blank=True, db_column='clturEvent', max_length=200, null=True)),
                ('exprnProgrmAt', models.CharField(db_column='exprnProgrmAt', max_length=5)),
                ('exprnProgrm', models.CharField(blank=True, db_column='exprnProgrm', max_length=300, null=True)),
                ('themaEnvrnCl', models.CharField(blank=True, db_column='themaEnvrnCl', max_length=300, null=True)),
                ('eqpmnLendCl', models.CharField(blank=True, db_column='eqpmnLendCl', max_length=100, null=True)),
                ('animalCmgCl', models.CharField(blank=True, db_column='animalCmgCl', max_length=100, null=True)),
                ('firstImageUrlV', models.CharField(blank=True, db_column='firstImageUrlV', max_length=300, null=True)),
                ('likeCount', models.IntegerField(db_column='likeCount')),
            ],
            options={
                'db_table': 'Campsite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampsiteSbrscl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Campsite_SbrsCl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampsiteTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Campsite_Tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Likes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sbrscl',
            fields=[
                ('sbrscl_id', models.AutoField(db_column='sbrsCl_id', primary_key=True, serialize=False)),
                ('sbrscl_name', models.CharField(db_column='sbrsCl_name', max_length=100)),
            ],
            options={
                'db_table': 'SbrsCl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('admin', models.IntegerField()),
                ('birth', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
