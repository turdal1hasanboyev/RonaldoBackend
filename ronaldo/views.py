from django.shortcuts import render, redirect

from ronaldo.models import User, Category, Comment, Company, Education, Experience, Awards, Skills, Services, Blog, OurProjects, SiteAdminisration, GetInTouch, Tag


def home(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    
    user = User.objects.get(id=1)
    companies = Company.objects.all().order_by('-id')[:5]
    educations = Education.objects.all().order_by('id')[:4]
    experiences = Experience.objects.all().order_by('-id')[:6]
    awards = Awards.objects.all().order_by('id')[:5]
    skills = Skills.objects.all().order_by('-id')[:6]
    services = Services.objects.all().order_by('id')[:6]
    blogs = Blog.objects.all().order_by('-id')[:3]
    our_projects = OurProjects.objects.all().order_by('-id')[:6]
    admin = SiteAdminisration.objects.get(id=1)

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
        'companies': companies,
        'educations': educations,
        'experiences': experiences,
        'awards': awards,
        'skills': skills,
        'services': services,
        'blogs': blogs,
        'our_projects': our_projects,
        'admin': admin,
    }

    return render(request, 'index.html', context)

def home2(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')

    user = User.objects.get(id=1)
    companies = Company.objects.all().order_by('-id')[:5]
    educations = Education.objects.all().order_by('id')[:4]
    experiences = Experience.objects.all().order_by('-id')[:6]
    awards = Awards.objects.all().order_by('id')[:5]
    skills = Skills.objects.all().order_by('-id')[:6]
    services = Services.objects.all().order_by('id')[:6]
    blogs = Blog.objects.all().order_by('-id')[:3]
    our_projects = OurProjects.objects.all().order_by('-id')[:6]
    admin = SiteAdminisration.objects.get(id=1)

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
        'companies': companies,
        'educations': educations,
        'experiences': experiences,
        'awards': awards,
        'skills': skills,
        'services': services,
        'blogs': blogs,
        'our_projects': our_projects,
        'admin': admin,
    }

    return render(request, 'index-2.html', context)

def single(request, slug):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')

    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')
    recent_blogs = Blog.objects.all().order_by('-id')[:3]

    blog = Blog.objects.get(slug__iexact=slug)
    comments = Comment.objects.filter(blog_id=blog.id)

    if request.method == "POST":   
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        website = request.POST.get("website")

        Comment.objects.create(
            blog_id=blog.id,
            user=request.user,
            name=name,
            email=email,
            comment=comment,
            website=website,
        )

        return redirect('single', blog.slug)
    
    context = {
        'blog': blog,
        'tags': tags,
        'categories': categories,
        'recent_blogs': recent_blogs,
        'comments': comments,
        }
    
    return render(request, 'single.html', context)
