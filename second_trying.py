import random

male_data = {
    12:63.8,
    13:64.1,
    14:64.5,
    15:64.8,
    16:65.2,
    17:65.5,
    18:65.8,
    19:66.1,
    20:66.4,
    21:66.7,
    22:67.0,
    23:67.3,
    24:67.5
}
female_data = {
    12:63.8,
    13:65.5,
    14:66.1,
    15:66.7,
    16:67.2,
    17:67.8,
    18:68.3,
    19:68.8,
    20:69.3,
    21:69.8,
    22:70.2,
    23:70.7,
    24:71.1
}

#kx+c formula

k = random.uniform(-5,5)
c = random.uniform(-5,5)

rate = 0.001

def do_math(x):
    return k*x+c

#n = amount of lessons
n = (10**6) + 5*(10**5)
#input gender and age
def get_gender():
    gender = input('Your gender (m/f): ')
    if gender == 'm' or gender == 'f':
        pass
    else:
        get_gender()
gender = get_gender()
def get_age():
    try:
        age = int(input('Now your age: '))
        return age
    except ValueError or TypeError:
        get_age()
age = get_age()

#learning session and counting stuff

if gender == 'm':
    for i in range(n):
        x = random.choice(list(male_data.keys()))
        co_a = male_data[x]
        ai_a = do_math(x)
        delta = co_a - ai_a
        k += delta*rate*x
        c += delta*rate
    To1 = male_data[24]
    To2 = To1 - age
    ToWhatYear = To2 + 24
    lifespanThere = k*ToWhatYear+c

else:
    for i in range(n):
        x = random.choice(list(female_data.keys()))
        co_a = female_data[x]
        ai_a = do_math(x)
        delta = co_a - ai_a
        k += delta*rate*x
        c += delta*rate
    To1 = female_data[24]
    To2 = To1 - age
    if To2 < 0:
        To2 = age
    ToWhatYear = int(To2 + 24)
    lifespanThere = int(k*ToWhatYear+c)
if ToWhatYear < 100:
    print(f"""
    You will be around {lifespanThere} when you die,
    You will live up to 20{ToWhatYear},
    You have {lifespanThere-age} years to live.
    """)
else:
    print(f"""
    You will be around {lifespanThere} when you die,
    You will live up to 2{ToWhatYear},
    You have {lifespanThere-age} years to live.
    """)
