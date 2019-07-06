# Voice-Enabled-License-Plate-Search

## Overview

The goal for this program is to take as input numbers and words from a phonetic
alphabet (ex. NATO phonetic alphabet), and return a string that represents the
user's input as a license plate. For example, the user may initiate a
correspondence with Alexa by saying "run license plate alpha bravo charlie one
two three", and the output would be ABC123 (in the form of a license plate.)

This process will be carried out through an Alexa Skill and a lambda function.
The Alexa Skill will be the front-end to the application, interacting with the
user and accepting their input. On the other hand, the lambda function will be
parsing and formatting a new response string to either give the license plate
string, or to respond with any errors that may have occurred.

**Decoding NATO/US Law Enforcement Phonetics**

This portion of the project is done in two parts: the Alexa Developer Portal,
and the Amazon Developer Console. The file from the former can be found within
the voice\_enabled\_license\_plate\_search.json file (to be added at a later date).
I'll explain the intent relevant to this Alexa Skill and how it was implemented:

- decodePhonetics:
The purpose for this intent is to take as input the state and license plate
information (in the form of NATO/US Law Enforcement phonetics) and output
said information where the license plate is formatted as a string of numbers
and letters. In order to do so, the slot *license_plate* was established with
the *AMAZON.SearchQuery* Slot Type so that it could gather the entire phrase
of words detailing the license plate. Because Amazon does not allow for a
sample utterance to contain more than one slot when the *AMAZON.SearchQuery*
slot type is in use, the *state* slot is not included in the sample utterances.
Instead, it is set as required to fulfill the intent, and the user is prompted
for a response to provide the related state following the input of the license
plate information. For more information on slot types and when/where to use them,
check out this [link](https://developer.amazon.com/docs/custom-skills/slot-type-reference.html).

Lastly, the portion related to the Amazon Developer Console can be found within
the file lambda\_function.py under the method *decode_phonetics(intent_slots)*.
The argument that it takes contains the necessary information on the state
and license plate that the user identified. For a general overview of the
method, it takes advantage of a dictionary containing all possible connections
between key words and their respective letters in order to translate the license
plate. In doing so, it forms the returned string variable containing the
decoded license plate and its related state.
