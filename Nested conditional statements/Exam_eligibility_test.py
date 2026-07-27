medical_cause = input("did you have a medical cause? (Y/N):").strip().upper()

if medical_cause == "Y":
    print("you are allowed")
else:
    atten = int(input("enter the attendance of the student:"))

    if atten >= 75:
        print("ALLOWED")
    else:
        print("NOT ALLOWED")