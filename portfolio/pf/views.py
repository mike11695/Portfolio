from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    # Render the HTML template index.html
    return render(request, 'index.html')

#Method to send a email from the contact form
def send_email(request, id=None):
    if request.method == 'POST':
        sender_name = request.POST.get('fullname')
        sender_email = request.POST.get('email')
        email_subject = request.POST.get('subject')
        email_content = request.POST.get('content')

        #Create the email and send it
        try:
            validate_email(sender_email)

            try:
                send_mail(
                    email_subject,
                    email_content,
                    sender_email,
                    ['malopez1195@gmail.com'],
                    fail_silently=False,
                )

                #redirect to index page
                return redirect('index')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        except ValidationError:
            return HttpResponse('Invalid e-mail address given')
    else:
        return HttpResponse('Something went wrong!', status=404)
