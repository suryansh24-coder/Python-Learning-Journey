letter = ''' 
Dear <|NAME|>,\n You are selected! \n Congratulations!\n You have been selected for the position of <|POSITION|> at our company.\n We are excited to have you on board and look forward to working with you. \n Please let us know if you have any questions or need any further information. \n Best regards, \n HR Team'''

name =input ("Enter the name of the candidate: ")
position = input ("Enter the position for which the candidate is selected: ")
letter =letter.replace("<|NAME|>", name)
letter = letter.replace("<|POSITION|>", position)
print(letter)