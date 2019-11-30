
import re, pyperclip


# TODO: create a regex for phone numbers
message = "Rick Jenkins, Associate Director for501-371-206-6501-682-6399URick.Jenkins@adhe.eduUPlanning and AccountabilitySharon Butler501-371-2069501-682-6399USharon.Butler@adhe.eduUProgram SpecialistNO CHILD LEFT BEHIND  PhoneFaxE-  Mail Dr. Suzanne Mitchell501-371-2062501-682-6399USusanne.Mitchell@adhe.eduUNo Child Left Behind Coordinator3"
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall(message))


# TODO create a regex for email addresses

emailRegex = re.compile(r'\w+@\w+.\w\w\w')
print(emailRegex.findall(message))




# TODO get the text off the clipboard




# TODO extract the email/phone from this text



# TODO copy the extracted email/phone to the clipboard 