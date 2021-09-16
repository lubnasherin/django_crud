from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # If we want the fields inside the forms then follow step:
        # fields = '__all__'  or we can specify the fields
        fields = ('fullname','mobile'

                  ,'emp_code','position')
        labels= {
            'fullname' : 'Full Name',
            'emp_code' : 'Employee Code',
            'mobile'   : 'Mobile',
            'position' : 'Position'

        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__( *args, **kwargs)
        self.fields['position'].empty_label = "select"

        self.fields['emp_code'].required = False    # to remove maditory fields