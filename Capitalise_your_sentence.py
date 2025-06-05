a =input("Enter sentences with incorrect case: ")

sentences = a.split('.')

# Strip spaces and capitalize
capitalized_parts = [part.strip().capitalize() for part in sentences]

#  Rejoin with '. ' 
result = '. '.join(capitalized_parts)

if a.strip().endswith('.'):
    result += '.'

print(result)
