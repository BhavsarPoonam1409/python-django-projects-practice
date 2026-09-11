from django import forms

class Userform(forms.Form):



    #  full name : 2 words (fname lname), atleast one space should be there 
    # jo hn




    name = forms.CharField(
        label = "Enter your Name",
        required = False,
        initial= "John",
        widget = forms.TextInput(
            attrs = {
                "placeholder" : "Enter your name"
            }
        )
    )
    email = forms.EmailField(
        label = "Enter your Email"
    )
    age = forms.IntegerField(
        min_value = 18,
        max_value = 60
    )

    mobile = forms.CharField(
        max_length = 12,
        min_length = 12,
    )
    gender = forms.MultipleChoiceField(
        choices = [
            ("M","Male"),
            ("F", "Female"),
            ("O", "other")
        ]
    )

    agree = forms.BooleanField(
        label = "I agree with the terms"
    )

    password = forms.CharField(
        widget = forms.PasswordInput()
    )

    def clean_mobile(self):
        mobileno = self.cleaned_data["mobile"]
       
        if(mobileno[0:2]  != "91" ):
            raise forms.ValidationError(
                "mobile no has to start with 91"
            )