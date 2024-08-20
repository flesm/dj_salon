from django.db import models


class CourseModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Номер курса')
    main_name = models.CharField(max_length=50, verbose_name='Название курса')
    extra_name = models.CharField(max_length=50, verbose_name='Дополнительное название')
    cost = models.IntegerField(verbose_name='Цена курса')
    duration = models.IntegerField(verbose_name='Продолжительность курса')
    lessons_num = models.IntegerField(verbose_name='Количество занятий')
    description = models.TextField(verbose_name='Описание')
    course_includes = models.TextField(verbose_name='Курс включает')
    event_form = models.CharField(max_length=30, verbose_name='Форма проведения')
    event_type = models.CharField(
        max_length=30,
        choices=[
            ('И', 'Индивидуальное'),
            ('Г', 'Групповое'),
            ('ИГ', 'Индивидуальное/групповое')
        ],
        verbose_name='Тип проведения',
        default='null'
    )
    issue = models.CharField(max_length=30, verbose_name='Выдается')
    big_img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Большое изображениме')
    mid_img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Среднее изображениме')
    small_img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Маленькое изображениме')

    def __str__(self):
        return self.main_name


