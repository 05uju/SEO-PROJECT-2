from apicall import *

date = response['forecast']['forecastday'][0]['date']
temp = response['forecast']['forecastday'][0]['day']['avgtemp_f']

if (temp < 30):
    print("Average temp:", temp)
    print("In" , offset , "days it's going to be below freezing! You should really wear some extra layers and bundle up with a coat and some gloves." )
elif(temp < 40):
    print("Average temp:", temp)
    print("In", offset ,"days it's going to be really really cold. I suggest you put on a thick coat with a sweater under it.")
elif(temp < 50):
    print("Average temp:", temp)
    print("In", offset ,"days it's going to be moderately cold. You should probably put on a long sleeve shirt or a sweater and a light jacket.")
elif(temp < 60):
    print("Average temp:", temp)
    print("In", offset, "days it's going to be cool. You could absolutely get away with wearing a sweater or a turtleneck but if you tend to get cold, you might want to bring a light jacket with you" )
elif(temp < 70):
    print("Average temp:", temp)
    print("In", offset, "days it will be not too cold and not too hot. Jeans and a short sleeve should be perfect.")
elif(temp < 80):
    print("Average temp:", temp)
    print("In", offset, "days it's going to be moderately warm. Wear something breathable and full-coverage like jeans and a short sleeve." )
elif(temp < 90):
    print("Average temp:", temp)
    print("In", offset, "days it's going to be very warm! You should wear some shorts and a short sleeve")
elif(temp < 100):
    print("Average temp:", temp)
    print("In", offset, "days it's going to be hot! Pull out your shorts and crop top and head to the beach!" )
else:
    print("Average temp:", temp)
    print("In", offset, "days it's going to be sweltering. Wear very light materials and make sure to stay in the shade!")












