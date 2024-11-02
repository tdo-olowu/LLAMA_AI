#!/usr/bin/env python3

"""
ERROR HANDLER MODEL
    This handles errors related to the model's input-output pipeline.
It deals with invalid input, inability to reason properly (e.g. due to network connectivity or token-related issues, or being too broke to purchase more tokens, or finding no suitable model for the request, etc.
It also handles invalid output - offensive output, irrelevant output, etc.
Should inherit from some generic ErrorHandler class
"""

class ErrorHandler_Model:
    pass
