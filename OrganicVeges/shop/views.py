from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.template import Context
from django.contrib.auth.models import User
from twilio.rest import Client


# Create your views here.
def demo(request):
    shop_now = Addproducts.objects.all()
    return render(request, 'demo.html', {'shop_now' : shop_now})

def Home(request):
    shop_now = Addproducts.objects.all()
    return render(request, 'Home.html',{'shop_now' : shop_now})

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('firstname', '') + " " + request.POST.get('lastname', '')
        username = request.POST.get('Username')
        amount = request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order = Orders(items_json= items_json, name=name, username=username, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        # subject = 'welcome to OrganicVeges'
        # html_message = render_to_string('mail.html', {'orders': order})
        # plain_message = strip_tags(html_message)
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [order.email, ]
        # send_mail(subject, plain_message, email_from, recipient_list)
        message = render_to_string('mail.html', {'orders': order})
        msg = EmailMessage(
            'OrganicVegse',
            message,
            settings.EMAIL_HOST_USER,
            [order.email,],
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        print("Mail successfully sent")

        account_sid = 'AC4eb065101d67c8b96b29879b03b70a16'
        auth_token = '44357165973b9a8df29f7bf04bebdc72'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body='You have got an order having order id '+ str(order.order_id) + ' from '+username+
                ' email id: '+ email +
                ' Address :' + address +
                ' Phone number: '+ phone ,

            from_='+14847200081',
            to='+91' + phone,

        )

        print(message.sid)

        thank=True
        id=order.order_id
        return render(request, 'index.html', {'thank':thank, 'id':id})
    return render(request, 'index.html')

def viewDetail(request,myid):
    commentsss = Commentsss.objects.all()
    #pr_id = AddComments.objects.filter('pr_id')
    #pr_str = str(pr_id)
    shops = Addproducts.objects.filter(id=myid)
    shop_now = Addproducts.objects.all()
    user=request.user

    #context ={'shops': shops, 'comments': comments ,'pr_id' : pr_id}

    print(shops)
    return render(request, 'ViewDetail.html', {'shops':shops ,'shop_now' : shop_now,'commentsss' : commentsss,'user':user})

def AboutUs(requets):
    return render(requets,'About Us.html')

def ContactUs(request):
    if request.method=="POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        contact = Contact(first_name=first_name, last_name=last_name,email=email,feedback=feedback)
        contact.save();
        return redirect('/')
    return render(request,'Contact Us.html')

'''def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        pr_id = request.POST.get('pr_id')
        product = Addproducts.objects.get(id=pr_id)
        comment = AddComments(comment=comment, user=user, product=product, pr_id=pr_id)
        comment.save();
        messages.success(request, "Your comment has been posted successfully")
    return redirect('viewDetail/<int:myid>')'''

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        pr_id = request.POST.get('pr_id')
        product = Addproducts.objects.get(id=pr_id)
        reply_id = request.POST.get('reply_id')
        commentsss = Commentsss.objects.all()
        shops = Addproducts.objects.filter(id=pr_id)
        shop_now = Addproducts.objects.all()
        comment = Commentsss(comment=comment, user=user, product=product, pr_id=pr_id,reply_id=reply_id)
        comment.save();
        messages.success(request, "Your comment has been posted successfully")
    return render(request,'ViewDetail.html', {'shops':shops ,'shop_now' : shop_now,'commentsss' : commentsss})


def like_post(request):
    user = request.user

    if request.method=='POST':
        post_id = request.POST.get('post_id')
        post_obj = Addproducts.objects.get(id=post_id)

        if user in post_obj.liked.all():
            Addproducts.obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, product=post_id)

        if not created:
            if like.value=='Like':
                like.value == 'Unlike'
            else:
                like.value = 'Like'
        like.save();

    return render(request,'shop:view-Detail',{})



def replyComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        pr_id = request.POST.get('pr_id')
        product = Addproducts.objects.get(id=pr_id)
        reply_id = request.POST.get('reply_id')
        replys = Reply.objects.all()
        shops = Addproducts.objects.filter(id=pr_id)
        shop_now = Addproducts.objects.all()
        commentsss = Commentsss.objects.all()
        reply = Reply(comment=comment, user=user, product=product, pr_id=pr_id, reply_id=reply_id)
        reply.save();
        messages.success(request, "Your comment has been posted successfully")
        return render(request, 'ViewDetail.html', {'shops': shops, 'shop_now': shop_now, 'replys': replys,'commentsss':commentsss})



#
#
# def BlogPostLike(request, pk):
#     post = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)
#
#     return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))