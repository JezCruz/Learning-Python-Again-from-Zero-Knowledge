# sample text file creator

with open("python-try/hello.txt", "w") as f:
    f.write("Hello Jez!")


# so the Output of this program
# Output:
# Open text file: hello.txt
# after you open the text file, you will see "Hello Jez!"

# so if you try to run again this python file again with new value it will replace all inside of it.
# example you change the f.write("Hello Jez!") to f.write("Good Morning!")
# he replace it from "Hello Jez!" to "Good Morning!"
# because you try to run "w" = (write) again.