from django.shortcuts import render
from . import forms, models
from django.shortcuts import redirect


def home(request):
    profile = models.Profile.objects.first()
    return render(request, "home-page.html", {"profile": profile})


def catalogue(request):
    plants = models.Plant.objects.all()
    profile = models.Profile.objects.first()
    return render(
        request, "catalogue.html", {"plants": plants, "profile": profile}
    )


def profile_create(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("myplant:catalogue")
    else:
        form = forms.ProfileForm()
        return render(request, "create-profile.html", {"form": form})


def profile_details(request):
    profile = models.Profile.objects.first()
    plants = models.Plant.objects.all()
    return render(
        request, "profile-details.html", {"profile": profile, "plants": plants}
    )


def profile_edit(request):
    profile = models.Profile.objects.first()

    if request.method == "POST":
        form = forms.ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("myplant:profile_details")
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
    profile = models.Profile.objects.first()
    plants = models.Plant.objects.all()

    if request.method == "POST":
        profile.delete()
        plants.delete()
        return redirect("myplant:home")

    else:
        return render(request, "delete-profile.html", {"profile": profile})


def plant_create(request):
    if request.method == "POST":
        form = forms.PlantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("myplant:catalogue")
    else:
        form = forms.PlantForm()
        profile = models.Profile.objects.first()
        return render(
            request, "create-plant.html", {"profile": profile, "form": form}
        )


def plant_details(request, plant_id):
    profile = models.Profile.objects.first()
    plant = models.Plant.objects.get(id=plant_id)
    return render(
        request, "plant-details.html", {"profile": profile, "plant": plant}
    )


def plant_edit(request, plant_id):
    plant = models.Plant.objects.get(id=plant_id)
    if request.method == "POST":
        form = forms.PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect("myplant:catalogue")
        else:
            return render(
                request, "edit-plant.html", {"profile": profile, "form": form}
            )

    else:
        form = forms.PlantForm(initial=plant.__dict__)
        profile = models.Profile.objects.first()
        return render(
            request, "edit-plant.html", {"profile": profile, "form": form}
        )


def plant_delete(request, plant_id):
    plant = models.Plant.objects.get(id=plant_id)
    profile = models.Profile.objects.first()

    if request.method == "GET":
        form = forms.DeletePlantForm(initial=plant.__dict__)
        profile = models.Profile.objects.first()
        return render(
            request, "delete-plant.html", {"profile": profile, "form": form}
        )
    else:
        plant.delete()
        return redirect("myplant:catalogue")
