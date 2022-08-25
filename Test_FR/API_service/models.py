from datetime import timezone

import pytz
from django.core.validators import RegexValidator
from django.db import models


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone_regex = RegexValidator(regex='^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=12, verbose_name='телефон')
    mobile_op = models.CharField(blank=False, max_length=5, verbose_name='моб оператор')
    tag = models.CharField(max_length=100, blank=True, verbose_name='метка клиента')
    timezone = models.CharField(max_length=32, choices=TIMEZONES, verbose_name='часовой пояс', default='UTC')
    # TZ_CHOICES = (
    #     ('UTC-12', 'UTC-12'),
    #     ('UTC-11', 'UTC-11'),
    #     ('UTC-10', 'UTC-10'),
    #     ('UTC-9', 'UTC-9'),
    #     ('UTC-8', 'UTC-8'),
    #     ('UTC-7', 'UTC-7'),
    #     ('UTC-6', 'UTC-6'),
    #     ('UTC-5', 'UTC-5'),
    #     ('UTC-4', 'UTC-4'),
    #     ('UTC-3', 'UTC-3'),
    #     ('UTC-2', 'UTC-2'),
    #     ('UTC-1', 'UTC-1'),
    #     ('UTC', 'UTC'),
    #     ('UTC+1', 'UTC+1'),
    #     ('UTC+2', 'UTC+2'),
    #     ('UTC+3', 'UTC+3'),
    #     ('UTC+4', 'UTC+4'),
    #     ('UTC+5', 'UTC+5'),
    #     ('UTC+6', 'UTC+6'),
    #     ('UTC+7', 'UTC+7'),
    #     ('UTC+8', 'UTC+8'),
    #     ('UTC+9', 'UTC+9'),
    #     ('UTC+10', 'UTC+10'),
    #     ('UTC+11', 'UTC+11'),
    #     ('UTC+12', 'UTC+12'),
    # )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Клиент {self.id} с номером {self.phone_number}'


class Mailing(models.Model):
    time_create = models.DateTimeField(verbose_name='время создания рассылки')
    text = models.TextField(blank=True, verbose_name='текст сообщения')
    mob_codes = models.CharField(max_length=50, blank=True, verbose_name='код моб оператора')
    tag = models.CharField(max_length=50, blank=True, verbose_name='метка клиента')
    time_end = models.DateTimeField(verbose_name='время окончания рассылки')

    @property
    def to_send(self):
        now = timezone.now()
        if self.beginning <= now <= self.ending:
            return True
        else:
            return False

    @property
    def sent_messages(self):
        return len(self.messages.filter(status='sent'))

    @property
    def messages_to_send(self):
        return len(self.messages.filter(status='proceeded'))

    @property
    def unsent_messages(self):
        return len(self.messages.filter(status='failed'))

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'Рассылка {self.id} от {self.time_create}'


class Message(models.Model):
    SENT = "sent"
    NO_SENT = "no sent"

    STATUS_CHOICES = [
        (SENT, "Sent"),
        (NO_SENT, "No sent"),
    ]

    date = models.DateTimeField(verbose_name='Дата отправки', auto_now_add=True)
    status = models.CharField(verbose_name='Статус отправки', max_length=15, choices=STATUS_CHOICES)
    message = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Сообщение {self.id} с текстом {self.message} для {self.client}'