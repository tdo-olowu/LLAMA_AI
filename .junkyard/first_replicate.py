#!/usr/bin/python3

import replicate
output = replicate.run(
        "replicate/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
        input={"prompt": "Hello there, how are you today?"}
    )

# ['https://replicate.com/api/models/stability-ai/stable-diffusion/files/50fcac81-865d-499e-81ac-49de0cb79264/out-0.png']

for item in output:
    print(item, end="")
print("\n")
