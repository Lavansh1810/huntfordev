from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateModel(request, model, results):
    
    page = request.GET.get('page')
    
    paginator = Paginator(model, results)

    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages
        model = paginator.page(page)


    leftIndex = (int(page) -2)

    if leftIndex<1:
        leftIndex=1
    
    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)

    return custom_range, model
