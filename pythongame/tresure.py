print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('Kamu berada di simpang jalan, kemana jalan yang akan kamu pilih "KIRI" or "KANAN"').lower()

if choice1 == "kiri":
    choice2 = input('Kamu sekarang tengah berada di tepi danau, apa yang akan kamu lakukan selanjutnya? "swim" or "wait"').lower()

    if choice2 == "wait":
        choice3 = input("setelah kamu berhasil melewati danau tersebut kamu menemukan 3 pintu, pintu mana yang kamu pilih? ").lower()
        if choice3  == "merah":
            print("setelah kamu masuk pintu merah, kamu terbakar oleh api GAME OVER!! ")
        elif choice3 == "kuning":
            print("pintu yang kamu pilih sangant tepat kamu mendapatkan harta karun, KAMU MENANG!!!")
        elif choice3 == "hijau":
            print("kamu dimakan oleh hewan buas, KAMU KALAH!!! GAME OVER!!!")
        else:
            print("tidak ada pintu yang kamu pilih")
    else:
        print("KAMU DIMAKAN HIDUP HIDUP OLEH SEGEROMBOLAN BUAYA!! GAME OVER")
else:
    print("KAMU JATUH KE JURANG , GAME OVER!!")



print("TERIMA KASIH TELAH BERMAIN GAME MENCARI HARTA KARUN SIMPLE ")

    
    
    