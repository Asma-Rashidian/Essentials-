""" Source Link :
                    https://pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/
"""

import argparse 

# Instantiate the argument.parser as ap 
ap = argparse.ArgumentParser()

# We must specify both shorthand "-n" and longhand version "--name" where either the flag could be used in command line 
ap.add_argument("-n" , "--name" , required=True , help="name of the user")

# Call vars on object to return parssed argument line into a Python Dictionary where the key is the name of command line argument 
# and the value is the input 
args = vars(ap.parse_args())


print (args)

# To access command line argument we use it like adictionary named args >>> args["name"]
print("Hi there {} , Nice to meet you !!".format(args["name"]))