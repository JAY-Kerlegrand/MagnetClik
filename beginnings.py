
#Here's a small intro for the game, haha
import time
import random
intro = ["Magnet High School is a prestigious STEM school focused on the discipline of engineering.\n",
"Hundreds of students compete vigorously in the selective admission process to be enrolled in the school and further their education in hopes of becoming productive members of society in their near futures.\n",
"Except...\n",
"Once in the school, some of these once restful, dutiful students...\n",
"if ever dutiful at all...\n",
"become stress-induced, procrastinating balls of sadness.\n",
"Congrats! You are one of these pitiful students, and you are trying to skirt by yet another week of homework.\n",
"Try to get your work done while also maintaining your energy and happiness!\n\n"]
#for line in intro:
    #print(line, end="")
    #time.sleep(2)
#print("-----------------")

#each character has different stats of base energy, work done per click, and base happiness; the base for all these traits, respectively, is 50, 5, 50
class Magneteer:

    def __init__(self, name, energy, work, happiness):
        self.name = name
        self.energy = energy
        self.work = work
        self.happiness = happiness

    def stats(self):
        global WORK
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        #note: Unicode used to bold the numbers
        if WORK > 150:
            WORK = 150
        if ENERGY < 0:
            ENERGY = 0
        if HAPPINESS < 0:
            HAPPINESS = 0
        if NUM_CLICKS < 0:
            NUM_CLICKS = 0
        print(f"""
        You have:
        \033[1m{WORK}\033[0m  work done out of 150
        \033[1m{ENERGY}\033[0m energy left
        \033[1m{HAPPINESS}\033[0m happiness
        \033[1m{NUM_CLICKS}\033[0m clicks left""")
        print("\n")
        #if work/happiness/num_clicks low, give a warning

    def working(self):
        global WORK
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        print("You do some work.\n")
        WORK += self.work
        ENERGY -= 3
        HAPPINESS -= 2
        NUM_CLICKS -= 1

    def eat(self):
        global ENERGY
        global NUM_CLICKS
        eating = ["Mother made some porridge, how nice.", "Crackers and cheese replenish your soul.", "Let's take a break for some grapes.", "You eat a cinnamon bun. It's sweet, just like you <3.", "Mmmm, sesame candy...", "You...drink some water? That's it? Ok..."]
        print("You eat something.", end=" ")
        print(random.choice(eating))
        ENERGY += 2
        NUM_CLICKS -= 1

    def sleep(self):
        global NUM_CLICKS
        global ENERGY
        print("You catch a few winks. But at what cost? You lost some clicks to do your work!")
        ENERGY += 4
        NUM_CLICKS -= random.randint(3,5)

    def procrastinate(self):
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        pro = ["You take a break to browse Twitter. You laugh at another stupid Trump tweet.", "You doodle on the edge of your pa- wait, no, you just finished a fully colored illustration...", "WAIT, IS THERE A NEW EPISODE OF *insert fave show*!!??-", "You literally just sit there and stare at your paper, trying to empty your mind of stress. It kinda works, but not really.", "You really just wanna play Smash Ultimate, so you do. Isabelle's sweet smile makes it all worth it."]
        print("You procrastinate.", end=" ")
        print(random.choice(pro))
        ENERGY -= 2
        HAPPINESS += 1
        NUM_CLICKS -= 1

    def cry(self):
        """The cry function has a 50/50 chance of either increasing or decreasing your HAPPINESS"""
        global HAPPINESS
        global NUM_CLICKS
        p = [1, 2]
        pp = random.choice(p)
        if pp == 1:
            print("You get a bit overwhelmed and some tears come a-flowing. But that's understandable, it can get stressful sometimes. You feel a bit better afterward.\n")
            HAPPINESS += 3
        else:
            print("A simple problem and a brain fart manage to hurl you into a fury of tears. You feel worse now. Oh no.\n")
            HAPPINESS -= 3
        NUM_CLICKS -= 1

characters = {
    "owl": Magneteer("Night Owl", 70, 6, 50),
    "genius": Magneteer("MIT Genius", 50, 8, 40),
    "studious": Magneteer("Studious Student", 40, 7, 70)}

#print("What type of Magneteer are you? \n")
#time.sleep(2)
#I have used Unicode to bold certain words
print(f"★★ The \033[1m Night Owl \033[0m can stay up to do more work, but they work more slowly. They start off with {characters['owl'].energy} ENERGY and {characters['owl'].happiness} HAPPINESS, and get {characters['owl'].work} WORK done per click.\n")
#time.sleep(2)
print(f"★★ The \033[1m MIT Genius \033[0m can work quickly, but they tend to procratinate more. They start off with {characters['genius'].energy} ENERGY and {characters['genius'].happiness} HAPPINESS, and get {characters['genius'].work} WORK done per click.\n")
#time.sleep(2)
print(f"★★ The \033[1m Studious Student \033[0m has less energy, but doesn't need to procrastinate as much. They start off with {characters['studious'].energy} ENERGY and {characters['studious'].happiness} HAPPINESS, and get {characters['studious'].work} WORK done per click.\n")
#time.sleep(2)

char = input("So, how do you work? (owl)(genius)(studious)\n")

print(f"\nNice! So you're the {characters[char].name} type, huh?\n")
time.sleep(2)

NUM_CLICKS = 50
WORK = 0
ENERGY = characters[char].energy
HAPPINESS = characters[char].happiness

#These are quick directions
directions = ["Directions:", "Press (e) to eat", "Press (s) to sleep", "Press (p) to procrastinate", "Press (c) to... cry", "Be careful, sleeping and crying may have some consequences...", "Stragetize! You've only got __ clicks to get it done, so use 'em wisely!"]
#for line in directions:
    #print(line)
    #time.sleep(1)
#print("\n")

while WORK < 150:
    if NUM_CLICKS <= 0:
        print("Fiddlesticks! You ran out of clicks to do your work!\n\n...")
        break
    if ENERGY <= 0:
        print("Aw, rats, your energy... I- I think you passed out from exhaustion, dude.\n\n")
        break
    if HAPPINESS <=0:
        print("You let your happiness deplete, and you broke down in tears from the mounting stress on your shoulders...I think you need a break...")
        break
    action = input("What do you want to do?\n")
    if action == "w":
        characters[char].working()
        characters[char].stats()
    elif action == "e":
        characters[char].eat()
        characters[char].stats()
    elif action == "s":
        characters[char].sleep()
        characters[char].stats()
    elif action == "p":
        characters[char].procrastinate()
        characters[char].stats()
    elif action == "c":
        characters[char].cry()
        characters[char].stats()

if WORK == 150:
    print("""
╔═══╗             ╔╗   ╔╗   ╔╗
║╔═╗║            ╔╝╚╗  ║║  ╔╝╚╗
║║ ╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗
║║ ╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣
║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║
╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝
          ╔═╝║
          ╚══╝

You finished all of your night's work, with your sanity still intact!
    Well, mostly intact...
    """)

#THE GAME PLAN FROM HERE
#at end of # of turns, if work points are at 100, player wins, if 100>p>80, player wins, but with penalty for next night, if less than 80, player loses
#do the same for happiness and energy (however, whether or not the player wins the night is not determined by these, they can only add a penalty for the next night)
#make a loop to play a "night" five times, for each day of the week
#...still don't know how to determine overall win/lose, perhaps total_points=0, and at the end of every night your performance gives you a # of points; at the end of the game, points added up and result in a "grade" (ex. A for excellent, F for fail)
#OOF IT BURNS














