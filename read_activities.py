import pandas as pd

df = pd.read_csv("ac_activities.csv")


for index in range(len(df.index)):
    type = df.loc[index, "Activity_Type"]
    if not(type == "Run"):
        continue
    id = df.loc[index, "Activity ID"]
    activity_date = df.loc[index, "Activity_Date"]
    distance = df.loc[index, "Distance"]
    grade_adj_distance = df.loc[index, "Grade_Adjusted_Distance"]
    moving_time = df.loc[index, "Moving_Time"]
    elapsed_time = df.loc[index, "Elapsed_Time"]
    total_elevation_gain = round(df.loc[index, "Elevation_Gain"], 4)
    elev_high = round(df.loc[index, "Elevation_High"], 4)
    elev_low = round(df.loc[index, "Elevation_Low"], 4)
    avg_heartrate = round(df.loc[index, "Average_Heart_Rate"], 2)
    avg_cadence = df.loc[index, "Average_Cadence"]
    if (not pd.isna(avg_cadence)):
        avg_cadence = round(avg_cadence * 2)
    gear_id = df.loc[index, "Gear"]
    if (not pd.isna(gear_id)):
        gear_id = round(gear_id)
    print(f"Values: ({id}, {activity_date}, {type}, {distance}, {grade_adj_distance}, {moving_time}, {elapsed_time}, {total_elevation_gain}, {elev_high}, {elev_low}, {avg_heartrate}, {avg_cadence}, {gear_id});")
    # parameters =
    # Here i want to call a method from connect_activities.py to this row of parameters
    # This should be possible from here only by passing the parameters
    # this means i should create a method/class that will have the db_config set, and perhaps
    # insert sql statement set

    # i can maybe have have a method/class that takes which type of sql statement is trying to be executed
    # and pass the parameters along with it
    # however right now i'm only trying to insert so maybe focus on that