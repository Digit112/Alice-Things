def starts_with(text, prefix):
	for i in range(len(prefix)):
#		print(text[i] + " != " + prefix[i])
		if text[i] != prefix[i]:
#			print("Not the same!")
			return False
	
#	print("The same!")
	return True

prefixes = {
	"Visa": ["4"],
	"MasterCard": map(str, range(51, 56)),
	"Diners Club": ["36", "38"],
	"Discover": ["6011", "65"],
	"Japan Credit Bureau": ["35"],
	"American Express": ["34", "37"]
}

def determine_issuer(num):
	for issuer in prefixes:
		prefix_list = prefixes[issuer]
		
		for prefix in prefix_list:
#			print(issuer + " has prefix " + prefix)
			if starts_with(num, prefix):
				return issuer
	
	return "Unknown"

def luhn(num):
	num = num[::-1]
	sum = 0
	for i in range(len(num)):
		if i % 2 == 0:
			doubled_val = int(num[i]) * 2
			if doubled_val > 9:
				doubled_val -= 9
			
			sum += doubled_val
			
		else:
			sum += int(num[i])
	
	return (10 - (sum % 10)) % 10

num = input("Card Number: ")

print(luhn(num))
print(determine_issuer(num))
