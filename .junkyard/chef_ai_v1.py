#!/usr/bin/python3
"""
c   command-line based Chef AI. Just chatbot with chef system prompt
First give structured output.
One precaution is harmful ingredients. We don't wanna teach users how to make poisons,
toxins, bombs, etc.

Don't forget if name main
"""

"""
-----------------------------------------------
IMPORTING NEEDED LIBRARIES
-----------------------------------------------
"""
import replicate
import sys

"""
-----------------------------------------------
Define general global variables and functions
to be used.
-----------------------------------------------
"""
# first, some error-handling.
argc = len(sys.argv)
if (argc < 1):
    print("No input received.")
    user_prompt = "I have crackers and a boiled egg. Give me a recipe."
else:
    user_prompt = str(sys.argv[1:])

model = "replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1"
temp = 0.3
sys_prompt = "You are a highly creative and resourceful chef "\
             "who can make an amazing meal out of even the most bare-bones "\
             "or inharmonious of ingredients. "\
             "You will help the user find at least one recipe in a sequence of friendly steps. "\
             "Give highly creative, slightly sarcastic names to each recipe."



# ----------------------------------------------
# will move these to their own file later.
def append_prompt(prev_prompt, new_prompt, user=False):
    user_tag_0 = "[INST]"
    user_tag_1 = "[/INST]"
    if (user):
        prev_prompt += f"\n{user_tag_0} {new_prompt} {user_tag_1}"
        return
    prev_prompt += f"\n{new_prompt}"
    return

# run the model until you explicitly ask to quit.
# type "Q" to quit.
def gameloop():
    pass


# user will also soon be capable of giving a prompt.
output = replicate.run(
          model,
          input = {"prompt": user_prompt,
                   "system_prompt": sys_prompt,
                   "temperature": temp
                   }
          )

response = str(output)
print(response)
