def bp(sys, dia):
    if dia < 80:
        if sys < 120:
            return "You have normal BP levels"

        elif sys < 130:
            return "You have slightly elevated BP levels"


    elif dia < 90 or sys < 140:
        return "You have High Blood Pressure (Hypertension) Stage 1"

    elif dia < 120 or sys < 180:
        return "You have High Blood Pressure (Hypertension) Stage 2"

    else:
        return "You have a Hypertensive Crisis!"

def tot_cholesterol(tot_chol):

# https://my.clevelandclinic.org/health/articles/17385-cardiovascular-disease-prevention--reversal
# You can use the info in the above link to put up more info in the insights
# Also change the form to add cholestrol levels instead of just categories

    if tot_chol <= 200:
        return "You have normal cholesterol levels"

    elif tot_chol < 240:
        return "You have boderline high cholesterol levels!"

    elif tot_chol >= 240:
        return "You have very high cholestrol levels"


def ldl_cholestrol(ldl):

#Ask user to input ldl levels in the form

    if ldl < 100:
        return "Optimal LDL levels"

    elif ldl <130:
        return "Near optimal/above optimal"

    elif ldl <160:

        return "Borderline high"

    elif ldl < 190:

        return "High!"

    elif >= 190:

        return "Very High!"

def hdl_cholestrol(hdl):

#Ask user to input hdl levels in the form

    if hdl < 40:
        return "Your HDL level is a Major risk factor! It's increasing the risk of developing heart diseases"

    elif hdl>= 60:
        return "You have desirable levels of HDL - helps to lower risk ofheart disease"

def triglycerides(tri):

#Ask user to input triglyceride levels in the form

    if tri < 150 :
        return "Normal levels"

    elif tri <200:
        return "Borderline high!"

    elif tri < 500:
        return "High!"

    elif tri >= 500:
        return "Very High!"


def cig_per_day(x):

    #Ask user to input cigarettes smoked per day in the form

    if x == 0:
        return "No risk"
    elif x <= 5:
        return "Even low levels of exposure to tobacco, such as a few cigarettes per day, occasional smoking, or exposure to secondhand tobacco smoke are sufficient to substantially increase risk of cardiac events. Please visit these sites for more information: https://www.health.harvard.edu/newsletter_article/light-and-social-smoking-carry-cardiovascular-risks , https://tobaccocontrol.bmj.com/content/14/5/315"

    else:
        return "Tobacco use is the single most preventable cause of cardiovascular diseases (CVDs). A person’s risk of heart attack greatly increases with the number of cigarettes he or she smokes. There is no safe amount of smoking. Smokers continue to increase their risk of heart attack the longer they smoke. People who smoke a pack of cigarettes a day have more than twice the risk of heart attack than nonsmokers. It is highly recommended that you quit the use of all tobacco prouducts. Please visit these sites for more information: https://www.fda.gov/tobacco-products/health-information/how-smoking-affects-heart-health"

def alcohol_consumption(gender, alcohol, drinks):

    # alc_type = {1 : 'beer', 2: 'wine', 3: 'spirits'}
    # %abV (alcohol by volume) = {beer: 5%, wine: 12%, spirts: 40%}
    # proof = 2 * %abV
    # A wine at 12.5 % vol contains 12.5ml of alcohol/100ml of wine x 0.8 g/ml = 10g of alcohol/100 ml of wine.
    # volume_per_day is in ml
    # 'drinks' should be dictionary of { type of drink : volume in ml } Example : drinks = {1 : 120, 2 : 300, 3: 0} is 120 ml of beer and 300 ml of wine

    if alcohol == 1: #Drinks alcohol


        gperday_user = 0

        for drink in drinks:

            abV_dict = {1 : 5, 2: 12, 3: 40}

            for key in abV_dict:
                if key == drink:
                    abV = abV_dict[key]

            vol = drinks[drink]
            ml_of_pure_ethanol = ((abV * vol)/100)

            g_of_pure_ethanol = ml_of_pure_ethanol * 0.8

            gperday_user = gperday_user + g_of_pure_ethanol


        if gender == 1: #male
            gperday_optimal = 30

        elif gender == 2: #female
            gperday_optimal = 15

        if gperday_user <= gperday_optimal:
            string = "You are drinking the optimal amount of alcohol per day. Drinking less than " + str(gperday_optimal) + " grams of alcohol per day actually reduces the risk of of CVD by reverse cholesterol transport, haemostasis and insulin sensitivity mechanisms."

        else: string = "You are drinking way above the recommended alcohol limit per day. heavy alcohol consumption is an established risk factor for hypertension and the development and progression of cardiovascular diseases. Please stick to these limits: Male - less than 30g per day , Female - less than 15g per day."


    elif alcohol == 0: #Does not drink alcohol
        string = "It's great that you do not drink. Research has shown that those who drink one drink per day (4 oz. of wine, 12 oz. of beer, or 1-1/2 oz. of 80-proof spirits) may have less risk. However, the American Heart Association does not recommend that non-drinkers start using alcohol. For more information, you can visit: https://content.iospress.com/articles/nutrition-and-aging/nua0052"


    return string
