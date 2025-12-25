from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)  # هنوز ذخیره نکن
            
            # پر کردن فیلدهای اتوماتیک
            contact.ip_address = get_client_ip(request)
            contact.user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]
            
            contact.save()
            messages.success(request, "Message sent successfully! ✅")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})



def get_client_ip(request):
    """تابع کمکی برای گرفتن IP کاربر"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
