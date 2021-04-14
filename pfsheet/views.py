from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'pfsheet/home.html')

def calculate(request):
    if request.method=='POST':
        uploadedfile = request.FILES['myfile']
        lines = []
        for line in uploadedfile:
            # print(line.decode('ascii').split('#~#'))
            # print(len(line.decode('ascii').split('#~#')))
            temp_list = line.decode('ascii').split('#~#')
            temp_list[1] = temp_list[1].replace(' ', '_')
            temp_list[-1] = temp_list[-1].replace('\r', '')
            temp_list[-1] = temp_list[-1].replace('\n', '')
            lines.append(temp_list)
        context = {
            'lines': lines
        }
        return render(request, 'pfsheet/calculate.html', context=context)

def result(request):
    if request.method=='POST':
        no_of_emps = request.POST.get('no_of_emps')
        # print(no_of_emps)
        emps = []
        for i in range(int(no_of_emps)):
            index = i + 1
            temp_list = [] 
            for j in range(1, 12):
                data = request.POST.get(f"row-{index}-col-{j}")
                temp_list.append(data)
                # print(f"id='row-{index}-col-{j}' is {data}")
            temp_list[1] = temp_list[1].replace('_', ' ')

            emps.append('#~#'.join(temp_list))
        # print(emps)
        context = {
            'emps': emps 
        }
        return render(request, 'pfsheet/result.html', context = context)