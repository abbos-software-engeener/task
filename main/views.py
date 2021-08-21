
from django.http import HttpResponse
from rest_framework.response import Response
import pytube
from youtube_search import YoutubeSearch


from rest_framework.decorators import api_view
from .models import *

@api_view(('GET','POST'))
def start(request):
    print("become")
    yt = pytube.Playlist(request.GET['url'])
    yt2 = pytube
    _data ={
        "id": yt.playlist_id,
        "url": yt.playlist_url,
        "description": yt.description,
        "views": yt.views,
        "length": yt.length,

        "owner": yt.owner,
        "owner_id": yt.owner_id,
        "owner_url": yt.owner_url,
        "video_urls": yt.video_urls,
        "videos": [
            {
                "id": video.video_id,
                "title": video.title,
                "rating": video.rating,
                "views": video.views,
                "streams": [
                    {
                        "resolution": stream.resolution,
                        "fps": stream.fps if "fps" in dir(stream) else "None",
                        "url": stream.url
                    } for stream in video.streams if "fps" in dir(stream)
                ]
            } for video in yt.videos
        ],
    }
    # print(yt.videos[0].streams[0].fps)

    return HttpResponse(str(_data))


@api_view(('GET','POST'))
def get_video(request):
    try:
        data = request.GET
        yt = pytube.YouTube(data['url'])
        _data = {
            "id": yt.video_id,
            "title": yt.title,
            "views": yt.views,
            "rating": yt.rating,
            "thumb_url": yt.thumbnail_url,
            "streams": [
                {
                            "resolution": stream.resolution,
                            "fps": stream.fps if "fps" in dir(stream) else "None",
                            "url": stream.url
                        } for stream in yt.streams if "fps" in dir(stream)
            ]
        }
        return Response({
            "ok": True,
            "error": 0,
            "data": _data
        })
    except Exception as e:
        return Response({
            "ok": False,
            "error": str(e),
            "data": 0
        })


@api_view(("GET", 'POST'))
def search(request):
    data = request.GET
    results = YoutubeSearch(data['q'], max_results=10).to_dict()
    return Response(results)



@api_view(["GET", 'POST'])
def test(request):
    # print("Boshlkanfsdfsk;djfbsugvbsdfz")
    credits = Credit.objects.filter(status=1)
    leasing = Credit.objects.filter(status=2)
    # print(type(credits), "rfsdfisdufysouidjhsidufhsopdiufhsoidufhsodifuhsodifuhsdf")






    _data = {
        "credits":[
            {
                "id": credit.id,
                "title": credit.title,
                "models":[
                    {
                        "id": model.id,
                        "title": model.title,
                        "credit": [
                          {
                            "month": credit.month,
                            "payments":[
                              {
                                "id": payment.id,
                                "order": payment.order,
                                "sum": payment.sum,
                                "percent": payment.percent,
                                "total": payment.total,
                                "remain": payment.remain
                              } for payment in Payment.objects.filter(credit=_credit.id)
                            ]
                          } for _credit in Credit.objects.filter(model=model.id)
                        ]
                    } for model in credit.model.select_related()
                ]
            } for credit in credits
        ],
        "leasing": [
            {
                "id": leasing.id,
                "title": leasing.title,
                "models":[
                    {
                        "id": model.id,
                        "title": model.title,
                        "credit": [
                          {
                            "month": _credit.month,
                            "payments":[
                              {
                                "id": payment.id,
                                "order": payment.order,
                                "sum": payment.sum,
                                "percent": payment.percent,
                                "total": payment.total,
                                "remain": payment.remain
                              } for payment in Payment.objects.filter(credit=_credit.id)
                            ]
                          } for _credit in Credit.objects.filter(model=model.id)
                        ]
                    } for model in leasing.model.select_related()
                ]
            } for leasing in leasing
        ],
    }
    return Response(_data)


