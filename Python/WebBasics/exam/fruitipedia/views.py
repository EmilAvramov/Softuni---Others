from django.shortcuts import render
from . import forms, models
from django.shortcuts import redirect


def index(request):
    profile = models.ProfileModel.objects.first()
    return render(request, "index.html", {"profile": profile})


def dashboard(request):
    fruits = models.FruitModel.objects.all()
    profile = models.ProfileModel.objects.first()
    return render(
        request, "dashboard.html", {"profile": profile, "fruits": fruits}
    )


def profile_create(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("fruitipedia:dashboard")
        else:
            return render(request, "create-profile.html", {"form": form})
    else:
        form = forms.ProfileForm()
        return render(request, "create-profile.html", {"form": form})


def profile_details(request):
    profile = models.ProfileModel.objects.first()
    fruits = models.FruitModel.objects.all()
    return render(
        request, "details-profile.html", {"profile": profile, "fruits": fruits}
    )


def profile_edit(request):
    profile = models.ProfileModel.objects.first()

    if request.method == "POST":
        form = forms.ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("fruitipedia:profile_details")
        else:
            return render(
                request,
                "edit-profile.html",
                {"profile": profile, "form": form},
            )

    else:
        form = forms.ProfileEditForm(initial=profile.__dict__)

        return render(
            request, "edit-profile.html", {"profile": profile, "form": form}
        )


def profile_delete(request):
    profile = models.ProfileModel.objects.first()
    fruits = models.FruitModel.objects.all()

    if request.method == "POST":
        profile.delete()
        fruits.delete()
        return redirect("fruitipedia:index")

    else:
        return render(request, "delete-profile.html", {"profile": profile})


def fruit_create(request):
    profile = models.ProfileModel.objects.first()
    if request.method == "POST":
        form = forms.FruitForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("fruitipedia:dashboard")
        else:
            return render(
                request,
                "create-fruit.html",
                {"profile": profile, "form": form},
            )
    else:
        form = forms.FruitForm()
        return render(
            request, "create-fruit.html", {"profile": profile, "form": form}
        )


def fruit_details(request, fruit_id):
    profile = models.ProfileModel.objects.first()
    fruit = models.FruitModel.objects.get(id=fruit_id)
    return render(
        request, "details-fruit.html", {"profile": profile, "fruit": fruit}
    )


def fruit_edit(request, fruit_id):
    fruit = models.FruitModel.objects.get(id=fruit_id)
    profile = models.ProfileModel.objects.first()
    if request.method == "POST":
        form = forms.FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect("fruitipedia:dashboard")
        else:
            return render(
                request, "edit-fruit.html", {"profile": profile, "form": form}
            )

    else:
        form = forms.FruitEditForm(initial=fruit.__dict__)
        return render(
            request, "edit-fruit.html", {"profile": profile, "form": form}
        )


def fruit_delete(request, fruit_id):
    fruit = models.FruitModel.objects.get(id=fruit_id)

    if request.method == "GET":
        form = forms.DeleteFruitForm(initial=fruit.__dict__)
        profile = models.ProfileModel.objects.first()
        return render(
            request, "delete-fruit.html", {"profile": profile, "form": form}
        )
    else:
        fruit.delete()
        return redirect("fruitipedia:dashboard")
