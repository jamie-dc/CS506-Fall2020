def draw_firestation(trucks=1):
    if trucks < 0:
      print("Uh oh, you can't have negative trucks!")
      return
    extra_trucks = trucks-1
    print("      ________    ")
    print("     /        \   ")
    print("    /          \  ")
    print("   /            \ ")
    print("  /______________\ ")
    print("  |              | ")
    print("  | Volunteer    | ")
    print("  | Fire         | ")
    print("  | Department   | ")
    if trucks == 0:
      print("  |              | ")
      print("  |              | ") 
      print("  |              | ") 
      print("  |              | ") 
      print("  |              | ")
      print("  |              | ") 
      print("  |______________| ") 
    else:
        print("  |              |"+ extra_trucks*"______________")
        print("  |              " + extra_trucks*"              " + "| ")
        print("  |   _n____n_   " + extra_trucks*"   _n____n_   " + "| ")
        print("  |   |______|   " + extra_trucks*"   |______|   " + "| ")
        print("  |   |      |   " + extra_trucks*"   |      |   " + "| ")
        print("  |   |      |   " + extra_trucks*"   |      |   " + "| ")
        print("  |   |_|__|_|   " + extra_trucks*"   |_|__|_|   " + "| ")
        print("  |____U____U____" + extra_trucks*"____U____U____" + "| ")
    return
