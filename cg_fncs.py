import random
locations = ["Frontal Chest","Top Skull"] #Location database for error checking


def selector_fn(location,ftrs, comp, level):
    # CREATES RANDOM SEQUENCE OF FEATURES FOR A SPECIFIC LOCATION
    #       location:   location of the injury
    #       ftrs:       features (i.e. diseases, incidental damage)
    #       comp:       compatibility mapper
    #       level:      level of difficulty (-> number of things to guess), ranges 1-5

    if location not in locations: #Error checking
        raise Exception("ERROR: The location was not in the database")
    if level>3:
        print("ERROR: The difficulty level was too high")
    
    min_level = 1
    N_features = random.randint(min_level,level) #N_features to sample
    N_features = N_features-(N_features>len(comp))*(N_features-len(comp))
    #Above line is just for robustness in case N_features > len(comp)

    out_ftrs = random.sample(list(ftrs[comp==1]), N_features) #
    return (location, out_ftrs)

def prompt_gen(location, features, s_bool):
    # if level > 1:
    severity = ["Mild ","Moderate ","Severe "]
    pn_severity = ["Small ","Medium ","Large "]
    feature_string = ""
    for f_n, f in enumerate(features):
        if f_n == len(features)-1 and len(features)!=1:
            connect = " and "
        elif len(features)==1:
            connect = "only " 
        elif f_n>0:
            connect = ", "
        else:
            connect = ""
        if s_bool and f=="Pulmonary Nodules":
            s_str = random.choice(pn_severity)
        elif s_bool:
            s_str = random.choice(severity)
        else:
            s_str = ""
        feature_string = feature_string+connect+s_str+f

    # else:
    #     feature_string = "only "+features

    if random.randint(1,2) >1:
        gender = "Male"
    else:
        gender = "Female"
    age = random.randint(18,80)

    out_prompt = str(age)+" Year Old "+gender+" "+location+" X-ray with "+feature_string
    
    return out_prompt


