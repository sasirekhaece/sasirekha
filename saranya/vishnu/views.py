from django.shortcuts import render
from docx import *


def index(request):
    li = []
    dummy = ""
    if request.method == 'POST':
        f = str(request.FILES['document']).split(".")
        print(f[1])
        if f[1] != "docx":
            return render(request, 'doc_error.html')
        mul = request.FILES['document']
        d = Document(mul)
        for t in d.paragraphs:
            s = t.text.split()
            for x in s:
                dummy = " "
                if x != ':':
                    dummy += x
            li.append(dummy)
        data = {'firstname': li[0], 'lastname': li[1], 'mobileno': li[2], 'street': li[3], 'city': li[4], 'state': li[5], 'country': li[6], 'pincode': li[7],
                'educationalqualification': li[8], 'workexperience': li[9]
                }
        if li[0] == " " or li[1] == " " or len(li[2]) != 10 or li[3] == " " or li[4] == " " or li[5] == " " or li[6] == " " or len(li[7]) != 6 or li[8] == " " or li[9] == " ":
            return render(request, 'emptyerror.html', data)
        form = StudentForm(data)
        if form.is_valid():
            form.save(data)
            return redirect('/index')
        else:
            return render(request, 'resume.html', data)
    return render(request, 'index.html')

