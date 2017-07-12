"""
Provides recommended agar plates by type of micro specimen. Can also search up plates/elements to see which specimen site uses them.
Next version will be using a dict containing list of strings for the specimen e.g(mac and smac for ear. This version is very poorly optimized
"""
stool = ["selenite", "hektoen", "mac", "smac", "macconkey", "sorbitol", "campy", "campylobacter", "cin", "4c", "cin if age < 10"] #CIN if age < 10
sputum = ["blood","bap", "sba", "choc", "chocolate", "mac", "macconkey", "gram", "gram stain", "4c","blood and choc in CO2"]
ear = ["blood","bap", "sba", "choc", "chocolate", "mac", "macconkey", "gram", "gram stain", "4c","blood and choc in CO2"]
throat = ["bap anaerobic", "sba anaerobic", "4c"]
urine = ["blood","bap", "sba", "mac", "macconkey", "cna", "cna only if turbid", "4c"]
mro = ["mrsa", "mac cpd", "bea"] #All of these plates are unique to MRO screening
wound = ["blood","bap", "sba", "mac", "macconkey", "gram", "gram stain","bap anaerobic", "sba anaerobic","blood in CO2"]
soft_tissue = ["blood","bap", "sba", "mac", "macconkey", "gram", "gram stain","bap anaerobic", "sba anaerobic","blood in CO2"]
bite_wound = ["blood","bap", "sba", "mac", "macconkey", "gram", "gram stain", "choc", "chocolate","blood in CO2"]
deep_wound = ["blood","bap", "sba", "mac", "macconkey", "gram", "gram stain", "bap anaerobic", "sba anaerobic","blood in CO2"]
below_waist = ["blood","bap", "sba", "mac", "macconkey", "gram", "gram stain", "cna","blood in CO2"]
csf = ["blood","bap", "sba", "choc", "chocolate", "gram", "gram stain","blood in CO2"]
sterile = ["thio", "thioglycollate", "sba", "bap", "choc", "mac", "macconkey", "gram", "gram stain"]
eye = ["blood""bap", "sba", "choc", "chocolate", "gram", "gram stain","blood in CO2"]
vaginal = ["gram" , "gram stain", "wet", "wet_prep"]
groupbscreen = ["group b broth", "cna", "cna is a subculture from broth"]
cervical = ["chocolate", "choc", "thayer martin", "tm"]
urethral = ["chocolate", "choc", "thayer martin", "tm", "gram", "gram stain", "wet", "wet_prep"]
term_list = ["selenite", "hektoen", "mac", "smac", "macconkey", "sorbitol", "campy", "campylobacter", "cin", "4c", "cin if age < 10", "bap", "sba", "choc", "chocolate", "mac", "macconkey", "gram", "gram stain", "4c", "bap", "sba", "choc", "chocolate", "mac", "macconkey", "gram", "gram stain", "4c", "bap anaerobic", "sba anaerobic", "4c", "bap", "sba", "mac", "macconkey", "cna", "cna only if turbid", "mrsa", "mac cpd", "bea", "bap", "sba", "mac", "macconkey", "gram", "gram stain", "bap anaerobic", "sba anaerobic", "cna", "thio", "thioglycollate", "wet", "wet_prep", "group b broth", "cna", "cna is a subculture from broth", "thayer martin", "tm","blood and choc in CO2","blood in CO2","blood"]
specimen_list = [[stool], [sputum], [ear], [throat], [urine], [mro], [wound], [soft_tissue], [bite_wound], [deep_wound], [below_waist], [csf], [sterile], [eye], [vaginal], [groupbscreen], [cervical], [urethral]]
specimen_string=["stool","sputum","ear","throat","urine","mro","wound","soft_tissue","bite_wound","deep_wound","below_waist","csf", "sterile", "eye","vaginal", "groupbscreen","cervical","urethral"]
#Add a loop that will keep the program going as long as the user does not enter "exit"
menu_option = 0
while menu_option != "exit":
    print("Welcome to the micro plate-o-bot 4000 main menu. What would you like to do?")
    print("1-Specimen Search:Enter 1 to view a specimen type and see the plates required as well as further information")
    print("2-Element Back Search:Enter 2 to search up a plate or characteristic")
    print("3-Term List:Enter 3 to see a list of all the terms contained. I recommend this before using the element back search.")
    print("Enter exit once you are done to close the program.")
    menu_option = input("Enter your decision here: ")
    jcounter= 0
    if menu_option == "1":
        while jcounter != 1:
            print("Welcome. Enter the type of specimen you would like to search up. Please enter the type as designated in the following list without the ' ")
            print(specimen_string)
            specimen = input("Enter the type here: ")
            specimen = specimen.lower()
            if specimen in specimen_string:
                locationspecimen= (specimen_string.index(specimen))
                print(specimen_list[locationspecimen])
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                jcounter = 1  #Prevents looping here if a good answer is given
            else:
                print("That is not an acceptable specimen. Please try again using the provided list.")

    elif menu_option == "2":
        print("Enter the type of plate or elements you would like to look up, note that the database only contains certain variations which are generally short forms and acronyms.")
        plate = input("Enter the desired plate or element here: ") #Should look for a way to optimize this to a single if. Working on it..
        plate = plate.lower()
        if plate in stool:
            print("Element contained in stool processing")
        if plate in sputum:
            print("Element contained in sputum processing")
        if plate in ear:
            print("Element contained in ear processing")
        if plate in throat:
            print("Element contained in throat processing")
        if plate in urine:
            print("Element contained in urine processing")
        if plate in mro:
            print("Element contained in stool processing")
        if plate in wound:
            print("Element contained in normal wound processing")
        if plate in soft_tissue:
            print("Element contained in soft tissue processing")
        if plate in bite_wound:
            print("Element contained in bite wound processing")
        if plate in deep_wound:
            print("Element contained in deep wound processing")
        if plate in below_waist:
            print("Element contained in below the waist wound processing")
        if plate in csf:
            print("Element contained in csf processing")
        if plate in sterile:
            print("Element contained in sterile site processing")
        if plate in eye:
            print("Element contained in eye/conjunctivitis processing")
        if plate in vaginal:
            print("Element contained in vaginal processing")
        if plate in groupbscreen:
            print("Element contained in Group B Screening")
        if plate in cervical:
            print("Element contained in cervical processing")
        if plate in urethral:
            print("Element contained in urethral processing")
        if plate in term_list: #Prevents screen from being too cluttered
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if plate not in term_list:
            print("Choice is not in list of terms. Please consult the following list")
            term_listdup = set(term_list)
            print(sorted(term_listdup))
    elif menu_option == "3":
        term_listdup = set(term_list) #When making the term list I was too lazy to check for duplicates so this removes them.....
        print(sorted(term_listdup)) #alphabetical order for ease of use
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
