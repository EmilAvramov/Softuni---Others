from .models import Profile, Plant
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name"]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name", "profile_picture"]
class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"


class DeletePlantForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
