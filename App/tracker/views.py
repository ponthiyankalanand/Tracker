from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import userAdminDetails, locationDetails
from django.contrib.auth.models import User, auth
from .serializers import locationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
import datetime
import hashlib
#for token return sighnup
#from rest_framework.authtoken.models import Token
 
def timehash():
	x = datetime.datetime.now()
	y = (x.strftime("%f"))
	a = str(hash(y))
	h = a [ 1 : 7 ]
	print (h)
	return(h)
def home(request):
	return render(request, 'index.html')
def login(request):
	return render(request, 'login.html')
def adminpage(request):
	uname = request.POST['username']
	upass = request.POST['password']
	#try:
	obj = auth.authenticate(username=uname, password=upass)
	res = not obj
	if res != True:
		userobj = userAdminDetails.objects.get(uname=uname)
		username=userobj.uname
		#print(userobj)
		userID=userobj.userID
		#print (userID)
		obj2 = locationDetails.objects.get(userID=userID)
		#print (obj2)
		print (obj2.latitude,obj2.longitude,username)
		return render(request, 'userAccount.html',{'loc':obj2,'username':username,'userid':userID})

	else:
		messages.info(request,'User name or Password wrong :(')
		return render(request, 'login.html')
	#except:	
		messages.info(request,'Error :(')
		return render(request, 'login.html')
def signup(request):
	return render(request, 'signup.html')
def createAccount(request):
	try:
		if request.method == 'POST':
			uname = request.POST['Name']
			upass = request.POST['password1']
			password2 = request.POST['password2']
			umail = request.POST['Mail_id']
			status = "True"
			userID = timehash()
			if User.objects.filter(username = uname).first():
				messages.error(request, "This username is already taken")
				return render(request,'signup.html')

			elif (password2 == upass):
				AccountDetails = User.objects.create_user(uname, umail, upass)
				Account = userAdminDetails(uname=uname,upass=upass,umail=umail,userID=userID,status=status)
				Account.save()
				AccountDetails.save()
				loc = locationDetails(longitude=1234,latitude=123,userID=userID,count=0)
				loc.save()
				#for token return sighnup
				#token= Token.object.get(user=account).key
				#data['token']   token
				#return Rsponse(data)
				#===================
				#AccountDetails = userAdminDetails(uname=uname,upass=upass,umail=umail,userID=userID,status=status)
				#AccountDetails.save()
				res = not AccountDetails
				if res != True:
					messages.info(request,'Account Creation Success !')
					return render(request, 'login.html')
				else:
					messages.info(request,'Account Creation failed. Try again.')
					return render(request, 'signup.html')	
			else:
				messages.info(request,'Passwords are wrong')
		else:
			messages.info(request,'Account creation failed')
			return render(request, 'login.html')

			
	except:
		return render(request, 'login.html')
@api_view(['POST'])
def apiOverview(request):

	api_urls = {
	'Create':'/task-create/'
	}
	return Response(api_urls)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lockhecker(request):
	serializer = locationSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
@api_view(['POST'])
def fetchtoken(request):
	response={}
	try:
		data=request.data
		username=data['username']
		password=data['password']
		print (username,password)
		obj = auth.authenticate(username=username, password=password)
		res = not obj
		if res != True:
		#return render(request, 'userAccount.html',{'loc':obj2,'username':username,'userid':userID})
			token = Token.objects.get(user_id=obj.id)
			response={'status':'S1177','token':token.key}
		else:
			#print( 'User name or Password wrong ')
			response={'status':'f1177','token':'NULL'}

	except:
		#print ('nope')
		response={'status':'e1177','token':'NULL'}

	return JsonResponse(response)


