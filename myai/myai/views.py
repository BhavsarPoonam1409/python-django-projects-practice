from django.shortcuts import render
from google import genai

def home(request):
    qus =""
    finalresponse =""
    try:
        if(request.method == "POST"):
            qus = request.POST.get("question")
            print(qus)
    except:
        pass

    myclient = genai.Client(api_key='')
    response = myclient.models.generate_content(
        model="gemini-3-flash-preview",
        contents= qus
    )

    finalresponse = response.text

    context ={
        "ans" :finalresponse
    }

    return render(request,"index.html",context)