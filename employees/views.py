from django.shortcuts import render
from django.views.generic import CreateView , ListView
from reportlab.pdfgen import canvas
from .forms import Add_employ
from django.urls import reverse_lazy
from .models import Employ
from django.http import HttpResponse , FileResponse
import csv 
from .tasks import send_emails



# Create your views here.




class EmploytListView(ListView):
    model = Employ
    template_name = "index.html"

    # call celery task 
    send_emails.delay()




class EmployView(CreateView):
    model = Employ
    form_class = Add_employ
    template_name = 'add_employ.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)
    


def generate_csv(request): 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment; filename="Eployess.csv"'

    writer = csv.writer(response) 
    writer.writerow(['Name', 'Age', 'Job title',
                    'Status', 'Phone', 'Email',
                    'Addres', 'Bio', 'Created at']) 

    emplyess = Employ.objects.all() 
    for employ in emplyess: 
        writer.writerow([employ.name, employ.age, employ.job_title,
                        employ.status, employ.phone, employ.email,
                        employ.addres, employ.bio, employ.created_at]) 

    return response




def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), as_attachment=True,  filename='employ.pdf')
    return response



def generate_pdf_file():
    from io import BytesIO

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Create a PDF document
    emloyess = Employ.objects.all()
    p.drawString(100, 750, "Emloyess")


    y = 700
    for emloy in emloyess:
        p.drawString(100, y, f"Name: {emloy.name}")
        p.drawString(100, y - 20, f"Age: {emloy.age}")
        p.drawString(100, y - 40, f"Job title: {emloy.job_title}")
        p.drawString(100, y -60, f"Status: {emloy.status}")
        p.drawString(100, y - 80, f"Phone: {emloy.phone}")
        p.drawString(100, y - 100, f"Email: {emloy.email}")
        p.drawString(100, y -120, f"Addres: {emloy.addres}")
        p.drawString(100, y - 140, f"Bio: {emloy.bio}")
        p.drawString(100, y - 160, f"Created at: {emloy.created_at}")
        y -= 300

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer