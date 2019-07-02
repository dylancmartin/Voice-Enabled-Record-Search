# Voice-Enabled-License-Plate-Search

The goal for this program is to take as input phonetic letters, and return a
string that represents all of the spoken phoentic letters. The input will
consist of various words from the NATO Phonetic Alphabet, and so a string of
the form of a license place (7RLE903 for exampel) would be the expected output.

This process will be carried out through an Alexa Skill and a lambda function.
The Alexa Skill will be the front-end to the application, interacting with the
user and accepting their input. On the other hand, the lambda function will be
parsing and formatting a new response string to either give the license plate
string, or to respond with any errors that may occur.

**Decoding NATO/US Law Enforcement Phonetics**
This portion of the project is done in two parts: the Alexa Developer Portal,
and the Amazon Developer Console. The file from the former can be found within
the voice\_enabled\_license\_plate\_search.json file. I'll explain the intents
relevant to this Alexa Skill and how they were implemented:
- decodePhonetics:
The purpose for this intent is to take as input state and license plate
information (in the form of NATO/US Law Enforcement phonetics) and output
said information where the license plate is formatted as a string of numbers
and letters. In order to do so, the slot *license_plate* was established with
the **AMAZON.SearchQuery** Slot Type so that it could gather the entire phrase
of words detailing the license plate. Because Amazon does not allow for a
sample utterance to contain more than one slot when the **AMAZON.SearchQuery**
Slot Type is in use, the *state* slot is not included in the sample utterances.
Instead, it is set as required to fulfill the intent, and the user is prompted
for a response to answer the state following the input of the license plate
information. For more information on slot types and when/where to use them,
check out this [link](https://developer.amazon.com/docs/custom-skills/slot-type-reference.html).


