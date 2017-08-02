import urllib

def read_text():
    #(1)Read text
    quotes = open(r"C:\Users\smith526\OneDrive - BYU Office 365\Python\profanity_checker\text_check.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    #(2)Check for curse words
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This docuent is safe")
    else:
        print("Could not scan the document properly.")
        
read_text()
