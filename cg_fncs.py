import random

class Patient():
    def __init__(self, age, gender, primary, secondary, location, modality):
        self.age = str(age)
        self.gender = str(gender)
        self.primary = str(primary)
        self.secondary = secondary
        self.location = str(location)
        self.modality = str(modality)


def selector_fn(location,ftrs, comp, level):
    # CREATES RANDOM SEQUENCE OF FEATURES FOR A SPECIFIC LOCATION
    #       location:   location of the injury
    #       ftrs:       features (i.e. diseases, incidental damage)
    #       comp:       compatibility mapper
    #       level:      level of difficulty (-> number of things to guess), ranges 1-5

    locations = ["Frontal Chest","Top Skull"] #Location database for error checking
    if location not in locations: #Error checking
        raise Exception("ERROR: The location was not in the database")
    if level>3:
        print("ERROR: The difficulty level was too high")
    
    min_level = 1
    N_features = random.randint(min_level,level) #N_features to sample
    N_features = N_features-(N_features>len(comp))*(N_features-len(comp))
    #Above line is just for robustness in case N_features > len(comp)

    out_ftrs = random.sample(list(ftrs[comp==1]), N_features) #
    if len(out_ftrs)>1: 
        if out_ftrs[1] == "Healthy":
            out_ftrs[1] = []
    return (location, out_ftrs)


def prompt_gen(location, features, s_bool, modality):
    # if level > 1:
    severity = ["Mild ","Moderate ","Severe "]
    pn_severity = ["Small ","Medium ","Large "]
    feature_string = ""
    ftr_strings = []
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
        elif s_bool and f!="Healthy" and f!=[]:
            s_str = random.choice(severity)
        else:
            s_str = ""
        feature_string = feature_string+connect+s_str+str(f)
        ftr_strings.append(s_str+str(f))

    # else:
    #     feature_string = "only "+features

    if random.randint(1,2) >1:
        gender = "Male"
    else:
        gender = "Female"
    age = random.randint(18,80)

    out_prompt = str(age)+" Year Old "+gender+" "+location+" "+modality+" with "+feature_string
    if len(features) == 1:
        primary = ftr_strings[0]
        secondary = []
    else:
        primary = ftr_strings[0]
        if ftr_strings[1] != []:
            secondary = [ftr_strings[1]]
        else:
            secondary = ftr_strings[1]

    pat = Patient(age, gender, primary, secondary, location, modality)
    
    return out_prompt, pat
