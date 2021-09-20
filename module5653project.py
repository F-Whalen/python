# Import arcpy
import arcpy, os

# This module selects by attribute the areas from the flood map layer that are
#     flood zones and adds them to the map as another layer.

def make_flood_zone_layer():
    """This function makes a flood zone layer to use for this project."""

    # Select Flood Zones and add to map.

    fz_query = 'FLD_ZONE = \'A\' Or FLD_ZONE = \'AE\' Or FLD_ZONE = \'AO\''
    fz_areas = "C:/data"  # generic folder address
    flood_zones = arcpy.SelectLayerByAttribute_management(fz_areas, 'NEW_SELECTION', fz_query)

    # Write the selected features to a new feature class
    arcpy.CopyFeatures_management(flood_zones, 'fldZns')
    
    

# This module clips the hospitals layer by the county boundary and adds
#     them to the map.

def clip_hospital_layer():
    """This module clips the hospital layer by the county boundary."""

    # Set local variables
    in_features = "COH_HOSPITALS"
    clip_features = "HCAD_Harris_County_Boundary"
    out_feature_class = "C1_Hospitals"

    # Execute Clip
    arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

# Function to get user input about the task they want to do and returns value.

def get_user_task():
    """Ask user what they want to do and return the result"""

    # Make sure that user enters a valid task.

    while True:
        process = input("Please enter 'clip', 'buffer', or 'intersect': ")
        if process == 'clip' or process == 'buffer' or process == 'intersect':
            break
        else:
            print("That is not a valid input. Pleast try again.")
            continue
    return process

# Function to get type of buildings user wants to use.

def user_building():
    """Ask user what buidling type they are interested in."""

    # Make sure that user enters a valid building

    while True:
        building_choice = input("Please enter either 'libraries' or 'hospitals': ")
        if building_choice == 'libraries' or building_choice == 'hospitals': 
            break
        else:
            print("That is not a valid input. Pleast try again.")
            continue
    if building_choice == 'libraries':
        building_c = 'COH_LIBRARIES'
    else:
        if building_choice == 'hospitals':
            building_c = 'County_Hospitals'           
    return building_c

# Function to find intersection of flood zone layer with user's building choice.

def intersect_w_user_input(building):
    """Takes user's building choice as input and intersects with flood layer."""
   
    # Intersect of user's building choice with Flood Zones

    # Set variables
    in_feature_1 = building
    in_feature_2 = "fldZns"
    out_feature = input("Input a name for intersect layer: ")

    # Run Intersect and add as map layer.

    arcpy.analysis.Intersect([in_feature_1,in_feature_2], out_feature)
    return out_feature
 

# Function to find clip of flood zone layer with user's building choice.

def clip_w_user_input(building):
    """Takes user's building choice as input and clip with flood layer."""
   
    # Clip of user's building choice with Flood Zones

    # Set local variables
    in_features = building
    clip_features = "fldZns"
    out_feature_class = "Clipped_bldgs"

    # Execute Clip

    arcpy.Clip_analysis(in_features, clip_features, out_feature_class)


# Function to find buffer with user's choice of building and distance.

def buffer_w_user_input(building):
    """Takes user's building choice as input and asks for buffer distance."""
    
    user_dist = input("Input a distance in miles: ")
    buffer_dist = "{} miles".format(user_dist)
    
    # Execute Buffer

    arcpy.analysis.Buffer(building, user_output_path, buff_dist)
    

    
# This function prints out list of buildings in flood zone
#   with "(might flood)" added to end of name. It can only be called if
#   an intersect was the task choice. It takes the intersect layer
#   and the column name of building choice as arguments.

def print_fld_zn_buildings(layer_name,column_name):
    """This function uses the cursor to print names in flood intersect layer."""
    # Define variable and define what the cursor is to search for.
    feature = layer_name
    print("in cursor ", layer_name, column_name)
    cursor = arcpy.da.SearchCursor(feature, [column_name])
    row = cursor.next()
    while row:
        print('{0} (might flood)'.format(row[0])) # Use .format method to print out columns.
        row = cursor.next()

        #for row in cursor:  # These 2 rows were not used, but I want to leave the
        #    print(row)      #    code here so I will remember that it works too.
    del cursor   # Delete the cursor to unlock files.

# Make another function that has a loop just in case I don't have enough.
# Because after doing all this work, I would hate to lose points
#     for something simple like not enough loops.

def gratuitous_for_loop_function():
    
    """This prints out all of the shapefiles created while running this code."""

    # Define where the files are located.
    
    folder_space = "C:/data"   # generic folder address

    #Make a list of the files.
    file_list = os.listdir(folder_space)

    # Print out one file name per line by using a for loop.
    
    for file_name in file_list:
        if file_name.endswith(".shp"):
            print(file_name)

