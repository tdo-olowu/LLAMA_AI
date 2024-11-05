#!/usr/bin/env python3

"""
CHEFAI PROTOTYPE
    Purely procedural, no persistence, minimal error-handling.
    Simple input validation
"""

import replicate
import os
# for say_hello(), say_goodbye(), valid(u_prompt), 
from chefai_functions import *

#llama_2_model = "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1"
replicate.api_key  = os.getenv('REPLICATE_API_TOKEN')

long_prompt = ""

say_hello()
active = True

# initialize configuration data
prompt_symbol = "> "
system_message = "You are a friendly professional chef who can make "
system_message += "delicious meals out of almost any edible ingredient."
model = "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1"
system_temp = 0.3 # this can be updated dynamically in a full application.

# input loop
while active:
    user_input = input(prompt_symbol)
    if (valid(user_input)):
        if (user_input.lower().strip() == "quit"):
            active = False
        else:
            # always make sure to append a newline at the end, for neatness
            long_prompt += ("[INST]" + user_input + "[\INST]\n")
            try:
                error = False
                response = replicate.run(
                              model,
                              input={"prompt": long_prompt,
                                     "system_prompt": system_message,
                                     "temperature": system_temp
                                     }
                            )
                print("Testing...:")
                print(response)
                # in the proper app, raise exception if response taking too long
            except Exception as e:
                error = True
                print("Mama mia, I cut my finger!")
            if (not error):
                # give response to user
                print(response)
                long_prompt += (response + "\n")
    else:
        print("Invalid input!")

say_goodbye()
