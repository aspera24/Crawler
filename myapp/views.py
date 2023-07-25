from django.shortcuts import render
from googleapiclient.discovery import build
from .models import S_Result
import wikipedia

def crawl(request):
    if request.method == 'POST':
        query = request.POST.get('url')
        api_key = 'AIzaSyAIXPyAFcARcGR_liTgSliSm5L1M0dv3ag'
        cse_id = '63e015b3ba3d24963'      
        service = build('customsearch', 'v1', developerKey=api_key)    
        try:
            results = service.cse().list(
                q = query,
                cx = cse_id,
                num = 10
            ).execute()   

            items = results.get('items', [])

            for item in items:
                S_Result.objects.create(
                    query = query,
                    title = item['title'],
                    link = item['link'],
                    snippet = item['snippet']
                ) 

            about = None
            try:
                about = wikipedia.summary(query, sentences=4)
            except:
                pass

            return render(request, 'result.html', {'items': items, 'query': query, 'about': about}) 
        except Exception as e:
            error_message = f"Error occurred: {str(e)}"
            return render(request, 'result.html', {'error_message': error_message})

    else:
        return render(request, 'home.html')


