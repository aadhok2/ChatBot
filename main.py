import re
from collections import defaultdict
import random

dst = {'location':'','movie':'','day':'','time':'','no_people':'','full_name':''}
#print("here",dst)

# nlu(input): Interprets a natural language input and identifies relevant slots and their values
# Input: A string of text.
# Returns: A list ([]) of (slot, value) pairs.  Slots should be strings; values can be whatever is most
#          appropriate for the corresponding slot.  If no slot values are extracted, the function should
#          return an empty list.
def nlu(input=""):
    # [YOUR CODE HERE]
    
    # Dummy code for sample output (delete or comment out when writing your code!):
    slots_and_values = []
    
    # To narrow the set of expected slots, you may (optionally) first want to determine the user's intent,
    # based on what the chatbot said most recently.
    user_intent = ""
    
    
    if "dsh" in dst:
        if dst["dsh"][0] == "Theatre_location":
            pattern = re.compile(r"\b([Cc]hicago)|([Nn]aperville)|([Aa]urora)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_location"
                #dst["dsh"].append("Movie_selection")
                slots_and_values.append(("uih", "respond_location"))
                slots_and_values.append(("dsh", "Movie_selection"))
            else:
                print("im here")
                user_intent = "unknown"
                slots_and_values.append(("uih", "unknown"))
            
        elif dst["dsh"][0] == "Movie_selection":
            # Check to see if the input contains a valid size.
            pattern = re.compile(r"\b([Ww]atch)|([Mm]ovie)|([Tt]enet)|([Ii]nterstellar)|([Ll]ion)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_movie"
                #dst["dsh"].append("Movie_day")
                slots_and_values.append(("uih", "respond_movie"))
                slots_and_values.append(("dsh", "Movie_day"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("uih", "unknown"))
        elif dst["dsh"][0] == "Movie_day":
            # Check to see if the input contains a valid size.
            pattern = re.compile(r"\b([Ss]unday)|([Mm]onday)|([Tt]uesday)|([Ww]ednesday)|([Tt]hursday)|([Ff]riday)|([Ss]aturday)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_day"
                #dst["dsh"].append("Show_time")
                slots_and_values.append(("uih", "respond_day"))
                slots_and_values.append(("dsh", "Show_time"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("uih", "unknown"))
        elif dst["dsh"][0] == "Show_time":
            # Check to see if the input contains a valid size.
            pattern = re.compile(r"\b([Mm]orning)|([Mm]atinee)|([Ff]irst)|([Ss]econd)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_show"
                #dst["dsh"].append("People")
                slots_and_values.append(("uih", "respond_show"))
                slots_and_values.append(("dsh", "People"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("uih", "unknown"))
        elif dst["dsh"][0] == "People":
            # Check to see if the input contains a valid size.
            pattern = re.compile(r"\b(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|([Oo]ne)|([Tt]wo)|([Tt]hree)|([Ff]our)|([Ff]ive)|([Ss]ix)|([Ss]even)|([Ee]ight)|([Nn]ine)|([Tt]en)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_people"
                #dst["dsh"].append("User_fullname")
                slots_and_values.append(("uih", "respond_people"))
                slots_and_values.append(("dsh", "User_fullname"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("uih", "unknown"))
        elif dst["dsh"][0] == "User_fullname":
            # Check to see if the input contains a valid size.
            pattern = re.compile(r"\b(name)|([Mm]ax)|([Aa]ndrew)|([Kk]arl)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_name" 
                slots_and_values.append(("uih", "respond_name"))
                slots_and_values.append(("dsh", "Tickets_booked"))
                
            else:
                user_intent = "unknown"
                slots_and_values.append(("uih", "unknown"))
        elif dst["dsh"][0] == "Tickets_booked":
           
            user_intent = "greeting"
            dst.pop("dsh")
            dst.pop("uih")
            dst["location"]=''
            dst["movie"]=''
            dst["day"]=''
            dst["time"]=''
            dst["no_people"]=''
            dst["full_name"]=''
#             else:
#                 user_intent = "unknown"
#                 slots_and_values.append(("uih", "unknown"))
    # If you're maintaining a dialogue state history but there's nothing there yet, this is probably the
    # first input of the conversation!
    else:
        user_intent = "greeting"
        slots_and_values.append(("uih", ["greeting"]))
        slots_and_values.append(("dsh", ["Theatre_location"]))
    
        
    # Then, based on what type of user intent you think the user had, you can determine which slot values
    # to try to extract.
    if user_intent == "respond_location":
        
        # In our sample chatbot, there's only one slot value we'd want to extract if we thought the user
        # was responding with a pizza size.
        pattern = re.compile(r"\b[Cc]hicago\b")
        contains_chi = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Nn]aperville\b")
        contains_nap = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Aa]urora\b")
        contains_sch = re.search(pattern, input)
        
        # Note that this if/else block wouldn't work perfectly if the input contained, e.g., both "small"
        # and "medium" ... ;)
        if contains_chi:
            slots_and_values.append(("location", "Chicago"))
        elif contains_nap:
            slots_and_values.append(("location", "Naperville"))
        elif contains_sch:
            slots_and_values.append(("location", "Aurora"))
        
    if user_intent == "respond_movie":
        
        # In our sample chatbot, there's only one slot value we'd want to extract if we thought the user
        # was responding with a pizza size.
        pattern = re.compile(r"\b[Tt]enet\b")
        contains_tenet = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ii]nterstellar\b")
        contains_is = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ll]ion\b")
        contains_lion = re.search(pattern, input)
        
        # Note that this if/else block wouldn't work perfectly if the input contained, e.g., both "small"
        # and "medium" ... ;)
        if contains_tenet:
            slots_and_values.append(("movie", "Tenet"))
        elif contains_is:
            slots_and_values.append(("movie", "Interstellar"))
        elif contains_lion:
            slots_and_values.append(("movie", "Lion"))
    if user_intent == "respond_day":
        
        # In our sample chatbot, there's only one slot value we'd want to extract if we thought the user
        # was responding with a pizza size.
        pattern = re.compile(r"\b[Ss]unday\b")
        contains_sun = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Mm]onday\b")
        contains_mon = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Tt]uesday\b")
        contains_tue = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ww]ednesday\b")
        contains_wed = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Tt]hursday\b")
        contains_thu = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ff]riday\b")
        contains_fri = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ss]aturday\b")
        contains_sat = re.search(pattern, input)
        
        # Note that this if/else block wouldn't work perfectly if the input contained, e.g., both "small"
        # and "medium" ... ;)
        if contains_sun:
            slots_and_values.append(("day", "Sunday"))
        elif contains_mon:
            slots_and_values.append(("day", "Monday"))
        elif contains_tue:
            slots_and_values.append(("day", "Tuesday"))
        elif contains_wed:
            slots_and_values.append(("day", "Wednesday"))
        elif contains_thu:
            slots_and_values.append(("day", "Thursday"))
        elif contains_fri:
            slots_and_values.append(("day", "Friday"))
        elif contains_sat:
            slots_and_values.append(("day", "Saturday"))
    if user_intent == "respond_show":
        
        # In our sample chatbot, there's only one slot value we'd want to extract if we thought the user
        # was responding with a pizza size.
        pattern = re.compile(r"\b[Mm]orning\b")
        contains_mor = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Mm]atinee\b")
        contains_mat = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ff]irst\b")
        contains_fir = re.search(pattern, input)
        
        pattern = re.compile(r"\b[Ss]econd\b")
        contains_sec = re.search(pattern, input)
        

        
        # Note that this if/else block wouldn't work perfectly if the input contained, e.g., both "small"
        # and "medium" ... ;)
        if contains_mor:
            slots_and_values.append(("time", "Morning"))
        elif contains_mat:
            slots_and_values.append(("time", "Matinee"))
        elif contains_fir:
            slots_and_values.append(("time", "First"))
        elif contains_sec:
            slots_and_values.append(("time", "Second"))

    if user_intent == "respond_people":
        
        # In our sample chatbot, there's only one slot value we'd want to extract if we thought the user
        # was responding with a pizza size.
        pattern = re.compile(r"\b(1)|([Oo]ne)\b")
        contains_1 = re.search(pattern, input)
        
        pattern = re.compile(r"\b(2)|([Tt]wo)\b")
        contains_2 = re.search(pattern, input)
        
        pattern = re.compile(r"\b(3)|([Tt]hree)\b")
        contains_3 = re.search(pattern, input)
        
        pattern = re.compile(r"\b(4)|([Ff]our)\b")
        contains_4 = re.search(pattern, input)
        
        pattern = re.compile(r"\b(5)|([Ff]ive)\b")
        contains_5 = re.search(pattern, input)  
                                    
        pattern = re.compile(r"\b(6)|([Ss]ix)\b")
        contains_6 = re.search(pattern, input)
        pattern = re.compile(r"\b(7)|([Ss]even)\b")
        contains_7 = re.search(pattern, input)
        pattern = re.compile(r"\b(8)|([Ee]ight)\b")
        contains_8 = re.search(pattern, input)
        pattern = re.compile(r"\b(9)|([Nn]ine)\b")
        contains_9 = re.search(pattern, input)
        pattern = re.compile(r"\b(10)|([Tt]en)\b")
        contains_10 = re.search(pattern, input)
        
        
        # Note that this if/else block wouldn't work perfectly if the input contained, e.g., both "small"
        # and "medium" ... ;)
        if contains_1:
            slots_and_values.append(("no_people", "1"))
        elif contains_2:
            slots_and_values.append(("no_people", "2"))
        elif contains_3:
            slots_and_values.append(("no_people", "3"))
        elif contains_4:
            slots_and_values.append(("no_people", "4"))
        elif contains_5:
            slots_and_values.append(("no_people", "5"))
        elif contains_6:
            slots_and_values.append(("no_people", "6"))
        elif contains_7:
            slots_and_values.append(("no_people", "7"))
        elif contains_8:
            slots_and_values.append(("no_people", "8")) 
        elif contains_9:
            slots_and_values.append(("no_people", "9"))
        elif contains_10:
            slots_and_values.append(("no_people", "10"))
        
    if user_intent == "respond_name":
        
        # In our sample chatbot, there's only one slot value we'd want to extract if we thought the user
        # was responding with a pizza size.
        pattern = re.compile(r"\b([Mm]ax)\b")
        contains_max = re.search(pattern, input)
        
        pattern = re.compile(r"\b(2)|([Aa]ndrew)\b")
        contains_andrew = re.search(pattern, input)
        
        pattern = re.compile(r"\b(3)|([Kk]arl)\b")
        contains_karl = re.search(pattern, input)
        

        
        
        # Note that this if/else block wouldn't work perfectly if the input contained, e.g., both "small"
        # and "medium" ... ;)
        if contains_max:
            slots_and_values.append(("full_name", "Max"))
        elif contains_andrew:
            slots_and_values.append(("full_name", "Andrew"))
        elif contains_karl:
            slots_and_values.append(("full_name", "Karl"))
        
    return slots_and_values


# update_dst(input): Updates the dialogue state tracker
# Input: A list ([]) of (slot, value) pairs.  Slots should be strings; values can be whatever is
#        most appropriate for the corresponding slot.  Defaults to an empty list.
# Returns: Nothing
def update_dst(input=[]):
	# [YOUR CODE HERE]
 
    # Dummy code for sample output:
    global dst
    for slot, value in input:
        if slot in dst and isinstance(dst[slot], list):
            dst[slot].insert(0, value)
        else:
            dst[slot] = value
    return

# get_dst(slot): Retrieves the stored value for the specified slot, or the full dialogue state at the
#                current time if no argument is provided.
# Input: A string value corresponding to a slot name.
# Returns: A dictionary representation of the full dialogue state (if no slot name is provided), or the
#          value corresponding to the specified slot.
def get_dst(slot=""):
    # [YOUR CODE HERE]
    
    # Dummy code for sample output (delete or comment out when writing your code!):
    dummy_state = defaultdict(list)
    if len(slot)==0:
        dummy_state = dst
        return dummy_state
    else:
        if slot in dst:
            if dst.get(slot) != '':
                dummy_state = dst[slot]
                return dummy_state
            else:
                dummy_state = ''
                return dummy_state


# dialogue_policy(dst): Selects the next dialogue state to be uttered by the chatbot.
# Input: A dictionary representation of a full dialogue state.
# Returns: A string value corresponding to a dialogue state, and a list of (slot, value) pairs necessary
#          for generating an utterance for that dialogue state (or an empty list if no (slot, value) pairs
#          are needed).
def dialogue_policy(dst=[]):
    # [YOUR CODE HERE]
    next_state = None
    slot_values = None
    #print("here",dst)
    
    if get_dst("location") != '':
        next_state  = "Movie_selection"
        if get_dst("movie") != '':
            next_state = "Movie_day"
            slot_values = [("movie",get_dst("movie"))]
            if get_dst("day") != '':
                next_state = "Show_time"
                if get_dst("time") != '':
                    next_state = "People"
                    if get_dst("no_people") != '':
                        next_state = "User_fullname"
                        if get_dst("full_name") != '':
                            next_state = "Tickets_booked"
                            slot_values = [("full_name",get_dst("full_name")),("no_people",get_dst("no_people"))]
                        elif get_dst("full_name") == '':
                            next_state = "User_fullname"
                    elif get_dst("no_people") == '':
                        next_state = "People"
                elif get_dst("time") == '':
                    next_state = "Show_time"
            elif get_dst("day") == '':
                next_state = "Movie_day"
        elif get_dst("movie") == '':
            next_state = "Movie_selection"
    elif get_dst("location") == '':
        next_state = "Theatre_location"

    # Dummy code for sample output (delete or comment out when writing your code!):

    return next_state, slot_values

# nlg(state, slots=[]): Generates a surface realization for the specified dialogue act.
# Input: A string indicating a valid state, and optionally a list of (slot, value) tuples.
# Returns: A string representing a sentence generated for the specified state, optionally
#          including the specified slot values if they are needed by the template.
def nlg(state, slots=[]):
    # [YOUR CODE HERE]
    
    # Dummy code for sample output (delete or comment out when writing your code!):
    template = defaultdict(list)
    
    if state == "Theatre_location":
        template["Theatre_location"]=[]
        template["Theatre_location"].append("Hi, I am AMB ChatBot\nPlease select the theater location to get started\nLocations are:\n1. Chicago\n2. Naperville\n3. Aurora")
        template["Theatre_location"].append("Welcome Back, I am AMB ChatBot\nPlease select the theater location to get started\nLocations are:\n1. Chicago\n2. Naperville\n3. Aurora")
    
    if state == "Movie_selection":
        template["Movie_selection"]=[]
        template["Movie_selection"].append("Thanks, How can I help you?\nTodays showings Tenet,Lion,Interstellar ")
        template["Movie_selection"].append("Great, Which movie do you want to watch?\nTodays showings Tenet,Lion,Interstellar")
    
    
    if state == "Movie_day":
        template["Movie_day"]=[]
        if slots != []:
            template["Movie_day"].append("Sure, when do you want to watch " + slots[0][1] + " ?(Please enter the day ex:'Monday')")
            template["Movie_day"].append("When do you want to watch " + slots[0][1] + " ?(Please enter the day ex:'Monday')")
    
    if state == "Show_time":
        template["Show_time"]=[]
        template["Show_time"].append("Great, at what time do you like to watch?(Please enter the show name\nShows are:\n1.Morning\n2. Matinee\n3. First\n4. Second)")
        template["Show_time"].append("Thanks, which time slot is better for you?(Please enter the show name\nShows are:\n1.Morning\n2. Matinee\n3. First\n4. Second)")
    
    
    if state == "People":
        template["People"]=[]
        template["People"].append("Great, How many tickets do you need?")
        template["People"].append("How many are planning to watch?")
    
    
    if state == "User_fullname":
        template["User_fullname"]=[]
        template["User_fullname"].append("Almost Done, please tell me your full name(Please select the name from Max,Andrew,Karl)")
        template["User_fullname"].append("Please tell me your full name(Please select the name from Max,Andrew,Karl)")
    
    
    if state == "Tickets_booked":
        template["Tickets_booked"]=[]
        if slots != []:
            if int(slots[1][1]) > 1:
                template["Tickets_booked"].append("Congrats " + str(slots[0][1]) + " ! Your tickets are booked")
            elif int(slots[1][1])==1:
                template["Tickets_booked"].append("Congrats " + str(slots[0][1]) + " ! Your ticket has been booked")
            if int(slots[1][1]) > 1:
                template["Tickets_booked"].append("Nice " + str(slots[0][1]) + " ! Your tickets are booked")
            elif int(slots[1][1])==1:
                template["Tickets_booked"].append("Nice " + str(slots[0][1]) + " ! Your ticket has been booked")
    

    
    # Build at least two templates for each dialogue state that your chatbot might use.
    """templates["greetings"] = []
    templates["greetings"].append("Hi, welcome to 421Pizza!  What would you like to order?")
    
    templates["clarification"] = []
    templates["clarification"].append("Just double-checking ...did you say that you want <num_pizzas> pizzas?")"""
    
    # When you implement this for real, you'll need to randomly select one of the templates for
    # the specified state, rather than always selecting template 0.  You probably also will not
    # want to rely on hardcoded input slot positions (e.g., slots[0][1]).  Optionally, you might
    # want to include logic that handles a/an and singular/plural terms, to make your chatbot's
    # output more natural (e.g., avoiding "did you say you want 1 pizzas?").
    """output = ""
    if len(slots) > 0:
        output = templates[state][0].replace("<num_pizzas>", str(slots[0][1]))
    else:
        output = templates[state][0]"""
    #print("here",template)
    num = random.randint(0,1)
    return template[state][num]
    
# Use this main function to test your code when running it from a terminal
# Sample code is provided to assist with the assignment, feel free to change/remove it if you want
# You can run the code from terminal as: python3 chatbot.py

def main():
    global dst
    
   
    
    # Test Cases
    
    iput = nlu("")
    #print("here",dst)
    update_dst(iput)
    current_state_tracker = get_dst()
    next_state, slot_values = dialogue_policy(current_state_tracker)
    output = nlg(next_state, slot_values)
    print("\nOutput: {0}\n".format(output))
    
    # The above test case is worked because there is no dsh item in dst it means there is no history so it is printing "Greetings"
    while next_state!="Tickets_booked":
        #print("chicago")
        i = input()
        iput = nlu(i)
        #print("here",dst)
        update_dst(iput)
        current_state_tracker = get_dst()
        next_state, slot_values = dialogue_policy(current_state_tracker)
        output = nlg(next_state, slot_values)
        print("\nOutput: {0}\n".format(output))

################ Do not make any changes below this line ################
if __name__ == '__main__':
    main()
