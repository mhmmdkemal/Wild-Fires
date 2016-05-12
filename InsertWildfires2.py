#Author: Mohammed Kemal
#Program: InsertWildfires 2
#Purpose: Create a new wilfire incidents point featureclass based on a text file

import arcpy
import sys
cur=None
try:
    arcpy.env.workspace=raw_input("Specify the WildlandFires.mdb with its full path:")#a worksapce from the user
    arcpy.env.overwriteOutput = True #overwrite envroment 
    file_name=raw_input("Specify the wildland fire file with full path:")#path to where the user will choose file
    Output_FILE = "Newfireinccident.shp"#this will be our output filename
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, Output_FILE, "POINT")#this will create points in the outputfile
    arcpy.AddField_management(Output_FILE, "CONFIVAL", "LONG", 6)#this lets add the confidence value in the shp file
    cur = arcpy.da.InsertCursor(Output_FILE, ["SHAPE@", "CONFIVAL"])#this inserts all the confidence values 
    f= open(file_name,'r')#this lets us read line by line 
    lstFires=f.readlines()#this places them in a vairable
    cntr=0# COunt counter
    for fire in lstFires:#a forloop in the list created earlier
        if 'Latitude' in fire:#if statement that checks lat
            continue#this allows us to continue
        pnt=arcpy.CreateObject("Point")#creates a point on the map
        lstValues=fire.split(",")#splits everything hen it sees a comma
        latitude=float(lstValues[0])#this is the first colum 
        longitude=float(lstValues[1])#the second column
        confid=int(lstValues[2])#the third column
        pnt.X=longitude#setting to the variables for the next line as well
        pnt.Y=latitude
        pnt.Z=confid
        print pnt.X, pnt.Y, pnt.Z#prins the things that were placed in it 
        cur.insertRow([pnt,confid])
        cntr +=1#adds and goes to the next
        print "Record number "+str(cntr)+" written to feature class"#this prints all the records
except Exception, e:#our exception
    print e
    print arcpy.GetMessages()

finally:#this deletes the cursor that was created 
    if cur:
        del cur


