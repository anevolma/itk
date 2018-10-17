# #Ülesanne 1

# def list_sum(list):
    # """this function takes an integer and returns sum of 1+2+...+N"""
    
    # result = 0   
    # for item in range(len(list)):
        # result = result + list[item]
    # return(result)

# print(list_sum([3, 5, 1]))
# # Väga hea, tubli töö ;)

# #Ülesanne 2

# def liblikas(string):
    # string = string.lower()
    # tekst = string.split()
    # for item in range(len(tekst)-1, 0, -1):  #alusta listi viimasest elemendist! kolmene range  -1 tagurpidi üks
        # if tekst[item].startswith('a'):
            # tekst[item] = 'liblikas'
            # return(tekst)
            # break
    
# print(liblikas("Kui Arno isaga koolimajja jõudis, olid tunnid juba alanud"))
# # Väga hea, tubli töö ;)


# #Ülesanne 3
        
def common_symbols(string, string1):
    result = 0
    result1 = 0
    list = []
	# 
    for i in range(len(string)):
        if string[i] == string1[i]:
            result = result + 1
    result = str(result)
    
	#nested for kahe stringi võrdlus
    for i in range(len(string)):
        for j in range(len(string1)):
            if string[i] == string1[j]:
                if string[i] in list:
                    continue
                else:
                    list.append(string[i])
    result1 = str(len(list))
    vastus = result + "," + result1
    print(vastus)

	
common_symbols("TAOA", "TUBA")
# Väga hea, tubli töö ;)      
print("Tere!")