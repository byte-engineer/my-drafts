#PRINT ----------------------------------------------------------------

#|> We use print() to display text (string).
#|> It print new line(\n) in the end by defult.
#|> We can use print() also to write on files. (later on the course)

print("Hello! ")                                                       # Result => "Hello! "
print("Hello", "World")                                                # We can input many inputs at once.
print("Hi" * 3)                                                        # Rebeat it 3 times.
print("Hi ", end= "!!")                                                # Result => "Hi !!"
print("Hi", "my", "friend", sep= ", ")                                 # seprator by defult = " " |Result => "Hi, my, friend"
print("Force it", flush= True)                                         # To force the output to flushed it immediately.Try to do this commend if the function dosn't work

#