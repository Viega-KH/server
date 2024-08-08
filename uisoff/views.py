from django.shortcuts import render, redirect, get_object_or_404
from employ.models import leadership
from blogs.models import news, category
from django.core.paginator import Paginator
from table.models import lesson
from school.models import infoschool
from slevel.models import infolevel
from django.http import JsonResponse
from statest.models import statestic
from contact.models import contact
from clubs.models import club
from library.models import library, librarycategore
from statest.models import statestic


def home(request):
    new = news.objects.all().order_by('-created_at')[:3]
    newfooter = news.objects.all().order_by('-created_at')[:2]
    school = infoschool.objects.all()
    slevel = infolevel.objects.all()
    statest = statestic.objects.get()
    context = {
        'new':new,
        'newfooter':newfooter,
        'school':school,
        'slevel':slevel,
        'statest':statest
    }
    return render(request, 'pages/home.html', context)




def homeselekt(request):
    if request.method == 'POST':
        school = request.POST.get('school') 
        slevel = request.POST.get('slevel') 
        
        if slevel:
            try:
                slevelget = infolevel.objects.get(id=slevel)
                response_data = {
                    'id': slevelget.id,
                    'title': slevelget.title,
                    'number_ch': slevelget.number_ch,
                    'number_ep': slevelget.number_ep,
                }
                return JsonResponse(response_data)
            except infolevel.DoesNotExist:
                return JsonResponse({'error': 'Level not found'}, status=404)

        if school:
            try:
                schoolget = infoschool.objects.get(id=school)
                response_data = {
                    'id': schoolget.id,
                    'title': schoolget.title,
                    'number_pt': schoolget.number_pt,
                    'number_s': schoolget.number_s,
                }
                return JsonResponse(response_data)
            except infoschool.DoesNotExist:
                return JsonResponse({'error': 'School not found'}, status=404)

        return JsonResponse({'error': 'No school or slevel ID provided'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)




def about(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    school = infoschool.objects.all()
    slevel = infolevel.objects.all()
    statest = statestic.objects.get()
    context = {
        'school':school,
        'slevel':slevel,
        'statest':statest,
        'newfooter':newfooter
    }
    statest = statestic.objects.get()
    return render(request, 'pages/about.html', context)




def leader(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    lists = leadership.objects.all()
    new = news.objects.all().order_by('-created_at')[:5]
    return render(request, 'pages/leader.html', { 'list':lists, 'new':new, 'newfooter':newfooter })




def new(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    news_list = news.objects.all().order_by('-created_at')
    paginator = Paginator(news_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/news.html', {'page_obj': page_obj, 'newfooter':newfooter})


def newad(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    news_list = news.objects.filter(category__name__icontains='E`lon').order_by('-created_at')
    paginator = Paginator(news_list, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/newad.html', {'page_obj': page_obj, 'newfooter':newfooter})




def newdet(request, id):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    news_list = news.objects.all().order_by('-created_at')[:5]
    new = news.objects.get(id=id)
    return render(request, 'include/news.html', {'news_list':news_list, 'new':new, 'newfooter':newfooter})




def contactsite(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    return render(request, 'pages/contact.html', { 'newfooter':newfooter })



def contactmessage(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if full_name and subject and phone and message:
            contact.objects.create(
                full_name=full_name,
                subject=subject,
                phone=phone,
                message=message
            )
            return redirect('contactsite')
        else:
            return JsonResponse({'error': 'All fields are required.'}, status=400)
    return JsonResponse()



def tablesite(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    new = news.objects.all().order_by('-created_at')[:5]
    schools = infoschool.objects.values_list('title', flat=True)
    schools_top = infoschool.objects.values_list('title', flat=True).order_by()[:4]
    selected_school = request.GET.get('table')
    print(selected_school)
    if selected_school:
        table = lesson.objects.filter(wschool__title__icontains=selected_school).order_by('-created_at')
    else:
        table = lesson.objects.all().order_by('-created_at').order_by()[:11]
    context = {
        'table': table,
        'schools': schools,
        'selected_school': selected_school,
        'schools_top': schools_top,
        'newfooter': newfooter,
        'new':new
    }
    return render(request, 'pages/table.html', context)


def clubs(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    new = news.objects.all().order_by('-created_at')[:5]
    schools = infoschool.objects.values_list('title', flat=True)
    last_school = schools.last() if schools else None
    selected_school = request.GET.get('table')
    print(selected_school)
    print(last_school)
    if selected_school:
        clublist = club.objects.filter(wschool__title__icontains=selected_school).order_by('-created_at')
    else:
        clublist = club.objects.filter(wschool__title__icontains=last_school).order_by('-created_at') if last_school else club.objects.none()
    context = {
        'schools': schools,
        'selected_school': selected_school or last_school,
        'clublist': clublist,
        'new': new,
        'newfooter': newfooter,
    }
    return render(request, 'pages/clubs.html', context)


def libraryviews(request):
    newfooter = news.objects.all().order_by('-created_at')[:2]
    new = news.objects.all().order_by('-created_at')[:5]
    librarys = library.objects.all().order_by('-created_at')
    librarycategores = librarycategore.objects.values_list('name', flat=True)
    selected_library = request.GET.get('selected_library')
    print(selected_library)
    if selected_library:
        librarys = library.objects.filter(categore__name__icontains=selected_library).order_by('-created_at')

    context = {
        'librarycategores':librarycategores,
        'librarys':librarys,
        'newfooter': newfooter,
        'selected_library ':selected_library,
        'new': new
    }
    return render(request, 'pages/library.html', context)
