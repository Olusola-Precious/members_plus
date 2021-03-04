from django.shortcuts import render, redirect
from .models import Members, Organizations
# from datetime import datetime as dt
import time

# Create your views here.

temp_user, temp_password = ("realadmin", "admin")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        #if (username == temp_user) and (password == temp_password):
        OrgIDs = [o.OrgID for o in Organizations.objects.all()]
        # print(OrgIDs)
        if username in OrgIDs :  # == 'MP-710374':
            OrgPass = Organizations.objects.get(OrgID=username)
            if password == OrgPass.password:
                request.session['orgID'] = username
                return redirect('home')
            else:
                return render(request, 'login.html', {'message':'Wrong Credentials'})

        else:
            return render(request, 'login.html', {'message':'Wrong Credentials'})

    return render(request, 'login.html', {})


def logout(request):
    try:
        del request.session['orgID']
    except:
        pass
    return redirect('login')

def index(request):
    orgid = request.session.get('orgID', None)
    print(orgid)
    org = Organizations.objects.get(OrgID=orgid)
    # print(org)
    all_members = Members.objects.filter(id=org.id)
    return render(request, 'admin.html', {'members': all_members, 'org':org})

def edit(request):
    id = request.GET.get('id', None)
    if id is None:
        return redirect('home')

    member = Members.objects.get(id=id)
    return render(request, "edit.html", {'member': member})

def view(request):
    id = request.GET.get('id', None)
    if id is None:
        return redirect('home')
    
    member = Members.objects.get(id=id)

    return render(request, "view.html", {'member':member})

def addMember(request):
    if request.method == 'POST':
        orgid = request.session['orgID']
        org = Organizations.objects.get(OrgID=orgid)
        # DOB = request.POST['DOB']
        #print(request.POST.keys())
        ID = 'MCP-'+ str(int(time.time()))[5:]
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        phone = request.POST['phoneNo']
        email = request.POST['email']
        DOB = request.POST['DOB']
        gender = request.POST['gender']
        bloodGroup = request.POST['bloodGroup']
        maritalStat = request.POST['maritalStat']
        country = request.POST['country']
        home = request.POST['homeAddress']
        state = request.POST['sateOForigin']
        LGA = request.POST['LGA']
        nextofkin = request.POST['nextOfKin']
        qual = request.POST['highQual']
        occupation = request.POST['occupation']
        proff = request.POST['proffession']
        position = request.POST['positionHeld']
        role = request.POST['role']
        office = request.POST['offAddress']
        try:
            img = request.FILES['photo']
        except KeyError: 
            img = ''
        
        other = request.POST['otherInfo']


        # FdefaultImg = "img/passportplaceholder.jpg"
        # MdefaultImg = "img/passportplaceholderM.jpg"

        # print(locals())
        
        # print(type(firstname))
        new = Members.objects.create(
            orgID = org,
            memberID = ID,
            firstname = firstname,
            lastname = lastname,
            phone_number = phone,
            email = email,
            DOB = DOB,
            gender = gender,
            bloodGroup = bloodGroup,
            maritalStatus = maritalStat,
            country = country, 
            residentialAddress = home,
            stateOfOrigin = state,
            LGA = LGA,
            nextOfKin = nextofkin,
            highestQual = qual,
            occupation = occupation,
            proffession = proff,
            positionHeld = position,
            officeAddress = office,
            role = role,
            otherInfo = other,
            profileImg = img 
        )

        new.save()
        return redirect('home')
    return render(request, "add.html", {})
