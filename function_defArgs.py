# Script to understand the functionality of the default arguments of the functions

def animals(name="snake", sound="hisses"):
        print(f"The {name} {sound}")


animals("cat", "meows")
animals("dog", "barks")
animals()
animals("monkey")