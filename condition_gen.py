import random
import numpy as np

from cg_fncs import selector_fn as sel
from cg_fncs import prompt_gen

def condition_gen():
    locations = ["Frontal Chest"] # PUT LOCATIONS HERE, SEPARATED BY COMMA
    L_loc = len(locations)
    modality = "X-Ray"
    features = np.array(["Healthy","Pneumonia","Pleural Effusion","Tuberculosis","Rib Cage Fracture","Pulmonary Nodules","Pneumothorax","Cardiomegaly"]) 
    severity = ["Mild","Moderate","Severe"]
    pn_severity = ["Small","Medium","Large"]
    severity_bool = True
    # PUT ALL FEATURES FOR ALL LOCATIONS ON ARRAY ABOVE
    L_ftr = len(features)
    if L_loc ==1:
        comp = np.ones((L_ftr,)) #If there is only one location, all conditions
        #should be compatible with that location
    else:
        comp = np.ones((L_ftr,L_loc)) #In this section the compatibility matrix
        #needs to be manually populated
        comp[:,0] = 1
        comp[-1,0] = 0
        comp[:,1] = 0
        comp[-1,1] = 1

    loc_idx = random.choice(range(L_loc)) #Chooses a random location for x-ray
    loc = locations[loc_idx]

    if L_loc>1: #Retrieves the compatibility vector of the chosen location
        curr_comp = comp[:,loc_idx]
    else:
        curr_comp = comp
    level = 2 #should read from front end in practice

    out_loc, out_ftrs = sel(loc,features, curr_comp, level) #function that selects
    #the features for a specific location

    out_prompt, pat = prompt_gen(out_loc, out_ftrs, severity_bool, modality) #Generates a prompt, level here
    # print(pat.age + " | " + pat.gender + " | " + pat.primary + " | " + str(pat.secondary) + " | " + pat.location + " | " + pat.modality)
    return out_prompt, pat


