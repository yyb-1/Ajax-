from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):

    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        if uname == 'root':

            return HttpResponse("登陆成功")
        error = '用户名' + str(uname) + '不对'
        return render(request,'login.html', {'error': error, 'uname':uname})

    return render(request,'login.html')

def login_ajax(request):

    print (request.POST)
    # <QueryDict: {'xx': ['test'], 'pp': ['111']}>
    uname = request.POST.get('xx')
    if uname == 'root':

        return HttpResponse("ok")

    return HttpResponse('error')


import json
def data(request):
    data_list = {'name': 'Tom', 'hobby':['football','basketball','music']}
    hobby_list = ['football','basketball','music']

    # data_list_str = json.dumps(data_list, ensure_ascii=False)   #json.dumps函数是将数据序列化，用于HttpResponse数据传送
    # #直接使用Httpresponse回复字段类型数据，就会将字典里的元素的键名拼接成一个字符串，所以不是我们想要的结果。
    # #因此我们需要先将字典转换成json字符串，再通过Httpresponse来进行响应。
    #
    # # return HttpResponse(data_list)   # namehobby
    #
    # return HttpResponse(data_list_str)  # 用HttpResponse响应时，需要在views中庸dumps打包成Json，然后在html中要用JSON.parse解析。

    # return JsonResponse(data_list)
    # #用JsonResponse响应时，不需要在views中dumps，也不需要html中庸parse。 html会自动将JsonResponse响应内容转换为字典。
    # #JsonResponse做了2件事： 1）序列化数据  2）加上ret[‘Content-Type] = application/json’响应头键值对

    #当使用JsonResponse响应非字典类型数据时，需要将Safe参数值改为False
    return JsonResponse(hobby_list, safe=False)

def sub(request):
    if request.method == 'GET':

        return render(request,'sub.html')

    else:
        # print(request.POST)   # <QueryDict: {}>
        # print(request.body)   # b'{"aa":"1","bb":"2"}'

        #django没有内置对application/json的消息格式的解析器，所以如果请求数据是json类型，我们需要自行解析
        import json
        data = request.body.decode()
        data = json.loads(data)
        # print(data, type(data))   # {'aa': '1', 'bb': '2'}

        total = 0
        for v in data.values():
            total = total + int(v)
        print(total)

        return HttpResponse(total)


#演示ajax通过get方法也能提交数据
# def sum(request):
#     print(request.GET)
#     # <QueryDict: {'aa': ['1'], 'bb': ['2']}>
#
#     return HttpResponse('sub-ok')


'''
socket 接收到我们请求的数据， 会分析一下Content-Type: application/x-www-form-urlencoded 这个请求头,并自动做如下解包动作：

    if Content-Type == 'application/x-www-form-urlencoded':
        data = 'a=1&b=2'
        l1 = data.split('&')   [a=1, b=2]
        for i in l1:
            k,v = i.split('=')
        if 请求方法 == ‘GET'：
            request.GET(k) = v
        
    elif Content-Type == 'multipart/form-data':
        request.FILES

    #django没有内置对application/json的消息格式的解析器，所以如果请求数据是json类型，我们需要自行解析

'''