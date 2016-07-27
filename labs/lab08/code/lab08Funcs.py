# lab08Funcs.py    Syllable Counting, for CS20, Spring 2016
# T. Pennebaker

def noConsecDups(theList):
    """
    noConsecDups is a function that takes a list of items or
    a string and returns a copy of that string list with no
    consecutive duplicates

    produces: the same list with any consecutive duplicates remove
    example: noConsecDups([2,3,3,3,4,4,5,6,6,2,2,1,5,3,3,2]
    produces: [2,3,4,5,6,2,1,5,3,2]

    if theList is not a string or list then return theList back unchanged
    """

    if (type(theList) not in [str,list]):
        return theList
    elif (len(theList)==0):
       return theList    # not [], because then it doesn't work on tuples or strings
    elif len(theList)==1:
       return theList
    # Now we know that the list has a least two elements.

    result = theList[0:1] # Initialize the result list containing the first item

    # Add items from theList to result if they're not consecutive duplicates
    for i in range(len(theList)):
        if theList[i] != result[-1]:
            result += theList[i:i+1]

    return result


def isVowel(letter):
   """
   isVowel checks whether a given letter is a vowel.  For purposes of this
   function, treat y as always a vowel, w never as a vowel.
   letter should be a string containing a single letter
   return "error" if the value of the parameter is not a single letter string,
   return True, if the letter is a vowel, otherwise False
   """

   if (type(letter) != str): # letter must be a string
       return "error"
   if (len(letter) != 1): # letter must only be a single character
       return "error"

    # return True if letter is a vowel (capital or lowercase)
   if (letter in ["a","e","i","o","u","y","A","E","I","O","U","Y"]):
       return True

   return False # otherwise return False


def countVowels(word):
   """
   parameter word should be a string
   produces:   an integer
   return boolean value False if the input is not a string,
   otherwise return number of vowels in word
   Note: the empty string is legal, and should produce the answer 0
   """

   if (type(word) != str):
       return False

   vowels = 0   # Initialize vowels as a counter at 0

   for letter in word: # Count the number of vowels in word using isVowel
       if isVowel(letter):
           vowels += 1

   return vowels # Return final count


def allVowelsA(word):
    """
     allVowelsA is a function that changes all vowels to 'a'.
       This function is a building block for a function that will count
       syllables by counting vowels.  For that purpose, all vowels are equivalent.
       But, we want to remove consecutive duplicate vowels.  Converting all
       vowels to the same vowel is a first step.
     word should be a string---otherwise return boolean value False
     when word is a string, return word with all vowels changed to the letter a
     examples:
       allVowelsA("by") produces "ba"
       allVowelsA("alien") produces "alaan"
       allVowelsA("boot") produces "baat"
       allVowelsA("fruition") produces "fraataan"
     Note: empty string is legal, and should return empty string
    """

    # This function is meant for strings, return False if word is not a string
    if (type(word) != str):
        return False

    result = "" # Initialize result as an empty string to add letters to

    # Add letters to result according to the contents of word
    for letter in word:
        if isVowel(letter):   # If letter is a vowel, substitute an 'a'
            result += 'a'
        else:               # If letter is not a vowel, leave it
            result += letter

    return result # Return the resulting string


def syllableHelper(word):
    """
    # syllableHelper is a function that is a building block for a function
    # that counts syllables.  It transforms a word by doing two things:
    #   (1) changing all vowels to the letter a
    #   (2) removing all consecutive duplicates
    # parameter word should be a string--if not return boolean value False
    # otherwise, return another string, with all vowels changed to the letter a,
    #     and consecutive duplicates removed
    # examples:
    #   syllableHelper("by") produces "ba"
    #   syllableHelper("alien") produces "alan"
    #   syllableHelper("boot") produces "bat"
    #   syllableHelper("fruition") produces "fratan"
    # Note: empty string is legal, and should return empty string
    """

    if (type(word) != str): # return False if word is not a string
        return False

    return noConsecDups(allVowelsA(word)) #Combine noConsecDups and allVowelsA


# removeSilentE is an example of a "heuristic".  A heuristic is an approach to
#   a problem that is not perfect, not guaranteed to succeed, but is still
#   useful.
# We want to remove silent e from the ends of words in English.  We'll use this approach:
#    (1) Let "howMany" be the number of 'a's in the word after it has been
#        processed by the syllableHelper function.
#    (2) If the original word now ends in 'e', and howMany is >= 2,
#        then, return the original word without the 'e' in place.
#    (3) Otherwise, return the word unchanged.
# These rules work for many words, such as "rule", "take", and "defenestrate"--we'll remove the silent
#  'e' from these words.  The rule also works for 'be', 'we', 'the', where the final e should
#  NOT be removed.  Some words where this rule fails are  "castle", "chronicle", "muscle"
#  The idea of a heuristic is that exceptions like these
#  are rare, so the rule is still pretty good.    Problem solving is often a matter of
#  starting with a "pretty good heuristic", and sucessively refining it.  (Can you think of an
#  improved rule that handles the words "castle", "chronicle" and "muscle" as well?)

def removeSilentE(word):
    """
    parameter "word" should be a string---otherwise return boolean value False
    returns word, but with silent e removed, according to the heuristic rules
      in the comment above.
    Note: the empty string is legal, and should produce the answer '' (empty string)
    """

    if (type(word) != str): # return False if word is not a string
        return False

    if (word == ""): # if word is an empty string, return an empty string
        return ""

    # count the vowels in the syllableHelpered version of word
    howMany = countVowels(syllableHelper(word))

    # Remove the 'e' remove the end of the word if probably not a syllable
    if ((word[-1] == 'e') or (word[-1] == 'E')) and howMany >= 2:
        return word[0:-1]
    else:
        return word


# removeEdWhenNotASyllable is another example of a "heuristic".
# In order to be able to count syllables, we want to
# remove ed from the ends of words in English such as "owned","phoned",
#   "rehearsed" and "goverened" when it doesn't add an extra syllable.
# We don't want to remove it from
#   words like "wed","cred", "bed", "tried"
# We'll use a similar approach to removeSilentE:
#    (1) Let "howMany" be the number of 'a's in the word after it has been
#        processed by the syllableHelper function.
#    (2) If the original word now ends in 'ed', and howMany is >= 2,
#        then, return the original word without the 'ed' in place.
#    (3) Otherwise, return the word unchanged.
# Words where this heuristic fails are "busted", "instituted", "embed"
# Can you think of an improvement to the heuristic that handles those cases?

def removeEdWhenNotASyllable(word):
    """
    word should be a string---otherwise return boolean value False
    if word is a string, return the same string, but with silent ed removed,
       according to the heuristic rules in the comment above.
    Note: the empty string is legal, and should produce the answer '' (empty string)
    """

    if (type(word) != str): # return False if word is not a string
        return False

    if (word == ""): # if word is an empty string, return an empty string
        return ""

    # count the vowels in the syllableHelpered version of word
    howMany = countVowels(syllableHelper(word))

    # Remove the 'ed' remove the end of the word if probably not a syllable
    if (word[-2:] in ['ed','eD','Ed','ED'] and howMany >= 2):
        return word[0:-2]
    else:
        return word


# countSyllables is a final example of a heuristic
# The theory is that the number of vowels in a word is a good indicator of the number of syllables
# in the word, if we (a) remove silent e, (b) remove final ed when it doesn't create a new syllable
# and (c) remove duplicate consecutive vowels in words like "boat", "patient", "pursuit" and "gaucho"
#
# This works for most words.   Convince yourself by trying it in your head on all the words in
# this sentence.  Then, try it on the first paragraph or two of the declaration of independence,
# found here:
#
# This heuristic does fail for some words.  Here are some examples:
#   "alien", "likely", "States".
#
# Here's our approach:   Write the code to do this.
#    (1) removeSilentE, removeEdWhenNotASyllable, and then all consecutive duplicate letters
#    (2) count the remaining vowels in the word that you get as a result of step 1 and return that.
#
#  Note that this approach also removes duplicate consonants, but we don't care, since we are only
#  counting vowels.  (If we changed our heuristic, that might change also).

def countSyllables(word):
     """
     word should be a string---otherwise, return False
     as long as word is a string, return an integer,
       our best guess at the number of syllables in word, using the heuristic above
     Note: the empty string is legal, and should produce the answer 0
     """

     if (type(word) != str): # return False if word is not a string
         return False

     # Combine removeSilentE, removeEdWhenNotASyllable, and syllableHelper to
     # count the number of values after each change
     return countVowels(syllableHelper(removeEdWhenNotASyllable(removeSilentE(word))))
