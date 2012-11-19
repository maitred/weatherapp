import  pywapi, string
imperial = False #Defaults to metric. Please don't change this. It would make me sad.
while True:
    try:
        line = input()
        print('looking up the weather for '+ str(line))
        
        if imperial:
            y_weather = pywapi.get_weather_from_yahoo( line , units = 'imperial')
            print ('It is '+ str.lower(y_weather['condition']['text']) + " and " + y_weather['condition']['temp'] + 'F now.')
        else:
            y_weather = pywapi.get_weather_from_yahoo( line , units = 'metric')
            print ('It is '+ str.lower(y_weather['condition']['text']) + " and " + y_weather['condition']['temp'] + 'C now.')
   
    except:
            print('There was a problem with your request. Please try again. Make sure this is a US ZIP code.')
    