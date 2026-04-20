# here lets try to change the "w" = write to "a" = append

with open("python-try/hello.txt", "a") as f:
    f.write("\nHey Wasup!")

# so if you remember on try1.py we used the "w" = write
# but rightnow we use "a" = append, append is to add test on a existing text file.
# example we use the hello.txt file that inside of it has "Hello Jez!"
# then if we run the try2.py the Output will becomes
# Hello Jez!
# Good morning, Jez!

# so yah the question is why the Output is in new line? it's because we use a "\n" to print it in new line.

# and additionally if we run it again the Output will print it again in new line.

# for example, if we run it again the output will become
# Hello Jez!
# Good morning, Jez!
# Good morning, Jez!

# then if we try to chage the f.write("\nGood morning, Jez!") to f.write("\nHey Wasup!") then run
# the Output will become
# Hello Jez!
# Good morning, Jez!
# Good morning, Jez!
# Hey Wasup!

# that is the use of "a" or append.