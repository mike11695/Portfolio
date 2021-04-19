from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.http import HttpResponse

# View for the ndex page aka home page
def index(request):
    # Render the HTML template index.html
    return render(request, 'index.html')

#Method to send a email from the contact form
def send_email(request, id=None):
    if request.method == 'POST':
        sender_name = request.POST.get('fullname')
        sender_email = request.POST.get('email')
        email_subject = request.POST.get('subject')
        email_content = request.POST.get('content') + "<br><br> E-mail from " + sender_email

        #Create the email and send it
        try:
            validate_email(sender_email)
            email = EmailMessage(
                email_subject,
                email_content,
                sender_email,
                ['malopez1195@gmail.com'])
            email.content_subtype = "html"

            try:
                email.send()

                #redirect to index page
                return redirect('index')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        except ValidationError:
            return HttpResponse('Invalid e-mail address given')
    else:
        return HttpResponse('Something went wrong!', status=404)

#page for projects that I've finished
def projects(request):
    # Render the HTML template projects.html
    return render(request, 'projects/projects.html')

#page for practice projects and exercises
def practice(request):
    # Render the HTML template practice.html
    return render(request, 'practice/practice.html')
