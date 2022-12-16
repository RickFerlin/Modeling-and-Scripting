import maya.cmds as cmds

list = ["Leg_##_Jnt", "Leg_##_Jnt", "Leg_##_Jnt", "Leg_##_Jnt", "Leg_##_Jnt", "Leg_##_Jnt", "Leg_##_Jnt", "Leg_##_Jnt",
        "Leg_##_Jnt", "Leg_##_Jnt", "Leg_##_Jnt"]

def seqrenamer(list):
    number_of_zeros = 0
    argument_num = 1
    hashtag = "#"

    for argument in list:
        for hashtag in argument:
            number_of_zeros += 1
        newarg = argument.replace("#", "0", number_of_zeros)
        newarg = newarg.replace("0", "", len(str(argument_num)))
        underscore = newarg.find("_", newarg.find("_") + 1)
        print(newarg[:underscore] + str(argument_num) + newarg[underscore:])
        argument_num += 1

seqrenamer(list)