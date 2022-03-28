from typing import Dict, Tuple
from django.views.decorators.csrf import csrf_exempt
from ninja import Router, Form
from search.service.like_cancel_service import like_cancel_shopping, like_cancel_book
from ninja.errors import HttpError
from accounts.models import CustomUser
from search.apis.v1.schemas import YoutubeLikeRequest, YoutubeLikeResponse
from search.models import Book, News, Shopping, Youtube
from search.service.like_cancel_service import like_cancel_youtube

router = Router(tags=["like_cancel"])


@csrf_exempt
@router.post("/youtube", response={201: YoutubeLikeResponse})
def cancel_like_youtube(request, youtube_request: YoutubeLikeRequest = Form(...)) -> Tuple[int, Dict]:
    try:
        like_cancel_youtube(request.user.id, youtube_request.url)
    except CustomUser.DoesNotExist:
        raise HttpError(404, "User does not Exist")
    except Youtube.DoesNotExist:
        raise HttpError(404, "Youtube does not Exist")
    return 201, {"result": "success"}


@csrf_exempt
@router.post("/news", response={201: NewsLikeResponse})
def cancel_like_shopping(request, news_request: NewsLikeRequest = Form(...)) -> Tuple[int, Dict]:):
    try:
        like_cancel_news(request.user.id, news_request.url)
    except CustomUser.DoesNotExist:
        raise HttpError(404, 'User does not Exist')
    except News.DoesNotExist:
        raise HttpError(404, 'News does not Exist')
    return 201, {'result': 'success'}


@csrf_exempt
@router.post("/book", response={201: BookLikeResponse})
def cancel_like_book(request, book_request: BookLikeRequest = Form(...)) -> Tuple[int, Dict]:
    try:
        like_cancel_book(user_id=2, book_link=book_request.link)
    except CustomUser.DoesNotExist:
        raise HttpError(404, 'User does not exist')
    except Book.DoesNotExist:
        raise HttpError(404, 'Book does not exist')
    return 201, {'result': 'success'}


@csrf_exempt
@router.post("/shopping", response={201: ShoppingLikeResponse})
def cancel_like_shopping(request, shopping_request: ShoppingLikeRequest = Form(...)):
    try:
        like_cancel_shopping(
            user_id=request.user.id,
            shopping_link=shopping_request.link
        )
    except CustomUser.DoesNotExist:
        raise HttpError(404, 'User does not Exist')
    except Shopping.DoesNotExist:
        raise HttpError(404, 'Shopping does not Exist')
    return 201, {'result': 'success'}

