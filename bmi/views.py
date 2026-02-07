from django.shortcuts import render

def home(request):
    context = {}

    if request.method == "POST":
        try:
            weight = float(request.POST.get("weight"))
            height_cm = float(request.POST.get("height"))
            height_m = height_cm / 100

            bmi = round(weight / (height_m ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            context = {
                "bmi": bmi,
                "category": category
            }

        except Exception:
            context = {
                "error": "Please enter valid numbers"
            }

    return render(request, "bmi/home.html", context)