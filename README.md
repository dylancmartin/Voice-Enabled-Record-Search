```                                                                                
Chase Peak                                                                         
Cal Poly Digital Transformation Hub                                                
```                                                                                

# Voice-Enabled-License-Plate-Search                                               

## Overview                                                                        

The goal for this program is to take as input numbers and words from a phonetic alphabet (ex. NATO phonetic alphabet), and return a string that represents the user's input as a license plate, or other official record. For example, the user may initiate a correspondence with Alexa by saying "run license plate alpha bravo charlie one two three", and the output would be ABC123.

This process will be carried out through an Alexa Skill and a lambda function.  The Alexa Skill will be the front-end to the application, interacting with the user and accepting their input. On the other hand, the lambda function will be parsing and formatting a new response string to either give the license plate string, or to respond with any errors that may have occurred, such as giving record information not based on the NATO/ US Law Enforcement Phonetic Alphabet..

**Decoding NATO/US Law Enforcement Phonetics**                                     

This portion of the project is done in two parts: the Alexa Developer Portal, and the Amazon Developer Console. The file from the former can be found within the voice\_enabled\_license\_plate\_search.json file. I'll explain the intents relevant to this Alexa Skill and how it was implemented:

- ParseLicensePlate/ParseId/ParseDriversLicense:
\
Three intents are being utilized in order to gather information based on the three basic record types that US Law Enforcement would need to identify. The process was carried about by establishing three individual intents for each of the types of record, and then merging each of them into a single method in the lambda function.                        
\
In the Alexa Developer Portal, each intent was made specific to a record type so that, in the creation of sample utterances, natural buffers would be put in between slots. In doing this, we can avoid a misinterpretation of the values we hope for each of the slots to grab. For example, creating the sample utterance "run {state} {record\_type} {record\_info}." offers no hard-coded words between slots that Alexa could use to distinguish information meant for each of the slots. Also, we avoid forming awkward-to-speak utterances by forcing cushions between slots like "run state {state} record type {record\_type} record information {record\_info}."
\
In the Amazaon Developer Console, a trigger needs to be set for Alexa Skills Kit with the skill id of the Alexa skill. With the given directory imported into the console, and role given to the lambda function (in this case, a dummy role can be provided since the function doesn't need to operate outside of it's current capacity). A single method is used to interact with the three defined intents, since they all serve the same relative purpose. The method parses and forms a string in letters and numbers. In order to prepare the information for extraction to 3rd party software, SSML, an XML-based markup language, is used to present the resulting information vocally while maintaining the data in the best format. For more information on SSML, [click here](https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html).
\
Lastly, the file *dictionaries.py* contains the python dictionaries for translating NATO phonetic/US Law Enforcement words to letters, and translating states to their respective abbreviations.

For any further questions, contact Chase Peak at **cpeak@calpoly.edu**.
