from django.shortcuts import get_object_or_404, redirect, render

from . forms import BookForm
from . models import Book

# Create your views here.

def index(request):
    return render(request, 'book_app/index.html')

def book_list(request):
    # DB에서 select한 결과 반환 (모든 상품 데이터 반환)
    # book.objects.all() 사용
    books = Book.objects.all()
    return render(request, 'book_app/book_list.html', {'books':books})

# 상세 상품 조회
# 전달받은 prd_no에 해당되는 1개 상품 데이터 반환
def book_detail(request, book_no):
    # prd_no 조건에 맞는 행 select
    # get_object_or_404() 사용
    book = get_object_or_404(Book, pk=book_no)
    return render(request, 'book_app/book_detail.html', {'book':book})

def book_insert(request):
    # (1) 요청이 POST 인지 확인하고
    if request.method == "POST":
        # (2) 폼 데이터의 내용을 form 변수에 저장
        form = BookForm(request.POST)
        # (3) Django의 기본 기능인 is_valid() 사용해서 데이터 유효성 확인
        if form.is_valid():
            # (4) form에 저장된 데이터를 아직 완전 저장하지 않고
            # (현재는 이 부분 없어도 됨 : 저장 지연)
            book = form.save(commit=False)
            # 수행할 작업이 있다면 여기서 수행 (우리는 현재 다른 작업 없음)
            # product....() 작업
            # (5) 여기에서 DB 저장 
            book.save()
            # (6) DB에 저장 후 결과 확인하기 위해 상품조회 화면으로 이동 (포워딩) 
            # redirect() 사용
            return redirect('book_list')
    else:
        form = BookForm()

    # (7) else : POST 요청이 아니라면 입력 폼 그대로 출력
    return render(request, 'book_app/book_form.html', {'form':form})

# 상품정보 수정
def book_update(request, book_no):
    # (1) 전달받은 prd_no에 해당되는 상품 정보 가져와서
    book = get_object_or_404(Book, pk = book_no)
    # (2) 요청이 POST 인지 확인하고 : 데이터 입력하고 서버로 전송
    if request.method == "POST":
        # (3) 가져온 product 데이터의 내용을 form 변수에 저장
        form = BookForm(request.POST, instance=book)
        # (4) Django의 기본 기능인 is_valid() 사용해서 데이터 유효성 확인
        if form.is_valid():
            # (5) form에 저장된 데이터를 아직 완전 저장하지 않고
            # (현재는 이 부분 없어도 됨 : 저장 지연)
            book = form.save(commit=False)
            # 수행할 작업이 있다면 여기서 수행 (우리는 현재 다른 작업 없음)
            # product....() 작업
            # (6) 여기에서 DB 저장 
            book.save()
            # (7) DB에 저장 후 결과 확인하기 위해 상품조회 화면으로 이동 (포워딩) 
            # redirect() 사용
            return redirect('book_list')
    else:
        form = BookForm(instance=book)    #  처음 폼 화면 출력
        # 폼에 prd_no에 해당되는 상품 데이터 출력

    # (7) else : POST 요청이 아니라면 입력 폼 그대로 출력
    return render(request, 'book_app/book_update.html', {'form':form})

def book_delete(requst, book_no):
    # bookno에 해당되는 상품 찾아와서
    book = get_object_or_404(Book, pk=book_no)

    # 상품 데이터 삭제
    book.delete()

    # 상품 조회화면으로 이동 (포워딩)
    return redirect('book_list')