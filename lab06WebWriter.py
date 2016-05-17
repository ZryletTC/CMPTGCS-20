# lab06WebWriter.py by Tyler Pennebaker for CS20 lab06,  5/16/16
# Takes weather data from a file and formats in an HTML file

import os  # This allows access to operating system features

def webDirectory():
    """
    returns a string containing the folder associated with
    web directory http://www.cs.ucsb.edu/~yourusername/cs20/lab06
    """
    
    # Get the home directory

    myHome = os.getenv("HOME")
    if (type(myHome)!=str):
        
       # raise Exception is a way to force Python to vomit
       # if we've run into a situation we don't know how to handle
       raise Exception("Can't get home directory")

    return myHome + "/public_html/cs20/lab06"


def webAddress():
    """
    returns the URL (complete with the correct username) for
    http://www.cs.ucsb.edu/~yourusername/cs20/lab06
    """
    
    # Get the home directory

    myUsername = os.getenv("USER")
    if (type(myUsername)!=str):
        
       # raise Exception is a way to force Python to vomit
       # if we've run into a situation we don't know how to handle
       raise Exception("Can't get home directory")

    return "http://www.cs.ucsb.edu/~" + myUsername + "/cs20/lab06"


def makeWebDirectoryIfItDoesNotExistAlready():
    """
    Create the directory ~/public_html/cs20/lab06 unless it already
    exists.
    """
    # This code checks to see if the web directory
    # ~/public_html/cs20/lab06 already exists
    # If so,we just return---there is nothing to do!
    
    if (os.access(webDirectory(),os.F_OK)):
        return

    # If not, then create a web directory for this lab (cs20/lab06)
    # The 0o755 is the Python way or writing octal number 755 (rwxr-xr-x)

    else:
        os.makedirs(webDirectory(),0o755)

    # If you run this on CSIL, now you should be able to navigate to
    # http://www.cs.ucsb.edu/~yourusername/cs20/lab06 and see files


def startWebPage(myTitle):
    """
    Returns a string with the head element for a web page
    with title myTitle.
    
    Example: webPageHeader("Temperatures") returns the
    header for a web page with temperatures on it, i.e.
    <head>
      <title>Temperatures</title>
    </head>
    """

    return ("<html>\n<head>\n" +
      " <title>"+ myTitle + "</title>\n" + 
      "</head>\n<body>\n<h1>"+myTitle+"</h1>\n")
    

def makeWeatherWebPage(inputFileName,outputFileName):
    """
    Takes the data from inputFileName and converts it into
    an HTML file whose name is specified by outputFileName
    which can be written to the web.
    """

    # Open the input file
    weatherFile = open(inputFileName,"Ur")

    # Open the output file
    makeWebDirectoryIfItDoesNotExistAlready()
    htmlFileName = webDirectory() + "/" + outputFileName
    htmlFile = open(htmlFileName,"w")

    # Write the start of the HTML file
    htmlFile.write(startWebPage("SB Weather"))
    htmlFile.write("<table border='1'>\n")

    # Write the table header
    htmlFile.write("<tr><th>Date</th>"+
                   "<th>Precip (in)</th>"+
                   "<th>High</th>"+
                   "<th>Low</th>"+
                   "<th>Wind Dir</th>"+
                   "<th>Wind Speed</th>"+
                   "<th>Rel Humid max</th>"+
                   "<th>Rel Humid min</th></tr>")

    
    # process every line in the file---and for each one
    # write a line to the html for the web page
    for line in weatherFile:

        # Convert this line into a list
        lineAsList = line.split(",")

        # Write each item in the line to the table
        htmlFile.write("<tr>")
        for item in lineAsList:
            htmlFile.write("<td>"+item+"</td>")
        htmlFile.write("</tr>")

    htmlFile.write("</table>\n</body>\n</html>\n")

    # close the intput file and the output file
    weatherFile.close()
    htmlFile.close()

    # Tell the user where to find the page
    print("Look for the web page at this URL:\n")
    print(" " + webAddress() + "/" + outputFileName)

    print("Or if working on a PC or Mac, at this one:\n")
    print(" file://" + htmlFileName)
