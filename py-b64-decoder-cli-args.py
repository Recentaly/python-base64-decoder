import base64 as b64
import sys
import re
import os

try:

    code = sys.argv[1]

except IndexError:  print("\nNo Command line argument found!\n");   code="WW91IGRpZG4ndCBnaXZlIGEgY29tbWFuZCBsaW5lIGFyZ3VtZW50IHNvIEkgZ2F2ZSB5b3UgdGhpcyBpbnN0ZWFkIQ==" # We do a bit of trolling, I suppose

def decode(code):

    try:

        # Below we try to remove the letter b that for some reason appears every time you decode to a string.
        # The third line below also makes sure the String is pure and there are no ' ' around our string

        output = str(b64.b64decode(code))
        output = output.replace("b","",1)
        output = re.sub(r'^\s*(\'\s*)?|(\s*\')?\s*$', '', output)

        if os.path.isfile("output.txt"):    # Check if our output file exists

            print("\nOutput file was found!\n")

        else:   open("output.txt",'a').close(); print("\nCreating new output file...\n")    # If it doesn't, we use this trick to make a new dummy output file

        with open("output.txt",'w') as output_file:

            output_file.write(output)
            print("\nProgram finished!\n")
            output_file.close()

    except b64.binascii.Error:    print("\nPlease enter a valid Base64 String\n")

decode(code)
