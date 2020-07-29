from django.shortcuts import render
from django.shortcuts import redirect
from testapp.models import *
from testapp import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
import datetime



# Create your views here.
def home_view(request):
    return render(request, 'testapp/home.html')
def contact_view(request):
    return render(request, 'testapp/contact.html')
@login_required
def student_info_view(request):
    students=Student.objects.all()
    return render(request,'testapp/results.html',{'students':students})

def enquiry_info_view(request):
    form=forms.enquiry_form()
    if request.method=='POST':
        form=forms.enquiry_form(request.POST)
        if form.is_valid():
            print('submitted form is valid priting info')
            fname=form.cleaned_data['name']
            fphone=form.cleaned_data['phone']
            femail=form.cleaned_data['email']
            fmessage=form.cleaned_data['message']
            dd=str(datetime.datetime.today()).split()[0]
            record=Enquiry.objects.get_or_create(date_s=dd,name=fname,phone=fphone,email=femail,message=fmessage)
            ## mail

            subject='Welcome to Doffadils school'
            message = 'Hi'+" "+ fname+ ",\n"
            recepient =[]
            recepient.append(femail)
            recepient.append(settings.EMAIL_HOST_USER)
            message=message+'We got your request, our executive will be get in touch with you shortly '+"\n name:"+ fname +"\n email:"+femail+"\n message:"+fmessage
            if 0:
                send_mail(subject,message, settings.EMAIL_HOST_USER, recepient, fail_silently = False)
            else:
                html_content='<h3>Hi </h3>'+'<h3>'+ fname+',</h3>' +'<h3>We got your request,our executive will be get in touch with you shortly</h3>'+'\n'+'phone:'+fphone+'\n'+'email:'+ femail+'\n'+'message:'+fmessage
                email = EmailMessage(
                subject,
                html_content,
                settings.EMAIL_HOST_USER,
                recepient,
                headers={'Message-ID': 'foo'},
                )

                email.content_subtype = "html"
                #email.attach('D:\\abc\schoolproj\static\images\school_msg.jpg', message, 'image/png')
                email.attach_file('D:\\abc\schoolproj\static\images\img1.jpg')
                email.send()
                print('email sent')
            return render(request,'testapp/contact.html',{'form':form})



    return render(request,'testapp/enquiry.html',{'form':form})

@login_required
def enquiry_report_view(request):
    enquirys=Enquiry.objects.all()
    return render(request,'testapp/enquiry_results.html',{'enquirys': enquirys})

@login_required
def SM_upload_view(request):
    form=forms.SM_upload_form()
    if request.method=='POST':
        form=forms.SM_upload_form(request.POST,request.FILES)
        if form.is_valid():
            print('valid SM form')
            form.save()
        else:
            print('not valid SM form')
    return render(request, 'testapp/aupload.html',{'form':form,'title':'Study Material UPLOAD Form'})

@login_required
def RV_upload_view(request):
    form=forms.RV_upload_form()
    if request.method=='POST':
        form=forms.RV_upload_form(request.POST,request.FILES)
        if form.is_valid():
            print('valid RV form')
            form.save()
        else:
            print('not valid RV form')
    return render(request, 'testapp/aupload.html',{'form':form,'title':'Recorded Videos UPLOAD Form'})

@login_required
def Rlink_upload_view(request):
    form=forms.Rlink_upload_form()
    if request.method=='POST':
        form=forms.Rlink_upload_form(request.POST,request.FILES)
        if form.is_valid():
            print('valid Recordings form')
            form.save()
        else:
            print('not valid Recordings form')
    return render(request, 'testapp/aupload.html',{'form':form,'title':'Recordings Links upload Form'})

@login_required    #########Modelformset############
def SM_upload_formset_view(request):
    #form=forms.SM_upload_form()
    #SM_formset=modelformset_factory(SM_upload,form=forms.SM_upload_form,extra=1)

    SM_formset=formset_factory(forms.SM_upload_form,extra=2)
    formset=SM_formset()
    if request.method=='POST':
        SM_formset=formset_factory(forms.SM_upload_form,extra=1)
        formset=SM_formset(request.POST,request.FILES)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
                form.save()
            print('valid SM formset')
            #formset.save() # no method exist
        else:
            print('not valid SM formset')
    return render(request, 'testapp/aupload.html',{'form':formset})

######new fucntion assingment submission report

def AS_report_query_form_view(request):
    if request.method=='POST':
        form=forms.Assignment_report_query_form(request.POST)
        if form.is_valid():
            print('xxxx',type(form['report_choice_field']))
            status=form.cleaned_data['report_choice_field']
            print('status',status)
            if status =='submitted' :
                print('as report form is valid status x  :', status)
                asreports=Assignment_submission.objects.filter(status="submitted")
                print('xxxxxxxxxxxxxxx:', status)
            else:
                print('as report form is valid status y:', status)
                asreports=Assignment_submission.objects.filter(status="NotSubmit")
                print('yyyyyyyyyyyyyyy:', status)
            # if status.value()==1:
            #     asreports=Assignment_submission.objects.filter(status='submitted')
            # else:
            #     asreports=Assignment_submission.objects.filter(status='NotSubmit')
            return render(request,'testapp/as_results.html',{'asreports':asreports,'title':'Assignment Material Submission Report','recs':asreports})
    else:
        form=forms.Assignment_report_query_form()
        return render(request,'testapp/as_results.html',{'title':'Assignment Material Submission Report','form':form})

def assignment_completed_report_view(request):
    try:
        my_dict=request.session['my_dict']
        sname=my_dict['sname']
    except KeyError:
        message='KeyError exeception occured'
        print(message +' my_dict zero in student_online_view'+' redirecting login to page')
        return redirect('/accounts/login/')

    if request.method=='POST':
        form=forms.Assignment_report_query_form(request.POST)
        if form.is_valid():
            print('xxxx',type(form['report_choice_field']))
            status=form.cleaned_data['report_choice_field']
            print('status',status)
            if status =='submitted' :
                print('as report form is valid status x  :', status)
                asreports=Assignment_submission.objects.filter(status="submitted",student_name=sname)

            else:
                print('as report form is valid status y:', status)
                asreports=Assignment_submission.objects.filter(status="NotSubmit",student_name=sname)

            return render(request,'testapp/as_results.html',{'asreports':asreports,'title':'Assignment Material Submission completed Report','recs':asreports})
    else:
        form=forms.Assignment_report_query_form()
        return render(request,'testapp/as_results.html',{'title':'Assignment Material Submission completed Report','form':form})

@login_required
def SM_report_view(request):
    areports=SM_upload.objects.all()
    return render(request,'testapp/a_results.html',{'areports':areports,'title':'Study Material Report'})

@login_required
def RV_report_view(request):
    areports=RV_upload.objects.all()
    return render(request,'testapp/a_results.html',{'areports':areports,'title':'Recorded Videos Report'})

@login_required
def Rlink_report_view(request):
    areports=Rlink_upload.objects.all()
    return render(request,'testapp/r_results.html',{'areports':areports,'title':'Recording Links Report'})

def logout_view(request):
    try:
        del request.session['my_dict']
    except KeyError:
        pass
    return render(request,'testapp/logout.html')

@login_required
def student_home_view(request):
    my_dict={}
    rec=Student.objects.filter(sname=request.user.username)
    for r in rec:
        my_dict['email']=r.email
        my_dict['classx']=r.classx
        my_dict['section']=r.section
        my_dict['sname']=r.sname
        print('email',r.email)
    request.session['my_dict']=my_dict  #copy my_dict{}  to session
    return render(request,'testapp/shome.html',my_dict)

# Assignment view page
def student_assignments_view(request):
    return student_assignments_common(request,'All')
#Assignment Links
def student_assignments_maths_view(request):
    return student_assignments_common(request,'Maths')

def student_assignments_english_view(request):
    return student_assignments_common(request,'English')

def student_assignments_science_view(request):
    return student_assignments_common(request,'Science')

def student_assignments_hindi_view(request):
    return student_assignments_common(request,'Hindi')

def student_assignments_telugu_view(request):
    return student_assignments_common(request,'Telugu')


def student_online_view(request):
    try:
        my_dict=request.session['my_dict']
        return render(request,'testapp/sonline.html',my_dict)
    except KeyError:
        message='KeyError exeception occured'
        print(message +' my_dict zero in student_online_view'+' redirecting login to page')
        return redirect('/accounts/login/')

#Study Material page
def student_home_study_material(request):
    return sub_route_fun(request,'All')

# Study Material child links
def student_subject_Maths_view(request):
    return sub_route_fun(request,'Maths')

def student_subject_Science_view(request):
    return sub_route_fun(request,'Science')

def student_subject_English_view(request):
    return sub_route_fun(request,'English')

def student_subject_Hindi_view(request):
    return sub_route_fun(request,'Hindi')

def student_subject_Telugu_view(request):
    return sub_route_fun(request,'Telugu')

#Assignment Submission page
def assignment_submission_view(request):
    return sub_assigment_submission_common(request,'All')

#Assignment Submission child links
def assignment_submission_maths_view(request):
    return sub_assigment_submission_common(request,'Maths')

def assignment_submission_english_view(request):
    return sub_assigment_submission_common(request,'English')

def assignment_submission_science_view(request):
    return sub_assigment_submission_common(request,'Science')

def assignment_submission_hindi_view(request):
    return sub_assigment_submission_common(request,'Hindi')

def assignment_submission_telugu_view(request):
    return sub_assigment_submission_common(request,'Telugu')

def test_video_play_view(request):
    return render(request, 'testapp/videop.html',{'rl':'https://www.youtube.com/watch?v=wdlvvQe3F8I'})
#### local fucntion
def sub_route_fun(request,lang):
    try:
        my_dict=request.session.get('my_dict',0)
        classx=my_dict['classx']
        if lang=='All':
            recs=SM_upload.objects.filter(std=classx)
        else:
            recs=SM_upload.objects.filter(std= int(classx),subject=lang)
        return render(request,'testapp/shomesm.html',{'recs':recs,'title':'study material','my_dict':my_dict})
    except:
        print('my_dict zero in {} sty Material sub_route_fun'.format(lang))
        return redirect('/accounts/login')

def sub_assigment_submission_common(request,lang):
    try:
        my_dict=request.session['my_dict']
        classx=my_dict['classx']
        sname=my_dict['sname']
        print('classx:',classx)
        if lang=='All':
            assignments=Assignment.objects.filter(std=classx)
            acount=Assignment.objects.filter(std=classx).count() # new
        else:
            assignments=Assignment.objects.filter(std=classx,subject=lang)
            acount=Assignment.objects.filter(std=classx,subject=lang).count() # new
    except KeyError:
        message='KeyError exeception occured'
        print(message +' my_dict zero in sub_assigment_submission_common '+ lang +' redirecting login to page')
        return redirect('/accounts/login/')

    #form1=forms.Assignment_form()
    #form=forms.Assignment_submission_form()
    #my_dict={'form':form,'form1':form1,'title':'assignments submission','assignments':assignments}

    ####
    # if acount:
    #     form1=forms.Assignment_form()
    #     form=forms.Assignment_submission_form()
    #     my_dict={'form':form,'form1':form1,'title':'assignments submission','assignments':assignments}
    # else:
    my_dict={'title':'assignments submission','assignments':assignments}
    ##
    # if request.method=='POST' :
    #     form1=forms.Assignment_form(request.POST)
    #     form=forms.Assignment_submission_form(request.POST,request.FILES)
    #     if form1.is_valid():
    #         print('form1 is valid')
    #         obj=form1['aid'].value()
    #         print('obj',obj)
    #         record=Assignment.objects.get(id=obj)
    #
    #     else:
    #         print('form1 is Not valid')
    #     if form.is_valid():
    #         print('form is valid')
    #
    #         student_name=sname
    #         print('student_name',student_name)
    #         submission_attach=form['submission_attach'].value()
    #         submission_attach1=form['submission_attach1'].value()
    #         submission_attach2=form['submission_attach2'].value()
    #         print('submission_attach',form.cleaned_data['submission_attach'])
    #         status=form['status'].value()
    #
    #         initial={'assignment':record,
    #         'student_name':student_name,
    #         'submission_attach':submission_attach,
    #         'submission_attach1':submission_attach1,
    #         'submission_attach2':submission_attach2,
    #         'status':status
    #         }
    #
    #         form2=forms.Assignment_submission_form(initial,request.FILES)
    #         print ('from 2 assignment', form2['assignment'].value())
    #         print ('from 2student_name', form2['student_name'].value())
    #         print ('from 2 submission_attach', form2['submission_attach'].value())
    #         print ('from 2 status', form2['status'].value())
    #
    #         form2.save()
    return render(request,'testapp/shomeasm.html',my_dict) #asupload

##
def sub_assigment_submission_new_view(request,id):
    try:
        my_dict=request.session['my_dict']
        classx=my_dict['classx']
        sname=my_dict['sname']
        print('classx:',classx)
        assignments=Assignment.objects.filter(std=classx)
        acount=Assignment.objects.filter(std=classx).count()
        print('id',id)
    except KeyError:
        message='KeyError exeception occured'
        print(message +' my_dict zero in sub_assigment_submission_common '+ lang +' redirecting login to page')
        return redirect('/accounts/login/')

    #form1=forms.Assignment_form()
    if acount:
        form=forms.Assignment_submission_form()
        my_dict={'form':form,'id':id,'student_name':sname,'title':'assignments submission','assignments':assignments,'acount':acount}
    else:
        my_dict={'id':id,'student_name':sname,'title':'assignments submission','assignments':assignments,'acount':acount}
    if request.method=='POST' :

        form=forms.Assignment_submission_form(request.POST,request.FILES)

        if form.is_valid():
            print('form is valid')

            student_name=sname
            print('student_name',student_name)
            submission_attach=form['submission_attach'].value()
            submission_attach1=form['submission_attach1'].value()
            submission_attach2=form['submission_attach2'].value()
            print('submission_attach',form.cleaned_data['submission_attach'])
            status=form['status'].value()

            initial={'assignment':id,
            'student_name':student_name,
            'submission_attach':submission_attach,
            'submission_attach1':submission_attach1,
            'submission_attach2':submission_attach2,
            'status':status
            }

            form2=forms.Assignment_submission_form(initial,request.FILES)
            print ('from 2 assignment', form2['assignment'].value())
            print ('from 2student_name', form2['student_name'].value())
            print ('from 2 submission_attach', form2['submission_attach'].value())
            print ('from 2 status', form2['status'].value())

            form2.save()
            return redirect('/sassignsub')
    return render(request,'testapp/shomeasm_xxx.html',my_dict) #asupload
def student_assignments_common(request,lang):
    try:
        my_dict=request.session['my_dict']
        print('my_dict', my_dict)
        classx=my_dict['classx']


        print('classx', classx)
        if lang=='All':
            recs=Assignment.objects.filter(std=int(classx))
        else:
            recs=Assignment.objects.filter(std= int(classx),subject=lang)
        title='assignment material'
        return render(request,'testapp/shomeam.html',{'recs':recs,'title':title})
    except KeyError:
        message='KeyError exeception occured'
        print(message +' my_dict zero in assignment Material view '+lang+' redirecting login to page')
        return redirect('/accounts/login/')
