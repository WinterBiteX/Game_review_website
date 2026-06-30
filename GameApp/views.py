from django.shortcuts import render,redirect
from GameApp.models import Category_Db,Game_Db,Requirement_Db,Upcoming_Db,Fan_Favorite_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from WebApp.models import Contact_Db,Login_Db,Comment_Db,Blog_Share
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login_page')
# def admin_page(req):
#     return render(req,"index.html")
def admin_page(req):
    if not req.user.is_authenticated:
        messages.warning(req, "Please login to access the admin dashboard!")
        return redirect(login_page)
    return render(req,"index.html")
def add_category(req):
    return render(req,"add_category.html")
def save_category(request):
    if request.method == "POST":
        a = request.POST.get("cname")
        b = request.POST.get("description")
        c = request.FILES['c_img']

        obj = Category_Db(Category_Name = a,Category_Description = b,Category_Image = c)
        obj.save()
        messages.success(request,"Game Category added...!")
        return redirect(add_category)
def display_category(req):
    data = Category_Db.objects.all()
    return render(req,"display_category.html",{"data":data})
def edit_category(req,cat_id):
    data = Category_Db.objects.get(id = cat_id)
    return render(req,"edit_category.html",{"data":data})
def update_category(request,cat_id):
    if request.method == "POST":
        a = request.POST.get("cname")
        b = request.POST.get("description")

        try:
            c = request.FILES['c_img']
            fs = FileSystemStorage()
            file = fs.save(c.name,c)
        except MultiValueDictKeyError:
            file = Category_Db.objects.get(id = cat_id).Category_Image
        Category_Db.objects.filter(id=cat_id).update(Category_Name = a,Category_Description = b,Category_Image = file)
        messages.success(request,"Game Category Updated...!")
        return redirect(display_category)
def delete_category(request,cat_id):
    data = Category_Db.objects.filter(id=cat_id)
    data.delete()
    messages.warning(request,"Game Category deleted...!")
    return redirect(display_category)

def add_games(req):
    data = Category_Db.objects.all()
    return render(req,"add_games.html",{"data":data})
def save_games(request):
    if request.method == 'POST':
        g_type = request.POST.get("category")
        cover = request.FILES['c_img']
        title = request.POST.get("title")
        tag = request.POST.get("name")
        short = request.POST.get("short")
        summary = request.POST.get("summary")
        genre = request.POST.get("genre")
        style = request.POST.get("style")
        plat = request.POST.get("platform")
        release = request.POST.get("r_date")
        mode = request.POST.get("mode")
        devops = request.POST.get("devops")
        publish = request.POST.get("publisher")
        age = request.POST.get("age_rating")
        average = request.POST.get("play")
        overall = request.POST.get("overall")
        g_link = request.POST.get("g_link")
        trailer = request.FILES.get('trailer')
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        img3 = request.FILES['img3']

        obj = Game_Db(Game_Category = g_type,Cover_Image = cover,Tag_Line = tag,Game_Name = title,
                      Short_Description = short,Summary = summary,Genre = genre,Game_Style = style,
                      Platform = plat,Release_Date = release,Game_Mode = mode,Developer = devops,Publisher = publish,
                      Age_Rating = age,Play_Time = average,Overall_Rating = overall,Download_Link = g_link,
                      Trailer = trailer,Image1 = img1,Image2 = img2,Image3 = img3)
        messages.success(request,"Game added...!")
        obj.save()
        return redirect(add_games)
def display_games(req):
    data = Game_Db.objects.all()
    return render(req,"display_games.html",{"data":data})
def edit_games(req,game_id):
    cat = Category_Db.objects.all()
    data = Game_Db.objects.get(id = game_id)
    return render(req,"edit_games.html",{"data":data,"cat":cat})
def update_games(request,game_id):
    if request.method == 'POST':
        g_type = request.POST.get("category")
        title = request.POST.get("title")
        tag = request.POST.get("name")
        short = request.POST.get("short")
        summary = request.POST.get("summary")
        genre = request.POST.get("genre")
        style = request.POST.get("style")
        plat = request.POST.get("platform")
        release = request.POST.get("r_date")
        mode = request.POST.get("mode")
        devops = request.POST.get("devops")
        publish = request.POST.get("publisher")
        age = request.POST.get("age_rating")
        average = request.POST.get("play")
        overall = request.POST.get("overall")
        g_link = request.POST.get("g_link")

        try:
            cover = request.FILES['c_img']
            fs1 = FileSystemStorage()
            file = fs1.save(cover.name,cover)
        except MultiValueDictKeyError:
            file = Game_Db.objects.get(id = game_id).Cover_Image

        try:
            img1 = request.FILES['img1']
            fs2 = FileSystemStorage()
            file1 = fs2.save(img1.name,img1)
        except MultiValueDictKeyError:
            file1 = Game_Db.objects.get(id = game_id).Image1

        try:
            img2 = request.FILES['img2']
            fs3 = FileSystemStorage()
            file2 = fs3.save(img2.name,img2)
        except MultiValueDictKeyError:
            file2 = Game_Db.objects.get(id = game_id).Image2

        try:
            img3 = request.FILES['img3']
            fs4 = FileSystemStorage()
            file3 = fs4.save(img3.name,img3)
        except MultiValueDictKeyError:
            file3 = Game_Db.objects.get(id = game_id).Image3

        try:
            trailer = request.FILES['trailer']
            fs5 = FileSystemStorage()
            file4 = fs5.save(trailer.name,trailer)
        except MultiValueDictKeyError:
            file4 = Game_Db.objects.get(id = game_id).Trailer

        Game_Db.objects.filter(id = game_id).update(Game_Category = g_type,Cover_Image = file,Tag_Line = tag,Game_Name = title,
                      Short_Description = short,Summary = summary,Genre = genre,Game_Style = style,
                      Platform = plat,Release_Date = release,Game_Mode = mode,Developer = devops,Publisher = publish,
                      Age_Rating = age,Play_Time = average,Overall_Rating = overall,Download_Link = g_link,
                      Trailer = file4,Image1 = file1,Image2 = file2,Image3 = file3)
        messages.success(request,"Game Updated...!")
        return redirect(display_games)
def delete_games(request,game_id):
    data = Game_Db.objects.filter(id = game_id)
    data.delete()
    messages.warning(request,"Game deleted...!")
    return redirect(display_games)

def add_requirement(req):
    game = Game_Db.objects.all()
    return render(req,"add_requirements.html",{"game":game})
def save_requirements(request):
    if request.method == "POST":
        gname = request.POST.get("gname")
        min_o = request.POST.get("minos")
        max_o = request.POST.get("maxos")
        min_r = request.POST.get("minram")
        max_r = request.POST.get("maxram")
        min_p = request.POST.get("minpro")
        max_p = request.POST.get("maxpro")
        min_g = request.POST.get("mingra")
        max_g = request.POST.get("maxgra")
        min_s = request.POST.get("minsto")
        max_s = request.POST.get("maxsto")

        obj = Requirement_Db(Requirement_Game = gname,Minimum_OperatingSystem = min_o,Maximum_OperatingSystem = max_o,
                             Minimum_RAM = min_r,Maximum_RAM = max_r,Minimum_Processor = min_p,Maximum_Processor = max_p,
                             Minimum_Graphics = min_g,Maximum_Graphics = max_g,Minimum_Storage = min_s,Maximum_Storage = max_s)
        obj.save()
        messages.success(request,"Requirements added...!")
        return redirect(add_requirement)
def display_requirement(req):
    data = Requirement_Db.objects.all()
    return render(req,"display_requirement.html",{"data":data})
def edit_requirement(req,req_id):
    game = Game_Db.objects.all()
    data = Requirement_Db.objects.get(id = req_id)
    return render(req,"edit_requirement.html",{"game":game,"data":data})
def update_requirement(request,req_id):
    if request.method == "POST":
        gname = request.POST.get("gname")
        min_o = request.POST.get("minos")
        max_o = request.POST.get("maxos")
        min_r = request.POST.get("minram")
        max_r = request.POST.get("maxram")
        min_p = request.POST.get("minpro")
        max_p = request.POST.get("maxpro")
        min_g = request.POST.get("mingra")
        max_g = request.POST.get("maxgra")
        min_s = request.POST.get("minsto")
        max_s = request.POST.get("maxsto")

        Requirement_Db.objects.filter(id = req_id).update(Requirement_Game = gname,Minimum_OperatingSystem = min_o,Maximum_OperatingSystem = max_o,
                             Minimum_RAM = min_r,Maximum_RAM = max_r,Minimum_Processor = min_p,Maximum_Processor = max_p,
                             Minimum_Graphics = min_g,Maximum_Graphics = max_g,Minimum_Storage = min_s,Maximum_Storage = max_s)
        messages.success(request,"Requirements Updated...!")
        return redirect(display_requirement)
def delete_requirement(request,req_id):
    data = Requirement_Db.objects.filter(id = req_id)
    data.delete()
    messages.warning(request,"Requirements deleted...!")
    return redirect(display_requirement)

def display_contact(req):
    data = Contact_Db.objects.all()
    return render(req,"display_contact.html",{"data":data})
def delete_contact(request,con_id):
    data = Contact_Db.objects.filter(id = con_id)
    data.delete()
    messages.success(request,"Contacts deleted...!")
    return redirect(display_contact)
def login_page(request):
    print("Is authenticated:", request.user.is_authenticated)
    return render(request,"admin_login.html")
def admin_login(request):
    if request.method == "POST":
        us = request.POST.get("email-username")
        ps = request.POST.get("password")

        if User.objects.filter(username__contains = us).exists():
            user = authenticate(username = us,password = ps)

            if user is not None:
                login(request,user)
                request.session['username'] = us
                request.session['password'] = ps
                messages.success(request,"Welcome....!")
                return redirect(admin_page)
            else:
                messages.error(request,"Incorrect Password...!")
                return redirect(login_page)
        else:
            messages.warning(request,"Username does not exists...!")
            return redirect(login_page)

def logout_user(request):
    logout(request)
    messages.warning(request,"You are logging out...!")
    return redirect(login_page)
def account_manager(request):
    obj = Login_Db.objects.all()
    return render(request,"account_manager.html",{"obj":obj})
def delete_account(request,us_id):
    data = Login_Db.objects.filter(id = us_id)
    data.delete()
    messages.warning(request,"Users Account removed!")
    return redirect(account_manager)
def add_upcoming(request):
    return render(request,"add_upcoming.html")
def save_upcoming(request):
    if request.method == 'POST':
        cover = request.FILES['c_img']
        inside = request.FILES['i_img']
        title = request.POST.get("title")
        tag = request.POST.get("name")
        short = request.POST.get("short")
        summary = request.POST.get("summary")
        genre = request.POST.get("genre")
        style = request.POST.get("style")
        plat = request.POST.get("platform")
        release = request.POST.get("r_date")
        mode = request.POST.get("mode")
        devops = request.POST.get("devops")
        publish = request.POST.get("publisher")
        age = request.POST.get("age_rating")
        average = request.POST.get("play")
        overall = request.POST.get("overall")
        trailer = request.FILES.get('trailer')

        obj = Upcoming_Db(Up_Cover_Image = cover,Up_Inside_Image = inside,Up_Tag_Line = tag,Up_Game_Name = title,
                      Up_Short_Description = short,Up_Summary = summary,Up_Genre = genre,Up_Game_Style = style,
                      Up_Platform = plat,Up_Release_Date = release,Up_Game_Mode = mode,Up_Developer = devops,Up_Publisher = publish,
                      Up_Age_Rating = age,Up_Play_Time = average,Up_Overall_Rating = overall,
                      Up_Trailer = trailer)
        messages.success(request,"Game added...!")
        obj.save()
        return redirect(add_upcoming)
def display_upcoming(request):
    data = Upcoming_Db.objects.all()
    return render(request,"display_upcoming.html",{"data":data})
def edit_upcoming(request,up_id):
    data = Upcoming_Db.objects.get(id = up_id)
    return render(request,"edit_upcoming.html",{"data":data})
def update_upcoming(request,up_id):
    if request.method == 'POST':
        title = request.POST.get("title")
        tag = request.POST.get("name")
        short = request.POST.get("short")
        summary = request.POST.get("summary")
        genre = request.POST.get("genre")
        style = request.POST.get("style")
        plat = request.POST.get("platform")
        release = request.POST.get("r_date")
        mode = request.POST.get("mode")
        devops = request.POST.get("devops")
        publish = request.POST.get("publisher")
        age = request.POST.get("age_rating")
        average = request.POST.get("play")
        overall = request.POST.get("overall")

        try:
            cover = request.FILES['c_img']
            fs1 = FileSystemStorage()
            file = fs1.save(cover.name,cover)
        except MultiValueDictKeyError:
            file = Upcoming_Db.objects.get(id = up_id).Up_Cover_Image

        try:
            cover1 = request.FILES['i_img']
            fs2 = FileSystemStorage()
            file1 = fs2.save(cover1.name,cover1)
        except MultiValueDictKeyError:
            file1 = Upcoming_Db.objects.get(id = up_id).Up_Inside_Image


        try:
            trailer = request.FILES['trailer']
            fs5 = FileSystemStorage()
            file4 = fs5.save(trailer.name,trailer)
        except MultiValueDictKeyError:
            file4 = Upcoming_Db.objects.get(id = up_id).Up_Trailer

        Upcoming_Db.objects.filter(id = up_id).update(Up_Cover_Image = file,Up_Inside_Image = file1,Up_Tag_Line = tag,Up_Game_Name = title,
                      Up_Short_Description = short,Up_Summary = summary,Up_Genre = genre,Up_Game_Style = style,
                      Up_Platform = plat,Up_Release_Date = release,Up_Game_Mode = mode,Up_Developer = devops,Up_Publisher = publish,
                      Up_Age_Rating = age,Up_Play_Time = average,Up_Overall_Rating = overall,
                      Up_Trailer = file4)
        messages.success(request,"Game Updated...!")
        return redirect(display_upcoming)
def delete_upcoming(request,up_id):
    data = Upcoming_Db.objects.filter(id = up_id)
    data.delete()
    messages.warning(request,"Game deleted...!")
    return redirect(display_upcoming)
# def display_comments(request):
#     data = Comment_Db.objects.all()
#     return render(request,"display_comments.html",{"data":data})
def display_comments(request):
    data = Comment_Db.objects.all()
    for comment in data:
        try:
            comment.current_image = Login_Db.objects.get(Name=comment.User_Name).Profile_Image
        except Login_Db.DoesNotExist:
            comment.current_image = None
    return render(request, "display_comments.html", {"data": data})
def delete_comments(request,com_id):
    data = Comment_Db.objects.filter(id=com_id)
    data.delete()
    messages.warning(request,"Users Comment is terminated!")
    return redirect(display_comments)
def display_feedback(request):
    data = Blog_Share.objects.all()
    return render(request,"Display_Feedback.html",{"data":data})
def delete_feedback(request,feed_id):
    data = Blog_Share.objects.filter(id = feed_id)
    data.delete()
    messages.warning(request,"User Feedback removed!")
    return redirect(display_feedback)
def add_fan_favorite(request):
    return render(request,"add_fan_favorites.html")
def save_fan_favorite(request):
    if request.method == "POST":
        gname = request.POST.get("gname")
        desc = request.POST.get("description")
        b_img = request.FILES['c_img']
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        p3 = request.POST.get("p3")

        obj = Fan_Favorite_Db(Fan_Game = gname,Fan_Description = desc,Fan_Image = b_img,Reason1 = p1,Reason2 = p2,Reason3 = p3 )
        obj.save()
        messages.success(request,"Fan-Favorite added successfully!")
        return redirect(add_fan_favorite)





















# Create your views here.
