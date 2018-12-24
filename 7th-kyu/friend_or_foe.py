def friend(x):
    def filter_friend(friend):
        return len(friend) == 4
    
    return list(filter(filter_friend, x))