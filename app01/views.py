from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# 展示出版社
def publisher_list(request):
    # 从数据库获取所有出版社对象
    all_publisher = models.Publisher.objects.all().order_by('pid')
    return render(request, 'publisher_list.html', {'pubs': all_publisher})


# 增加出版社
def add_publisher(request):
    # 定义err_msg,new_name
    err_msg, new_name = '', ''
    # 区分请求方式
    if request.method == 'POST':
        # 获取提交的数据
        new_name = request.POST.get('new_name')
        print(new_name)
        # 判断提交的数据是否是空
        if not new_name:
            err_msg = '不能为空'
        # 数据库查询new_name是否已经存在
        obj_list = models.Publisher.objects.filter(name=new_name)
        if obj_list:
            # 数据已存在,返回错误提示
            err_msg = '数据已存在'
        if new_name and not obj_list:
            # 向数据库插入数据
            ret = models.Publisher.objects.create(name=new_name)
            # 跳转到展示页面
            return redirect('/publisher_list/')
    # 返回一个提交数据的页面(form表单)
    return render(request, 'add_publisher.html', {'err_msg': err_msg, 'new_name': new_name})


# 删除出版社
def del_publisher(request):
    # 获取要删除数据的id
    pk = request.GET.get('pk')
    # 数据不存在给错误提示
    if not models.Publisher.objects.filter(pk=pk):
        return HttpResponse('数据不存在')

    # 数据库删除数据
    models.Publisher.objects.get(pk=pk).delete()
    # 返回到展示页面
    return redirect('/publisher_list/')


# 编辑出版社
def edit_publisher(request):
    # 定义错误提示
    err_msg = ''
    # 获取要编辑对象的ID
    pk = request.GET.get('pk')
    # 从数据库中获取数据
    obj_list = models.Publisher.objects.filter(pk=pk)
    if not obj_list:
        return HttpResponse('数据不存在')
    # 数据存在
    obj = obj_list[0]

    if request.method == 'POST':
        # 获取提交的新的名字
        new_name = request.POST.get('new_name')
        if not new_name:
            err_msg = '不能为空'
        exist = models.Publisher.objects.filter(name=new_name)
        if exist:
            err_msg = '数据已存在'
        if new_name and not exist:
            # 修改出版社的名称
            obj.name = new_name
            obj.save()  # 向数据库提交
            # 返回到展示页面
            return redirect('/publisher_list/')

    return render(request, 'edit_publisher.html', {'obj': obj, 'err_msg': err_msg})


def test(request):
    # 增加
    # obj = models.Publisher.objects.create(name='xx出版社')
    # print(obj)

    # 查询
    ret = models.Publisher.objects.filter(name='xx出版社')
    print(ret)
    return HttpResponse('ok')


# 展示书籍
def book_list(request):
    # 获取所有的书籍对象
    all_books = models.Book.objects.all()
    for i in all_books:
        print(i.publisher, type(i.publisher))  # 出版社对象
        print(i.publisher_id, )  # 直接从book表中获取到出版社的ID
        print(i.publisher.pk, )  # 拿到出版社对象，再获取到ID
        print(i.publisher.name, )
        print('*' * 20)

    return render(request, 'book_list.html', {'all_books': all_books})


# 增加书籍
def add_book(request):
    if request.method == 'POST':
        # 获取提交的数据
        new_name = request.POST.get('new_name')
        publisher_id = request.POST.get('publisher_id')
        # 数据库插入数据
        # publisher_obj = models.Publisher.objects.get(pk=publisher_id)
        # models.Book.objects.create(title=new_name, publisher=publisher_obj)
        models.Book.objects.create(title=new_name, publisher_id=publisher_id)
        # 跳转到展示页面
        return redirect('/book_list/')
    # 获取到所有的出版社信息
    all_publishers = models.Publisher.objects.all()
    return render(request, 'add_book.html', {'all_publishers': all_publishers})


# 删除书籍
def del_book(request):
    # 获取提交的数据pk
    pk = request.GET.get('pk')
    # 查询出对象进行删除
    models.Book.objects.filter(pk=pk).delete()
    # 跳转到展示页面
    return redirect('/book_list/')


# 编辑书籍
def edit_book(request):
    # 获取到要修改对象的id
    pk = request.GET.get('pk')
    # 查询出要修改的对象
    book_obj = models.Book.objects.get(pk=pk)

    if request.method == 'POST':
        # 获取提交的数据
        new_name = request.POST.get('new_name')
        publisher_id = request.POST.get('publisher_id')
        # 修改数据
        book_obj.title = new_name
        book_obj.publisher_id = publisher_id
        # book_obj.publisher = models.Publisher.objects.get(pk=publisher_id)
        book_obj.save()  # 保存到数据库中
        # 跳转到展示页面
        return redirect('/book_list/')

    # 查询出所有的出版社对象
    all_publishers = models.Publisher.objects.all()
    return render(request, 'edit_book.html', {'book_obj': book_obj, 'all_publishers': all_publishers})


# 展示作者
def author_list(request):
    # 获取到所有的作者信息
    all_authors = models.Author.objects.all().order_by('pk')
    # for author in all_authors:
    #     print(author)
    #     print(author.name)
    #     print(author.id)
    #     print(author.books)          # 管理对象
    #     print(author.books.all())    # 作者关联的所有书籍对象
    #     print("*" * 30)
    return render(request, 'author_list.html', {'all_authors': all_authors})


# 增加作者
def add_author(request):
    if request.method == 'POST':
        # 获取提交的数据
        new_name = request.POST.get('name')
        book_ids = request.POST.getlist('books')
        # print(request.POST)
        # print(new_name)
        # print(book_ids)
        # 数据插入到数据库中
        # 创建一个新的作者
        author_obj = models.Author.objects.create(name=new_name)
        # 作者与书籍做多对多的关联
        author_obj.books.set(book_ids)
        return redirect('/author_list/')
    # 获取所有的书籍的信息
    all_books = models.Book.objects.all()
    return render(request, 'add_author.html', {"books": all_books})


# 删除作者
def del_author(request):
    # 从URL上获取要删除对象的ID
    del_id = request.GET.get('pk')
    # 删除对象
    models.Author.objects.get(pk=del_id).delete()
    # models.Author.objects.filter(pk=del_id).delete()
    # 1. 删除了查询的对象
    # 2. 删除了对象的多对多的记录
    return redirect('/author_list/')

# 编辑作者
def edit_author(request):
    # 获取要编辑的作者的ID
    pk = request.GET.get('pk')
    # 获取编辑的对象
    author_obj = models.Author.objects.get(pk=pk)
    if request.method == 'POST':
        # 获取提交的数据
        name = request.POST.get('name')
        book_ids = request.POST.getlist('books')
        # 修改数据
        # 修改了作者名字
        author_obj.name = name
        author_obj.save()
        # 修改作者和书籍多对多的关系
        author_obj.books.set(book_ids)  # 所有的记录都重新设置   不需要save()

        return redirect('/author_list/')

    # 查询所有的书籍
    books = models.Book.objects.all()

    return render(request, 'edit_author.html', {'author_obj': author_obj, 'books': books})
