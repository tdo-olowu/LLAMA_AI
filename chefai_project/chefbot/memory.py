#!/usr/bin/env python3

"""
MEMORY
    This keeps track of the conversation so far in the thread.
memory helps in somehow maintaining context.
It has only one job - track the history of prompts and responses, and incorporate recent prompts or responses into the history if validated.
I want to reduce dependencies as much as possible, but until then maybe...
I should just use LangChain to handle this.
"""

class Memory:
    pass
