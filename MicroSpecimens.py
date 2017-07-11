stool = ["selenite","hektoen","mac","smac", "macconkey","sorbitol","campy","campylobacter","cin", "4c", "cin if age < 10"] #CIN if age < 10
sputum = ["bap","sba","choc","chocolate","mac","macconkey","gram", "gram stain","4c"]
ear = ["bap","sba","choc","chocolate","mac","macconkey","gram", "gram stain","4c"]
throat = ["bap anaerobic","sba anaerobic","4c"]
urine = ["bap", "sba", "mac", "macconkey", "cna", "cna only if turbid","4c"]
mro = ["mrsa", "mac cpd", "bea"] #All of these plates are unique to MRO screening
wound = ["bap","sba","mac","macconkey","gram","gram stain"]
soft_tissue = ["bap","sba","mac","macconkey","gram","gram stain"]
bite_wound = ["bap","sba","mac","macconkey","gram","gram stain","choc","chocolate"]
deep_wound = ["bap","sba","mac","macconkey","gram","gram stain","bap anaerobic", "sba anaerobic"]
below_waist = ["bap","sba","mac","macconkey","gram","gram stain","cna"]
csf = ["bap", "sba","choc","chocolate","gram","gram stain"]
sterile = ["thio", "thioglycollate","sba","bap","choc","mac","macconkey","gram","gram stain"]
eye = ["bap","sba","choc","chocolate","gram", "gram stain"]
vaginal = ["gram", "gram stain", "wet", "wet_prep"]
groupbscreen =  ["group b broth", "cna", "cna is a subculture from broth"]
cervical = ["chocolate","choc", "thayer martin", "tm"]
urethral = ["chocolate","choc","thayer martin", "tm","gram", "gram stain", "wet", "wet_prep"]
term_list = ["selenite","hektoen","mac","smac", "macconkey","sorbitol","campy","campylobacter","cin", "4c", "cin if age < 10","bap","sba","choc","chocolate","mac","macconkey","gram", "gram stain","4c","bap","sba","choc","chocolate","mac","macconkey","gram", "gram stain","4c","bap anaerobic","sba anaerobic","4c","bap", "sba", "mac", "macconkey", "cna", "cna only if turbid","mrsa", "mac cpd", "bea","bap","sba","mac","macconkey","gram","gram stain","bap anaerobic", "sba anaerobic","cna","thio", "thioglycollate","wet", "wet_prep","group b broth", "cna", "cna is a subculture from broth","thayer martin", "tm"]
specimen_list =[[stool],[sputum],[ear],[throat],[urine],[mro],[wound],[soft_tissue],[bite_wound],[deep_wound],[below_waist],[csf],[sterile],[eye],[vaginal],[groupbscreen],[cervical],[urethral]]


print("Welcome to the micro plate-o-bot 4000 main menu. What would you like to do?")
print("1-Specimen Search:Enter 1 to view a specimen type and see the plates required as well as further information")
print("2-Element Back Search:Enter 2 to search up a plate or characteristic")
print("3-Term List:Enter 3 to see a list of all the terms contained. I recommend this before using the element back search.")
menu_option= input("Enter your decision here: ")
menu_option2= int(menu_option)
menucounter = 0 #Loop for going back to menu if input is not available
if menu_option2 == 1:
    while menucounter < 1:
        print("Welcome. Enter the type of specimen you would like to search up. Please enter the type as designated in the following list")
        print("stool,sputum,ear,throat,urine,mro,wound,soft_tissue,bite_wound,deep_wound,below_waist,csf, sterile, eye. vaginal, groupbscreen,cervical,urethral ")
        specimen = input("Enter the type here: ")
        specimen = specimen.lower()
        if specimen == "stool":
            print (stool)
            menucounter = 2
        elif specimen == "sputum":
            print (sputum)
            menucounter = 2
        elif specimen == "ear":
            print (ear)
            menucounter = 2
        elif specimen == "throat":
            print (throat)
            menucounter = 2
        elif specimen == "urine":
            print(urine)
            menucounter = 2
        elif specimen =="mro":
            print(mro)
            menucounter = 2
        elif specimen =="wound":
            print(wound)
            menucounter = 2
        elif specimen =="soft_tissue":
            print(soft_tissue)
        elif specimen =="bite_wound":
            print(bite_wound)
            menucounter = 2
        elif specimen =="deep_wound":
            print(deep_wound)
            menucounter = 2
        elif specimen =="below_waist":
            print(below_waist)
            menucounter = 2
        elif specimen =="csf":
            print(csf)
            menucounter = 2
        elif specimen =="sterile":
            print(sterile)
            menucounter = 2
        elif specimen =="eye":
            print(eye)
            menucounter = 2
        elif specimen =="vaginal":
            print(vaginal)
            menucounter = 2
        elif specimen =="groupbscreen":
            print(groupbscreen)
            menucounter = 2
        elif specimen =="cervical":
            print(cervical)
            menucounter = 2
        elif specimen =="urethral":
            print(urethral)
            menucounter = 2
        else:
            print("That is not an acceptable specimen. Please try again using the provided list.")
elif menu_option2 == 2:
    print("Enter the type of plate or elements you would like to look up, note that the database only contains certain variations which are generally short forms and acronyms.")
    plate= input("Enter the desired plate or element here: ")
    plate= plate.lower()
    if plate in stool:
        print ("Element contained in stool processing")
    if plate in sputum:
        print ("Element contained in sputum processing")
    if plate in ear:
        print ("Element contained in ear processing")
    if plate in throat:
        print ("Element contained in throat processing")
    if plate in urine:
        print ("Element contained in urine processing")
    if plate in mro:
        print ("Element contained in stool processing")
    if plate in wound:
        print("Element contained in normal wound processing")
    if plate in soft_tissue:
        print ("Element contained in soft tissue processing")
    if plate in bite_wound:
        print ("Element contained in bite wound processing")
    if plate in deep_wound:
        print ("Element contained in deep wound processing")
    if plate in below_waist:
        print ("Element contained in below the waist wound processing")
    if plate in csf:
        print ("Element contained in csf processing")
    if plate in sterile:
        print ("Element contained in sterile site processing")
    if plate in eye:
        print ("Element contained in eye/conjunctivitis processing")
    if plate in vaginal:
        print ("Element contained in vaginal processing")
    if plate in groupbscreen:
        print ("Element contained in Group B Screening")
    if plate in cervical:
        print ("Element contained in cervical processing")
    if plate in urethral:
        print ("Element contained in urethral processing")
    if plate not in specimen_list:
        print ("Choice is not in list of terms. Please consult the following list")
        term_listdup =set(term_list)
        print (sorted(term_listdup))
elif menu_option2 == 3:
    term_listdup =set(term_list) #When making the term list I was too lazy to check for duplicates so this removes them.....
    print(sorted(term_listdup)) #alphabetical order for ease of use
    #Need to work out way to separate lists and sort individual terms alphabetically ratherh than sublists








