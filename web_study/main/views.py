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