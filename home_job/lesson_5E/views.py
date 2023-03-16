from django.shortcuts import render


def go_jinja(request):
    return render(request, 'template_for_jinja.html',
                  context={
                      'data': {'name': 'Kolia', 'last_name': 'Bogdanovich'}},
                  using='jinja2')


def go_sort(request):
    cont_list = [1, 2, 5, 1, 87]
    return render(request, 'template_for_sort.html',
                  context={'data': cont_list, 'len': len(cont_list)},
                  using='jinja2', )
