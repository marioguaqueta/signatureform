from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from jsignature.utils import draw_signature
import datetime
from django.utils import timezone
from django.contrib.auth import logout as django_logout
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer 
from reportlab.platypus import Image as rep_image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse
from io import StringIO

from PIL import Image



def login(request):
    if request.user.is_authenticated():
      return redirect('index')
    else :
      loginuser=LoginForm()
      if request.method == "POST":
          loginpost = LoginForm(request.POST)
          if loginpost.is_valid():
             user = authenticate(username=loginpost.data['username'], password=loginpost.data['password'])
             if user is not None:
                 auth_login(request, user)
                 return redirect('index')
             else:
                 print("Login not OK")
                 return render (request, 'form/login.html',{'loginuser':loginuser, 'notvalidcredentials':True})
          else:
              return render (request, 'form/login.html',{'loginuser':loginuser, 'notvaliddata':True})
      return render (request, 'form/login.html',{'loginuser':loginuser})

@login_required(redirect_field_name='login')
def logout(request):
  django_logout(request)
  return redirect('login')

def register(request):
    registeruser=RegisterForm()
    if request.method == "POST":
        registerpost = RegisterForm(request.POST)
        if registerpost.is_valid():
           user = User.objects.create_user(username=registerpost.cleaned_data.get('username'),
                                 email=registerpost.cleaned_data.get('email'),
                                 password=registerpost.cleaned_data.get('password'),
                                 first_name = registerpost.cleaned_data.get('first_name'),
                                 last_name = registerpost.cleaned_data.get('last_name'))
           return redirect('login')
        else:
            return render (request, 'form/register.html',{'registeruser':registeruser, 'notvaliddata':True})
    return render (request, 'form/register.html',{'registeruser':registeruser})    

@login_required(redirect_field_name='login')
def index(request):
    registeruser=SignatureForm()
    if request.method == "POST":
      signature = request.POST.get("signature", "")
      signature_rep = request.POST.get("signature_rep", "")
      print("Tamaño "+str(len(signature))+" Tamaño "+str(len(signature_rep)))
      if len(signature)>0 and len(signature_rep)>0:

        form = AuthDiscountRouster.objects.create(
            name=request.POST.get("name", ""),
            identification=request.POST.get("identification", ""),
            signature=request.POST.get("signature", ""),
            code=request.POST.get("code", ""),
            key=request.POST.get("key", ""),
            legal_rep=request.POST.get("legal_rep", ""),
            nit=request.POST.get("nit", ""),
            signature_rep=request.POST.get("signature_rep", ""))
        request.session['formid'] = form.id
        return render (request, 'form/registersignature.html',{'registeruser':registeruser, 'downloadpdf':True})
      else:
        return render (request, 'form/registersignature.html',{'registeruser':registeruser, 'notsignature':True}) 

      return redirect('index')
    return render (request, 'form/registersignature.html',{'registeruser':registeruser}) 

 
@login_required(redirect_field_name='login')
def viewform(request):

  form = AuthDiscountRouster.objects.filter(id = request.session['formid'])[0]
  file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/documents/"+form.name.replace(" ", "-")+'-descuento-de-nomina.pdf'
  doc = SimpleDocTemplate(file_path,pagesize=letter,
            rightMargin=72,leftMargin=72,
            topMargin=72,bottomMargin=18)

  Story=[]
  tittle = 'AUTORIZACIÓN DE DESCUENTO POR NÓMINA PARA FINANCIACIÓN DE PRIMAS Y RENOVACIONES'
  after_cc = 'Yo '+form.name+'mayor  de  edad,  identificado  (a)  con  la CC. '+form.identification+' autorizo a Capitalizadora Bolívar S.A ó Seguros Bolívar S.A ó  Seguros  Comerciales  Bolívar  S.A,  Asistencia  Bolívar  S.A.  ó  Sociedades  Bolívar  S.A  ó  Seguridad Cia. Administradora de Fondos de Inversión S.A ó Prevención Técnica Ltda. Para que  descuente de mi salario, comisiones mensuales  y/o prestaciones sociales definitivas el valor de las primas de los seguros ofrecidos por Seguros Bolívar S.A y Seguros Comerciales Bolívar S.A'
  signature = 'Firma: '
  signature_picture = draw_signature(form.signature)
  next_cc = 'C.C No: '+form.identification
  code_or_key = 'Código:'+form.code+' ó Clave: '+form.key
  legal_rep_name = 'Representante legal de la agencia: '+form.legal_rep
  nit = 'NIT: '+form.nit
  signature_rep = 'Firma Representante Legal: '
  signature_rep_picture = draw_signature(form.signature_rep)


  background = Image.new("RGB", signature_picture.size, (255, 255, 255))
  background.paste(signature_picture, mask=signature_picture.split()[3]) # 3 is the alpha channel
  signature_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/signatures/"+form.name.replace(" ", "-")+'descuento-de-nomina-signature.jpg'
  background.save(signature_path, 'JPEG', quality=100)

  background = Image.new("RGB", signature_rep_picture.size, (255, 255, 255))
  background.paste(signature_rep_picture, mask=signature_rep_picture.split()[3]) # 3 is the alpha channel
  signature_rep_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/signatures/"+form.name.replace(" ", "-")+'descuento-de-nomina-signature-rep.jpg'
  background.save(signature_rep_path, 'JPEG', quality=100)



  

  styles=getSampleStyleSheet()
  styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER,leading=24))
  ptext = '<font size=18><strong>%s</strong></font>' % tittle
  Story.append(Paragraph(ptext, styles["Center"]))
  Story.append(Spacer(1, 90))
  styles.add(ParagraphStyle(name='Left', alignment=TA_JUSTIFY, leading=18))
  ptext = '<font size=12>%s</font>' % after_cc
  Story.append(Paragraph(ptext, styles["Left"]))
  Story.append(Spacer(4, 12))
  ptext = '<font size=12>%s</font>' %  signature
  Story.append(Paragraph(ptext, styles["Left"]))
  image = rep_image(signature_path, width=signature_picture.size[0], height=signature_picture.size[1])
  # image.hAlign = 'LEFT'
  Story.append(image)
  Story.append(Spacer(4, 12))
  ptext = '<font size=12>%s</font>' % next_cc
  Story.append(Paragraph(ptext, styles["Left"]))
  Story.append(Spacer(4, 12))
  ptext = '<font size=12>%s</font>' % code_or_key
  Story.append(Paragraph(ptext, styles["Left"]))
  Story.append(Spacer(4, 12))
  ptext = '<font size=12>%s</font>' % legal_rep_name
  Story.append(Paragraph(ptext, styles["Left"]))
  Story.append(Spacer(4, 12))
  ptext = '<font size=12>%s</font>' % nit
  Story.append(Paragraph(ptext, styles["Left"]))
  Story.append(Spacer(4, 12))
  ptext = '<font size=12>%s</font>' % signature_rep
  Story.append(Paragraph(ptext, styles["Left"]))
  image = rep_image(signature_rep_path, width=signature_rep_picture.size[0], height=signature_rep_picture.size[1])
  Story.append(image)
  Story.append(Spacer(4, 12))

  doc.build(Story)
  if os.path.exists(file_path):
    with open(file_path, 'rb') as fh:
      response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
      response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
      return response
  



