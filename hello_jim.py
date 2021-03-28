def hello_jim(how_many):
    if how_many == 0:
        return("Jim.")
    else:
        output = "hello," + " " + hello_jim(how_many-1)
        print(output)
        return(output)
hello_jim(5)
