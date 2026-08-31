from ninja import NinjaAPI



api = NinjaAPI()




@api.get("/testing")
def testing(request):
    return 'Testing FreudLens API'