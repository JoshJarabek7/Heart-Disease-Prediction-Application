import pickle

import joblib
import pandas as pd

with open("../Models/model_rf.pkl", "rb") as f:
    model = joblib.load(f)

with open("../Models/scaler.pkl", "rb") as f:
    scaler = joblib.load(f)


def data():
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print('Welcome to the Heart Disease Prediction Application!')
    print('Please enter your information below:')
    print('----------------------------------------------')
    print('Press enter to continue...')
    input()
    print('----------------------------------------------')

    race_asian = race_black = race_hispanic = race_aian = race_white = race_other = 0
    db_yes = db_no = db_no_border = db_yes_preg = 0
    bmi_underweight = bmi_normal = bmi_overweight = bmi_obese = bmi_extreme_obese = 0
    low_sleep = mid_sleep = high_sleep = 0
    mean_age = 0
    skin_cancer = 0
    kidney = 0
    asthma = 0
    gen_health = 0
    physical_health = 0
    diff_walk = 0
    physically_active = 0
    sex = 0
    smoking = 0
    stroke = 0

    print(
        'Please Enter Your Race: \n'
        '1. Asian \n'
        '2. Black \n'
        '3. Hispanic \n'
        '4. American Indian / Alaskan Native \n'
        '5. White \n'
        '6. Other \n')
    race = int(input())
    if race == 1:
        race_asian = 1
    elif race == 2:
        race_black = 1
    elif race == 3:
        race_hispanic = 1
    elif race == 4:
        race_aian = 1
    elif race == 5:
        race_white = 1
    elif race == 6:
        race_other = 1
    else:
        print("Invalid input")

    print('Please enter your age: \n'
          '1. 18-24 \n'
          '2. 25-29 \n'
          '3. 30-34 \n'
          '4. 35-39 \n'
          '5. 40-44 \n'
          '6. 45-49 \n'
          '7. 50-54 \n'
          '8. 55-59 \n'
          '9. 60-64 \n'
          '10. 65-69 \n'
          '11. 70-74 \n'
          '12. 75-79 \n'
          '13. 80 or older \n')

    age = int(input())

    if age == 1:
        mean_age = 21
    elif age == 2:
        mean_age = 27
    elif age == 3:
        mean_age = 32
    elif age == 4:
        mean_age = 37
    elif age == 5:
        mean_age = 42
    elif age == 6:
        mean_age = 47
    elif age == 7:
        mean_age = 52
    elif age == 8:
        mean_age = 57
    elif age == 9:
        mean_age = 62
    elif age == 10:
        mean_age = 67
    elif age == 11:
        mean_age = 72
    elif age == 12:
        mean_age = 77
    elif age == 13:
        mean_age = 80
    else:
        print("Invalid input")

    print('Please enter your BMI: \n'
          '1. Less Than 18.5 \n'
          '2. 18.5 to 24.9 \n'
          '3. 24.9 to 29.9 \n'
          '4. 29.9 to 34.9 \n'
          '5. Over 34.9 \n')
    bmi = int(input())
    if bmi == 1:
        bmi_underweight = 1
    elif bmi == 2:
        bmi_normal = 1
    elif bmi == 3:
        bmi_overweight = 1
    elif bmi == 4:
        bmi_obese = 1
    elif bmi == 5:
        bmi_extreme_obese = 1
    else:
        print("Invalid input")

    print(
        'Do you smoke?: \n'
        '1. No \n'
        '2. Yes \n'
    )
    smoke_input = int(input())
    if smoke_input == 1:
        smoking = 0
    elif smoke_input == 2:
        smoking = 1
    else:
        print("Invalid input")

    print("Please Enter Your Sex: \n"
          "1. Female \n"
          "2. Male")
    sex_input = int(input())
    if sex_input == 1:
        sex = 0
    elif sex_input == 2:
        sex = 1
    else:
        print("Invalid Input")

    print("Have You Ever Had A Stroke? \n"
          "1 - No \n"
          "2 - Yes \n")
    stroke_input = int(input())

    if stroke_input == 1:
        stroke = 0
    elif stroke_input == 2:
        stroke = 1
    else:
        print("Invalid Input")

    print("In The Past Month, How Many Days Have You Had Physical Health Problems? \n")
    physical_health_input = float(input())
    if 0 <= physical_health_input <= 30:
        physical_health = physical_health_input
    else:
        print("Invalid Input")

    print("Do You Have Difficulty Walking? \n"
          "1 - No \n"
          "2 - Yes \n")
    diff_walking = int(input())
    if diff_walking == 1:
        diff_walk = 0
    elif diff_walking == 2:
        diff_walk = 1
    else:
        print("Invalid Input")

    print("Do You Exercise? \n"
          "1 - No \n"
          "2 - Yes \n")
    exercise = int(input())
    if exercise == 1:
        physically_active = 0
    elif exercise == 2:
        physically_active = 1
    else:
        print("Invalid Input")

    print(" In General, Your Health Is: \n"
          "1 - Poor \n"
          "2 - Fair \n"
          "3 - Good \n"
          "4 - Very Good \n"
          "5 - Excellent \n")
    gen_health_input = int(input())
    if gen_health_input == 1:
        gen_health = 0
    elif gen_health_input == 2:
        gen_health = 1
    elif gen_health_input == 3:
        gen_health = 2
    elif gen_health_input == 4:
        gen_health = 3
    elif gen_health_input == 5:
        gen_health = 4
    else:
        print("Invalid Input")

    print("Do You Have Asthma? \n"
          "1 - No \n"
          "2 - Yes \n")
    asthma_input = int(input())
    if asthma_input == 1:
        asthma = 0
    elif asthma_input == 2:
        asthma = 1
    else:
        print("Invalid Input")

    print("Do You Have Kidney Disease? \n"
          "1 - No \n"
          "2 - Yes \n")
    kidney_input = int(input())
    if kidney_input == 1:
        kidney = 0
    elif kidney_input == 2:
        kidney = 1
    else:
        print("Invalid Input")

    print("Do You Have Skin Cancer? \n"
          "1 - No \n"
          "2 - Yes \n")
    skin_cancer_input = int(input())
    if skin_cancer_input == 1:
        skin_cancer = 0
    elif skin_cancer_input == 2:
        skin_cancer = 1
    else:
        print("Invalid Input")

    print("Do You Have Diabetes? \n"
          "1 - Yes \n"
          "2 - Yes (during pregnancy) \n"
          "3 - No, borderline diabetes \n"
          "4 - No \n")
    diabetes_input = int(input())
    if diabetes_input == 1:
        db_yes = 1
    elif diabetes_input == 2:
        db_yes_preg = 1
    elif diabetes_input == 3:
        db_no_border = 1
    elif diabetes_input == 4:
        db_no = 1
    else:
        print("Invalid Input")

    print("On Average, How Many Hours Do You Sleep? \n"
          "1 - Less Than 6 Hours \n"
          "2 - 6 to 9 Hours \n"
          "3 - More Than 9 Hours \n")
    sleep_input = int(input())
    if sleep_input == 1:
        low_sleep = 1
    elif sleep_input == 2:
        mid_sleep = 1
    elif sleep_input == 3:
        high_sleep = 1
    else:
        print("Invalid Input")

    df = pd.DataFrame({
        "Mean_Age": [mean_age],
        "SkinCancer": [skin_cancer],
        "KidneyDisease": [kidney],
        "Asthma": [asthma],
        "GenHealth": [gen_health],
        "PhysicalHealth": [physical_health],
        "DiffWalking": [diff_walk],
        "PhysicalActivity": [physically_active],

        "Diabetic_No, borderline diabetes": [db_no_border],
        "Diabetic_Yes": [db_yes],
        "Diabetic_Yes (during pregnancy)": [db_yes_preg],
        "Diabetic_No": [db_no],
        "Sex": [sex],

        "BMI_Extremely obese": [bmi_extreme_obese],
        "BMI_Obese": [bmi_obese],
        "BMI_Normal": [bmi_normal],
        "BMI_Overweight": [bmi_overweight],
        "BMI_Underweight": [bmi_underweight],

        "Race_Asian": [race_asian],
        "Race_Black": [race_black],
        "Race_White": [race_white],
        "Race_Hispanic": [race_hispanic],
        "Race_American Indian/Alaskan Native": [race_aian],
        "Race_Other": [race_other],

        "SleepTime_High": [high_sleep],
        "SleepTime_Normal": [mid_sleep],
        "SleepTime_Low": [low_sleep],

        "Smoking": [smoking],
        "Stroke": [stroke],

    })

    col = df.columns
    test = scaler.transform(df)

    X_test = pd.DataFrame(test, columns=col)
    result = model.predict(X_test)

    if result[0] == 1:
        end_result = "You're at risk of Heart Disease"
    else:
        end_result = "You're not at risk of Heart Disease"
    print(end_result)