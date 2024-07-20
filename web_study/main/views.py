from django.shortcuts import render
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
def posting(request, pk):
    
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)을 검색
    post = Post.objects.get(pk=pk)
    
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져온다.
    return render(request, 'posting.html', {'post': post})

def new_post(request):
    if request.method == 'POST':
        new_article=Post.objects.create(
            postname=request.POST['postname'],
            contents=request.POST['contents'],
        )
    return render(request, 'new_post.html')