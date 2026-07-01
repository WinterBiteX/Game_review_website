import cloudinary.uploader
import os
from django.shortcuts import render,redirect
from GameApp.models import Category_Db,Game_Db,Requirement_Db,Upcoming_Db,Fan_Favorite_Db
from django.http import JsonResponse
from WebApp.models import Contact_Db,Login_Db,Comment_Db,Favorite_Db,Blog_Share
from django.contrib import messages
from django.utils.timesince import timesince
from django.core.validators import validate_email
from django.core.exceptions import ValidationError




# def home_page(request):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     cat = Category_Db.objects.all()
#     up_come = Upcoming_Db.objects.all()
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"home_page.html",{"cat":cat,"image":image,"up_come":up_come,"fav_count":fav_count})
def home_page(request):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    cat = Category_Db.objects.all()
    up_come = Upcoming_Db.objects.all()
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"home_page.html",{"cat":cat,"image":image,"up_come":up_come,"fav_count":fav_count})




# def game_page(request):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     data = Game_Db.objects.all()
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"game_page.html",{"data":data,"image":image,"fav_count":fav_count})
def game_page(request):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    data = Game_Db.objects.all()
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"game_page.html",{"data":data,"image":image,"fav_count":fav_count})




# def game_details(request,game_id):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     data = Game_Db.objects.get(id = game_id)
#     game_name = Game_Db.objects.get(id = game_id).Game_Name
#     requirements = Requirement_Db.objects.filter(Requirement_Game = game_name)
#     filter = Game_Db.objects.get(id=game_id).Game_Category
#     similar = Game_Db.objects.filter(Game_Category = filter).exclude(id = game_id)
#     is_favorite = Favorite_Db.objects.filter(Fav_User = name,Fav_Gname = game_name).exists()
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"game_details.html",{"data":data,"requirement":requirements,"image":image,"similar":similar,
#                                                "is_favorite":is_favorite,"game_id":game_id,"fav_count":fav_count})
def game_details(request,game_id):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    data = Game_Db.objects.get(id=game_id)
    game_name = Game_Db.objects.get(id=game_id).Game_Name
    requirements = Requirement_Db.objects.filter(Requirement_Game=game_name)
    filter = Game_Db.objects.get(id=game_id).Game_Category
    similar = Game_Db.objects.filter(Game_Category=filter).exclude(id=game_id)
    is_favorite = Favorite_Db.objects.filter(Fav_User=name,Fav_Gname=game_name).exists()
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"game_details.html",{"data":data,"requirement":requirements,"image":image,"similar":similar,
                                               "is_favorite":is_favorite,"game_id":game_id,"fav_count":fav_count})




# def game_trailer(request,game_id):
#     game_name = Game_Db.objects.get(id = game_id).Game_Name
#     comments = Comment_Db.objects.filter(Game_Name = game_name)
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     ved = Game_Db.objects.get(id = game_id)
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"game_trailer.html",{"ved":ved,"image":image,"comments":comments,"fav_count":fav_count})
# def game_trailer(request,game_id):
#     game_name = Game_Db.objects.get(id = game_id).Game_Name
#     comments = Comment_Db.objects.filter(Game_Name = game_name)
#     for c in comments:
#         try:
#             c.current_image = Login_Db.objects.get(Name=c.User_Name).Profile_Image
#         except Login_Db.DoesNotExist:
#             c.current_image = None
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     ved = Game_Db.objects.get(id = game_id)
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"game_trailer.html",{"ved":ved,"image":image,"comments":comments,"fav_count":fav_count})
def game_trailer(request,game_id):
    game_name = Game_Db.objects.get(id=game_id).Game_Name
    comments = Comment_Db.objects.filter(Game_Name=game_name)
    for c in comments:
        try:
            u = Login_Db.objects.get(Name=c.User_Name)
            c.current_image = u.Profile_Image_URL if u.Profile_Image_URL else u.Profile_Image
        except Login_Db.DoesNotExist:
            c.current_image = None
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    ved = Game_Db.objects.get(id=game_id)
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"game_trailer.html",{"ved":ved,"image":image,"comments":comments,"fav_count":fav_count})



def search(request):
    query = request.GET.get('q', '')

    if query:
        games = Game_Db.objects.filter(Game_Name__icontains=query)
        results = []
        for game in games:
            results.append({
                'game_name': game.Game_Name,
                'cover_image': game.Cover_Image.url,
                'overall_rating': game.Overall_Rating,
                'age_rating': game.Age_Rating,
                'url': f"/game_details/{game.id}/",
            })
        return JsonResponse({'results': results})
    return JsonResponse({'results': []})



# def search_games(request):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     return render(request,"search_games.html",{"image":image})
def search_games(request):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    return render(request,"search_games.html",{"image":image})



# def game_filter(request,game_name):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     data = Game_Db.objects.filter(Game_Category = game_name)
#     title  = game_name
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"game_filter.html",{"data":data,"title":title,"image":image,"fav_count":fav_count})
def game_filter(request,game_name):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    data = Game_Db.objects.filter(Game_Category=game_name)
    title = game_name
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"game_filter.html",{"data":data,"title":title,"image":image,"fav_count":fav_count})



# def contact(request):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"contact.html",{"image":image,"fav_count":fav_count})
def contact(request):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"contact.html",{"image":image,"fav_count":fav_count})


def login_page(req):
    return render(req,"login_page.html")
def user_login(req):
    return render(req,"user_login.html")
def save_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        city = request.POST.get("city")
        message = request.POST.get("message")

        errors = {}

        if not name:
            errors["name"] = "This field is required."
        elif len(name)<3:
            errors["name"] = "Name must be at least 3 characters long."

        if not mobile:
            errors["mobile"] = "This field is required."
        elif not mobile.isdigit() or len(mobile) != 10:
            errors["mobile"] = "Mobile number must be a 10-digit number."

        if not email:
            errors["email"] = "This field is required."
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors["email"] = "Invalid email address."

        if not city:
            errors["city"] = "This field is required."

        if not message:
            errors["message"] = "This field is required."

        if errors:
            return render(request,"contact.html",{"error":errors,"data":request.POST})

        obj = Contact_Db(Name = name,Mobile = mobile,Email = email,City = city,Message = message)
        obj.save()
        messages.success(request,"Thank you for the review!")
        return redirect(contact)
def save_user_details(request):
    if request.method == "POST":

        # profile_status = request.POST.get('profile_picture_status')
        # if profile_status == 'changed' and 'profile_picture' in request.FILES:
        #     profile_picture = request.FILES['profile_picture']
        # else:
        #     profile_picture = ''

        if 'profile_picture' in request.FILES:
            if os.environ.get('CLOUDINARY_CLOUD_NAME'):
                upload_result = cloudinary.uploader.upload(request.FILES['profile_picture'])
                profile_picture_url = upload_result['secure_url']
                profile_picture = ''
            else:
                profile_picture = request.FILES['profile_picture']
                profile_picture_url = ''
        else:
            profile_picture = ''
            profile_picture_url = ''

        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")

        errors = {}

        if not name:
            errors["name"] = "This field is required."
        elif len(name) < 3:
            errors["name"] = "Name must be at least 3 characters long."
        elif Login_Db.objects.filter(Name=name).exists():
            errors["name"] = "This name is already in use."

        if not email:
            errors["email"] = "This field is required."
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors["email"] = "Invalid email address."
            if Login_Db.objects.filter(Email=email).exists():
                errors["email"] = "This email is already registered."

        if not mobile:
            errors["mobile"] = "This field is required."
        elif not mobile.isdigit() or len(mobile) != 10:
            errors["mobile"] = "Mobile number must be a 10-digit number."
        elif Login_Db.objects.filter(Mobile=mobile).exists():
            errors["mobile"] = "This mobile number is already registered."


        if not password:
            errors["password"] = "This field is required."
        elif len(password) < 6:
            errors["password"] = "Password must be at least 6 characters long."

        if not re_password:
            errors["re_password"] = "This field is required."
        elif password != re_password:
            errors["re_password"] = "Passwords do not match."

        if not request.POST.get("agree-term"):
            errors["agree_term"] = "You must agree to the terms of service."

        if errors:
            return render(request, "login_page.html", {"errors": errors, "data": request.POST})

        # obj = Login_Db(Name = name,Email = email,Mobile = mobile,Password = password,Re_Password = re_password,
        #                Profile_Image = profile_picture)
        obj = Login_Db(Name=name, Email=email, Mobile=mobile, Password=password,
               Re_Password=re_password, Profile_Image=profile_picture,
               Profile_Image_URL=profile_picture_url)

        obj.save()
        messages.success(request,"Account Created!")
        return redirect(user_login)
def login_user(request):
    if request.method == "POST":
        us = request.POST.get("name")
        pwd = request.POST.get("password")
        if Login_Db.objects.filter(Name = us,Password = pwd).exists():
            request.session["Name"] = us
            request.session["Password"] = pwd
            name = request.session.get("Name")
            messages.success(request,"Welcome "+name+"...!")
            return redirect(home_page)
        else:
            messages.error(request,"Password Incorrect!")
            return redirect(user_login)

    else:
        messages.warning(request,"Account not exists!")
        return redirect(user_login)

def user_logout(request):
    del request.session["Name"]
    del request.session["Password"]
    messages.warning(request,"You are logged out!")
    return redirect(user_login)


# def upcoming_details(request,up_id):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     data = Upcoming_Db.objects.get(id = up_id)
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"upcoming_details.html",{"data":data,"image":image,"fav_count":fav_count})
def upcoming_details(request,up_id):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    data = Upcoming_Db.objects.get(id=up_id)
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"upcoming_details.html",{"data":data,"image":image,"fav_count":fav_count})




# def upcoming_trailer(request,up_id):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     ved = Upcoming_Db.objects.get(id = up_id)
#     fav_game = Upcoming_Db.objects.get(id=up_id).Up_Game_Name
#     comments = Comment_Db.objects.filter(Game_Name = fav_game)
#     for c in comments:
#         try:
#             c.current_image = Login_Db.objects.get(Name=c.User_Name).Profile_Image
#         except Login_Db.DoesNotExist:
#             c.current_image = None
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"upcoming_trailer.html",{"ved":ved,"image":image,"comments":comments,"fav_count":fav_count})
def upcoming_trailer(request,up_id):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    ved = Upcoming_Db.objects.get(id=up_id)
    fav_game = Upcoming_Db.objects.get(id=up_id).Up_Game_Name
    comments = Comment_Db.objects.filter(Game_Name=fav_game)
    for c in comments:
        try:
            u = Login_Db.objects.get(Name=c.User_Name)
            c.current_image = u.Profile_Image_URL if u.Profile_Image_URL else u.Profile_Image
        except Login_Db.DoesNotExist:
            c.current_image = None
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"upcoming_trailer.html",{"ved":ved,"image":image,"comments":comments,"fav_count":fav_count})



def save_comment(request):
    if request.method == 'POST':
        game_name = request.POST.get("gname")
        user_name = request.POST.get("uname")
        user_image = request.POST.get("u_image")
        comment  = request.POST.get("comment")


        if not user_name or not comment:
            return JsonResponse({'error': 'Invalid data'}, status=400)


        try:
            obj = Comment_Db(Game_Name=game_name, User_Image=user_image,User_Name = user_name,Comment = comment)
            obj.save()


            response_data = {
                'game_name': obj.Game_Name,
                'user_name': obj.User_Name,
                'comment':obj.Comment,
                'user_image': obj.User_Image if obj.User_Image else "default_image_url_or_path",
                'created_at': timesince(obj.Created_Time),  # Assuming created_at field exists
            }

            return JsonResponse(response_data, status=201)

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)


    return JsonResponse({'error': 'Invalid request method'}, status=400)

def toggle_favorite(request, game_id):
    if request.method == "POST":
        uname = request.session.get("Name")
        gname = Game_Db.objects.get(id = game_id).Game_Name
        fav_count = Favorite_Db.objects.filter(Fav_User = uname).count()


        favorite = Favorite_Db.objects.filter(Fav_User=uname, Fav_Gname=gname).first()

        if favorite:
            favorite.delete()
            fav_count -= 1
            print(fav_count)
            return JsonResponse({'status': 'removed',"count":fav_count})


        game_name = request.POST.get("game_name")
        cover_image = request.POST.get("cover_image")
        age_rating = request.POST.get("age_rating")
        overall_rating = request.POST.get("overall_rating")
        user = request.POST.get("user")
        gameId = request.POST.get("game_id")


        obj = Favorite_Db(
            Fav_Cover=cover_image,
            Fav_Gname=game_name,
            Fav_Age=age_rating,
            Fav_Overall=overall_rating,
            Fav_User=user,
            Fav_ID = gameId
        )
        obj.save()
        fav_count += 1
        print(fav_count)
        return JsonResponse({'status': 'added',"count":fav_count})

    return JsonResponse({'status': 'error'}, status=400)

# def favorite(request):
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     user = request.session.get("Name")
#     favorite = Favorite_Db.objects.filter(Fav_User = user)
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"favorite.html",{"favorite":favorite,"image":image,"fav_count":fav_count})
def favorite(request):
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    favorite = Favorite_Db.objects.filter(Fav_User=name)
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"favorite.html",{"favorite":favorite,"image":image,"fav_count":fav_count})
def remove_favorite(request, favorite_id):
    if request.method == "POST":
        favorites = Favorite_Db.objects.filter(Fav_User = request.session.get("Name")).count()
        favorite = Favorite_Db.objects.get(id=favorite_id, Fav_User=request.session.get("Name"))
        favorite.delete()  # Remove the favorite game
        favorites = favorites-1
        return JsonResponse({'status': 'removed','count':favorites})

def fav_save_comment(request):
    if request.method == 'POST':
        game_name = request.POST.get("upname")
        user_name = request.POST.get("upuser")
        user_image = request.POST.get("upimage")
        comment = request.POST.get("upcomment")

        # Check that required data exists
        if not user_name or not comment:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        # Save the comment to the database
        try:
            obj = Comment_Db(Game_Name=game_name, User_Image=user_image,User_Name = user_name,Comment = comment)
            obj.save()

            # Prepare the response data
            response_data = {
                'game_name': obj.Game_Name,
                'user_name': obj.User_Name,
                'comment':obj.Comment,
                'user_image': obj.User_Image if obj.User_Image else "default_image_url_or_path",
                'created_at': timesince(obj.Created_Time),  # Assuming created_at field exists
            }

            return JsonResponse(response_data, status=201)  # Return JSON response

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)

    # Return an error if the request method is not POST
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# def blog_post(request):
#     data = Fan_Favorite_Db.objects.all()
#     for i in data:
#         created = i.Fan_Created
#     formatted_date = created.strftime("%B %d, %Y")
#     name = request.session.get("Name")
#     image = Login_Db.objects.get(Name = name).Profile_Image
#     fav_count = Favorite_Db.objects.filter(Fav_User = name).count()
#     return render(request,"blog_post.html",{"data":data,"image":image,"fav_count":fav_count,"formatted_date":formatted_date})
def blog_post(request):
    data = Fan_Favorite_Db.objects.all()
    for i in data:
        created = i.Fan_Created
    formatted_date = created.strftime("%B %d, %Y")
    name = request.session.get("Name")
    user = Login_Db.objects.get(Name=name)
    image = user.Profile_Image_URL if user.Profile_Image_URL else user.Profile_Image
    fav_count = Favorite_Db.objects.filter(Fav_User=name).count()
    return render(request,"blog_post.html",{"data":data,"image":image,"fav_count":fav_count,"formatted_date":formatted_date})
def save_blog(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        fav_game = request.POST.get("fav_game")
        feedback = request.POST.get("message")

        obj = Blog_Share(Blog_Name = name,Blog_Email = email,Blog_Fav = fav_game,Blog_Feedback = feedback)
        obj.save()
        return redirect(blog_post)


# def update_profile_picture(request):
#     if request.method == "POST" and request.FILES.get("new_profile_picture"):
#         name = request.session.get("Name")
#         user = Login_Db.objects.get(Name=name)
#         user.Profile_Image = request.FILES["new_profile_picture"]
#         user.save()
#     return redirect(request.META.get("HTTP_REFERER", "home_page"))
def update_profile_picture(request):
    if request.method == "POST" and request.FILES.get("new_profile_picture"):
        name = request.session.get("Name")
        user = Login_Db.objects.get(Name=name)
        if os.environ.get('CLOUDINARY_CLOUD_NAME'):
            upload_result = cloudinary.uploader.upload(request.FILES["new_profile_picture"])
            user.Profile_Image_URL = upload_result['secure_url']
            user.Profile_Image = ''
        else:
            user.Profile_Image = request.FILES["new_profile_picture"]
            user.Profile_Image_URL = ''
        user.save()
        messages.success(request, "Profile picture updated!")
    return redirect(request.META.get("HTTP_REFERER", "home_page"))







# Create your views here.
