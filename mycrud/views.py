from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import students
from .forms import StudentForm
                            # ---- class view-----#
# ListView for displaying all students
class StudentListView(ListView):
    model = students
    template_name = "index.html" 
    context_object_name = "emp" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students_list = students.objects.all()
        for student in students_list:
            student.update_form = StudentForm(instance=student)
        context['emp'] = students_list  
        context['form'] = StudentForm()  
        return context

# CreateView for adding a student
class StudentCreateView(CreateView):
    model = students
    form_class = StudentForm
    # fields = ['name', 'email', 'course', 'address', 'phone']
    template_name = "index.html"  
    success_url = reverse_lazy('index')  
    context_object_name = "emp"
    
    def form_valid(self, form):
        messages.success(self.request, "🎉 Student added successfully! ")
        return super().form_valid(form)

# UpdateView for updating student details
class StudentUpdateView(UpdateView):
    model = students
    form_class = StudentForm
    template_name = "index.html"  
    success_url = reverse_lazy('index')
    context_object_name = "emp"

    def form_valid(self, form):
        messages.success(self.request, "✅ Student details updated successfully!")
        return super().form_valid(form)

# DeleteView for deleting a student
class StudentDeleteView(DeleteView):
    model = students
    template_name = "index.html"  
    success_url = reverse_lazy('index')

    
            # ---- function view-----#
# from django.shortcuts import render, redirect
# from .models import students
# # Create your views here.
# def INDEX(request):
#     emp = students.objects.all()
#     context = {
#         'emp': emp,
#     }
#     return render(request, "index.html", context)

# def Add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         course = request.POST.get('course')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')

#         emp = students(name=name, email=email, course = course, address=address, phone=phone)
#         emp.save()
        
#         return redirect('index')  

#     return render(request, "index.html")

# def Edit(request):
#     emp = students.objects.all()
#     context = {
#         'emp': emp,
#     }
#     return redirect(request,'index.html', context)

# def Update(request,id):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         course = request.POST.get('course')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
        
#         emp = students(
#             id = id,
#             name=name, email= email, course = course, address=address, phone=phone
#         )

#         emp.save()
#         return redirect('index')
#     return redirect(request, 'index.html')

# def Delete(request, id):
#     emp = students.objects.filter(id=id)
#     emp.delete()
#     return redirect('index')