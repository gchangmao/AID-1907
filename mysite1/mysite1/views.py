from django.http import HttpResponse

#127.0.0.1:8000
def page_view(requset):
    #请求返回
    html = '<h1>这是个页面</h1>'
    return HttpResponse(html)
def page1_view(request):
    html = '<h1>这是我的页面</h1>'
    return  HttpResponse(html)

def page2_view(request):
    html = '<h1>看这里！！！</h1>'
    return  HttpResponse(html)

def pagen_view(request,n):
    print(1111111111)
    print(type(n))
    html = '<h1>这是编号为%s的网页</h1>'%(n)
    return HttpResponse(html)


def add_view(requset):
    





