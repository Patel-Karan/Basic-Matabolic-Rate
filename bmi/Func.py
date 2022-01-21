def bmi(w,h):
    cal = round(w/((h*0.01)**2),2)
    if cal <= 18.4:
        cat = 'Underweight'
        risk = 'Malnutrition risk'
    elif cal >= 18.5 and cal<= 24.9:
        cat = 'Normal weight'
        risk = 'Low risk'
    elif cal >= 25 and cal<= 29.9:
        cat = 'Overweight'
        risk = 'Enhanced risk'
    elif cal >= 30 and cal<= 34.9:
        cat = 'Moderately obese'
        risk = 'Medium risk'
    elif cal >= 35 and cal<= 39.9:
        cat = 'Severely obese'
        risk = 'High risk'
    else:
        cat = 'Very severely obese'
        risk = 'Very high risk'
    return cal,cat,risk

def bmi_df(df,w,h):
    Cal = []
    Cat = []
    Risk = []
    r,c = df.shape
    for i in range(r):
        a,b,c = bmi(df[w][i],df[h][i])
        Cal.append(a)
        Cat.append(b)
        Risk.append(c)
    df['BMI'] = Cal
    df['BMI_Category'] = Cat
    df['Health_Risk'] = Risk    