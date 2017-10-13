from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


class HomeView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    
class PostView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

def contact(request):
    form_class = ContactForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('blog/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Dime Drop Times" +'',
                ['roflbot101@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/pages/success')

    return render(request, "blog/contact.html", {
        'form': form_class,
    })

