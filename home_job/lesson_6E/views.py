from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string


def get_letter(request):
    htmlmessage = render_to_string('letter.html')
    send_mail('Tema', 'Hi people!!!!!', 'from@Kolia.com',
              ['bogdanovichkolia1990@gmail.com'],
              html_message=htmlmessage)
    return HttpResponse('sent!')
