# Import needed modules.

import module5653project

import arcpy, os

# Set environments and overwrite.
#set overwrite true

arcpy.env.workwpace = "C:/data" # generic folder address
arcpy.env.overwriteOutput = True

# Start calling functions

# Make the flood zone layer.

module5653project.make_flood_zone_layer()

# Clip the hospital layer by the county layer.

module5653project.clip_hospital_layer()

# Get user input for task they want to perform.

task = module5653project.get_user_task()

# Get user input for building type they are interested in
#    (choice is libraries or hospitals)

buildings = module5653project.user_building()

# Perform user's task choice with their building choice.

if task == 'intersect':
    int_layer_name = module5653project.intersect_w_user_input(buildings)
    want_list = input("Do you want to print a list of the intersect? y or n: ")
    
    # print(buildings)  # This debugging code is left in place as comment because I need it.

    # I realize the following nested if/else statements should probably be in the
    #    "intersect" function in the module code, but I was having trouble getting
    #     them to work there with the correct building layer, so I left them here
    #     because it works.
    
    if want_list == "y":
        if buildings == "County_Hospitals":
            col_name = "NAME"
        else:
            if buildings == "COH_LIBRARIES":
                col_name = "LIBRARY"
        module5653project.print_fld_zn_buildings(int_layer_name,col_name)
elif task == 'clip':
    module5653project.clip_w_user_input(buildings)
else:
    if task == 'buffer':
        module5653project.buffer_w_user_input(buildings)

# Call function to print out a list of all files created by this code.
# Also, this makes another loop for my code so hopefully there are enough.

module5653project.gratuitous_for_loop_function()
        

