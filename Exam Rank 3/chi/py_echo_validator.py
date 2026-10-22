#! /usr/bin/env python3

def echo_validator(text: str) -> bool:

    reverse_text = text[::-1]

    return text.replace(" ","").lower() == reverse_text.replace(" ", "").lower()



if __name__ == "__main__":
    print(f"True -> {echo_validator("racecar")}")
    print(f"True -> {echo_validator("A man a plan a canal Panama")}")
    print(f"False -> {echo_validator("race a car")}")
    print(f"True -> {echo_validator("Was it a car or a cat I saw")}")
