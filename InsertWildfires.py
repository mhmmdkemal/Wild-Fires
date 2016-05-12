#Author: Mohammed Kemal
#Program: InsertWildfires.py
#Purpose: To add coordinate data from a table to the Wildfire shapefile.

import arcpy #import arcpy

cur=None #the cursor as a counter 

try:
    arcpy.env.workspace=raw_input("Specify the WildlandFires.mdb with its full path:")#a worksapce from the user 
    file_name=raw_input("Specify the wildland fire file with full path:")#file name that is inputted by the user placed in a variable
    f= open(file_name,'r')# this allows us to open the file 
    lstFires=f.readlines()#this lets us read line by line 
    cur=arcpy.da.InsertCursor("FireIncidents",["SHAPE@","CONFIDENCEVALUE"])#this lets us insert a new cursor containg a function
    cntr=1 # COunt counter 
    for fire in lstFires:#a forloop in the list created earlier 
        if 'Latitude' in fire:#if statement that checks lat 
            continue #this allows us to continue
        pnt=arcpy.CreateObject("Point")#creates a point on the map
        lstValues=fire.split(",")#splits everything hen it sees a comma
        latitude=float(lstValues[0])#this is the first colum 
        longitude=float(lstValues[1])#the second column
        confid=int(lstValues[2])#the third column
        pnt.X=longitude#setting to the variables for the next line as well
        pnt.Y=latitude
        print pnt.X, pnt.Y #prins the things that were placed in it 
        cur.insertRow([pnt,confid])#
        print "Record number"+str(cntr)+"written to feature class"#this prints all the records
except Exception, e:#our exception
    print e
    print arcpy.GetMessages()

finally:#this deletes the cursor that was created 
    if cur:
        del cur


