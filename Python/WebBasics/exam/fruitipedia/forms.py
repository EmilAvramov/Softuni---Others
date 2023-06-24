from .models import ProfileModel, FruitModel
from django import forms


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_attributes()

    def __set_attributes(self):
        for field in self.fields.values():
            field.label = False

        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password"].widget.attrs["placeholder"] = "Password"

    class Meta:
        model = ProfileModel
        fields = ["first_name", "last_name", "email", "password"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ["first_name", "last_name", "image_url", "age"]


class FruitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_attributes()

    def __set_attributes(self):
        for field in self.fields.values():
            field.label = False

        self.fields["name"].widget.attrs["placeholder"] = "Fruit Name"
        self.fields["image_url"].widget.attrs[
            "placeholder"
        ] = "Fruit Image URL"
        self.fields["description"].widget.attrs[
            "placeholder"
        ] = "Fruit Description"
        self.fields["nutrition"].widget.attrs["placeholder"] = "Nutrition Info"
        self.fields["nutrition"].required = False

    class Meta:
        model = FruitModel
        fields = "__all__"


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = "__all__"


class DeleteFruitForm(FruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_attributes()

    def __set_attributes(self):
        for field in self.fields.values():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
