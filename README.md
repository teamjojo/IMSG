# IMSG
this is the email system for The NutBox                     Power off / trigger IMSG
we use it like this                                              ^
                                                                 |
Arduino --> Web-server(Mac mini) ---> error codes ---> arduino --|
                                                                 do nothing
the arduino sends the temprature, power and smoke levels to the mac mini
the mac mini says he the temprature is high and we have a lot of smoke trigger error codes 
those trigger IMSG/Brakes(all power off)
the arduino does the brakes and keeps sending all its info to the server
everybody gets emails saying the error code/why/info/and backup power(for the arduino) levels
thats how it works
