This is the code used to respond to my text messages in Twilio.  It takes commands of the form:
[command] [sub-command] [args]
Some of the commands don't need alternate sub-commands and args with everything separated by spaces.
Here is a list of the commands with their corresponding sub-commands:
    wifi
        no sub-commands, this simply responds with my wifi password
    random
        order + [args]
            This takes all of the args and responds with the args in a random order
        choice + [args]
            This takes all of the args and responds with a random choice of one of the [args]
        sp
            This responds with a random South Park episode that is on Hulu right now
        sunny
            This responds with a random It's Always Sunny episode that is on Netflix right now
        [any number]
            This responds with a random integer between 0 and the number input number, even if it is negative