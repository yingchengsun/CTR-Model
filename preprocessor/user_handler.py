import constants


def build_user_profile():
    # make user raw data
    user_profile_file = open(constants.dir_path + "userid_profile.txt")
    user_profile = [['0', '0']]
    for line in user_profile_file:
        fields = line.strip('\n').split('\t')
        user_profile.append([fields[1], fields[2]])
    print "Buliding user profile finished."
    return user_profile