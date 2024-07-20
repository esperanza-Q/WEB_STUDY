# 수정
from django.shortcuts import render, get_object_or_404, redirect

# View에 Model(Post 게시글) 가져오기
from .models import Post

# Create your views here.

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장한다.
    postlist = Post.objects.all()
    return render(request, 'blog.html', {'postlist': postlist})

# blog의 게시글(posting)을 부르는 posting 함수
#수정
def posting(request, post_id):
    
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)을 검색
    
    #수정
    # post=get_object_or_404(Post, pk=post_id)
    post = Post.objects.get(pk=post_id)
    
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져온다.
    return render(request, 'posting.html', {'post': post})

# 수정
def new_post(request):
    if request.method == 'POST':
        postname=request.POST['postname']
        contents=request.POST['contents']
        
        if postname and contents:
            new_article = Post.objects.create(
                postname=postname,
                contents=contents,
                # user=request.user
            )
            return redirect('blog')
    else:
        return render(request, 'new_post.html')
        
#혹시나 글 목록에 제목들이 ('제목'),로 나오는 경우 추가로 해야할 것 :
#cmd창에 프로젝트까지 들어간 상태에서
#python manage.py shell
#이후 나오는 >>부분에 밑에 코드들 작성
#from main.models import Post
#for post in Post.objects.all():
#    print(post.postname, type(post.postname))
#위 코드 작성하고 엔터. 이때, ('제목',) <class 'tuple'> 이런 식으로 뜨면, 밑에 코드들 이어 작성(만약 tuple 자리에 string 또는 str이 뜨면 코드 자체를 잘못 작성한 거거나 그 이외의 오류.)
#for post in Post.objects.all():
#   if isinstance(post.postname, tuple):
#       post.postname = post.postname[0]  # 튜플의 첫 번째 요소를 문자열로 저장
#       post.save()
#코드 작성 후 엔터.
#for post in Post.objects.all():
#   print(post.postname, type(post.postname))
#코드 작성 후 엔터. 이때 <class 'string'> 또는 <class 'str'> 뜨면 된 것.
#다시 마이그레이션하고 실행시키면 제목이 제대로 저장되는 것 확인할 수 있음.
