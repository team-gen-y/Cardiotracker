import csv
def clear():
    with open('flaskapp/user_data.csv', 'r+') as csvfile:
        csvfile.readline()
        csvfile.truncate(csvfile.tell())
# with open('flaskapp/user_data.csv','a',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['age','gender','height','weight','bmi','ap_lo','ap_hi','pulse','num_smoke','num_alco','activ_time','date'])