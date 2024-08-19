from django.shortcuts import render, redirect

from .models import User, Category, Comment, Company, Education, Experience, Awards, Skills, Services, Blog, OurProjects, SiteAdminisration, GetInTouch, Tag


def home(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')

    admin = SiteAdminisration.objects.get(id=1)
    user = User.objects.get(id=1)

    companies = Company.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    awards = Awards.objects.all()
    skills = Skills.objects.all()
    services = Services.objects.all()
    blogs = Blog.objects.all()
    our_projects = OurProjects.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        GetInTouch.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return redirect('home')
    
    context = {
        'user': user,
        'companies': companies.order_by('-id')[:5],
        'educations': educations.order_by('id')[:4],
        'experiences': experiences.order_by('-id')[:6],
        'awards': awards.order_by('id')[:5],
        'skills': skills.order_by('-id')[:6],
        'services': services.order_by('id')[:6],
        'blogs': blogs.order_by('-id')[:3],
        'our_projects': our_projects.order_by('-id')[:6],
        'admin': admin,
    }

    return render(request, 'index.html', context)

def home2(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')

    admin = SiteAdminisration.objects.get(id=1)
    user = User.objects.get(id=1)

    companies = Company.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    awards = Awards.objects.all()
    skills = Skills.objects.all()
    services = Services.objects.all()
    blogs = Blog.objects.all()
    our_projects = OurProjects.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        GetInTouch.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return redirect('home2')
    
    context = {
        'user': user,
        'companies': companies.order_by('-id')[:5],
        'educations': educations.order_by('id')[:4],
        'experiences': experiences.order_by('-id')[:6],
        'awards': awards.order_by('id')[:5],
        'skills': skills.order_by('-id')[:6],
        'services': services.order_by('id')[:6],
        'blogs': blogs.order_by('-id')[:3],
        'our_projects': our_projects.order_by('-id')[:6],
        'admin': admin,
    }

    return render(request, 'index-2.html', context)

def single(request, slug):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')

    tags = Tag.objects.all()
    categories = Category.objects.all()
    recent_blogs = Blog.objects.all()

    blog = Blog.objects.get(slug__iexact=slug)

    comments = Comment.objects.filter(blog_id=blog.id)

    if request.method == "POST":   
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        web_site = request.POST.get("website")

        Comment.objects.create(
            blog_id=blog.id,
            user_id=request.user.id,
            name=name,
            email=email,
            comment=comment,
            web_site=web_site,
        )

        return redirect('single', blog.slug)
    
    context = {
        'blog': blog,
        'tags': tags.order_by('name'),
        'categories': categories.order_by('name'),
        'recent_blogs': recent_blogs.order_by('-id')[:3],
        'comments': comments,
        }
    
    return render(request, 'single.html', context)
