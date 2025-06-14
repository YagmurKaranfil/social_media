# Generated by Django 5.2.1 on 2025-06-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0007_delete_followers_remove_profile_profileimg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profile_img',
            new_name='profileimg',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
