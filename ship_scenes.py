# -*- coding: utf-8 -*-
from sys import exit
from random import randint, random
import ship_char

class Scene(object):

    def enter(self):
        print "This scene does not exist, subclass it and define enter()."
        exit(1)


class Death(Scene):

    memes = [
        'Oh dear, now I have to clean up this mess.',
        'Wow, you must have the IQ of a potted plant.',
        'I know of a tapeworm that could do a better job at this than you.',
        'As Principal Skinner would say: \'Pathetic.\'',
        'Well, I once saw an amoeba do worse at this than you. So cheer up!',
        'What is the point of you?!',
        'You really are a paragon of the human race, aren\'t you?',
        'Maybe you\'ll get this in a century or so.'
    ]

    def enter(self):
        print "-" * 70
        print "You died..."
        print Death.memes[randint(0, len(self.memes) - 1)]
        print "-" * 70
        exit(1)


class YourRoom(Scene):

    def enter(self):
        print "-" * 70
        print "YOUR ROOM"
        print "\n"
        print "You are a crewman on the cargo ship 'The XXX', which is currently"
        print "in the middle of the Pacific carrying some cargo you know little"
        print "about. Suddenly, in the middle of the night you wake up to a loud"
        print "crash and screaming outside your quarters."
        print "\n"
        print "Confused, you get up and turn on the light. You notice the engines"
        print "have stopped. The door to your room is locked so whatever caused"
        print "that ruckus outside can't get in. Most people would be content with"
        print "that and go back to sleep. You however, being a bit death-wishy,"
        print "decide to go outside and investigate."
        print "-" * 70

        while True:

            action = raw_input('> ')

            if "unlock door" in action:
                print "-" * 70
                print "In classic horror movie-'You really shouldn't do that'-style"
                print "you unlock your door and go through it, into the hallway."
                print "-" * 70
                return 'hallway'
            else:
                print "-" * 70
                print "I didn't feel like coding that choice. Do something else."
                print "-" * 70


class Hallway(Scene):

    def enter(self):
        print "-" * 70
        print "HALLWAY"
        print "\n"
        print "As you step out of your room you see one of your crewmates eerily"
        print "standing with his back turned to you. As you don't really feel"
        print "like breaking your stereotypical horror movie character of the"
        print "'person who does every single thing to get themselves killed'"
        print "you call out to him only to find that he has become undead. He"
        print "inches closer to you at an excrutiatingly slow pace (why do zombies"
        print "always do that?). You need to get to the engine room behind him"
        print "and he's coming for you! Quick, think! Or take your time..."
        print "he's really freakin' slow."
        print "-" * 70

        while True:

            action = raw_input('> ')

            if "run away" in action:
                print "-" * 70
                print "Now we're talking! Breaking stereotypes for the win! Being"
                print "the coward you are you run away from him (which really isn't"
                print "that hard). You quickly shake him off and take a bit of a"
                print "detour to reach the door to the engine room."
                print "-" * 70
                return "engine_room"
            elif "attack" in action:
                print "-" * 70
                print "Ever the smart guy you decide to attack him with your bare"
                print "hands. You find out that zombies are actually quite strong"
                print "(surprising, considering how damn slow they are). Your"
                print "crewmate overpowers you and you immediately regret your"
                print "decision as he starts eating you alive."
                print "-" * 70
                return 'death'
            else:
                print "-" * 70
                print "I didn't feel like coding that choice. Do something else."
                print "-" * 70


class EngineRoom(Scene):

    def enter(self):
        print "-" * 70
        print "ENGINE ROOM"
        print "\n"
        print "You need to turn on the engines and comms to be able to call for"
        print "help in the bridge of the ship. To turn on the engines you need"
        print "to enter a three digit code into the terminal. With this being a"
        print "horror cargo ship, the terminal goes on lockdown and the engine"
        print "room floods if the wrong code is entered 10 times in a row. So"
        print "get it right!"
        print "-" * 70

        code = "%d%d%d" % (randint(0, 9), randint(0, 9), randint(0, 9))
        tries = 0

        action = raw_input('[Terminal]> ')

        while code != action and tries < 9:
            print "*" * 11
            print "INCORRECT"
            print "*" * 11
            tries += 1
            action = raw_input('[Terminal]> ')

        if code == action:
            print "-" * 70
            print "As you enter the code you hear the engines of the ship rumble"
            print "and start. With the engines on, communications are back online"
            print "(Who needs comms without engines anyway?). Since there is"
            print "nothing left for you to do here, you make your way to the bridge"
            print "of this weirdly dangerous cargo ship."
            print "Why did you even apply for this job?"
            print "-" * 70
            return 'bridge'
        else:
            print "-" * 70
            print "You enter the code and the terminal goes on lockdown. Before"
            print "you know it water begins to flood the engine room and there"
            print "is no way out. You think about your actions and deem them to"
            print "be incredibly unintelligent. Your last though before water"
            print "fills your lungs is, quite strangely, of that really nice"
            print "burger you had at Five Guys about a year ago."
            print "-" * 70
            return 'death'


class Bridge(Scene):

    def enter(self):
        print "-" * 70
        print "BRIDGE"
        print "\n"
        print "As you enter the bridge, you are met by this horrible stench,"
        print "a bit like a fart under the sheets after a long night"
        print "of drinking. In front of you is this huge, writhing mass. You"
        print "assume, from the captain's hat on its 'head', that this thing used"
        print "to be the captain. You run to a locker nearby and grab a shotgun"
        print "(with a surprisingly unlimited ammo supply). Get ready to fight!"
        print "-" * 70
        return 'fight'


class Fight(Scene):

    def enter(self):
        print "+" * 70
        print "BOSS FIGHT"
        print "\n"
        print "You have 4 options:"
        print "A 'body shot': Minimal damage, 90%\ chance to hit."
        print "A 'nut shot': Medium damage, 45%\ chance to hit."
        print "A 'headshot': High damage, 20%\ chance to hit."
        print "'GO FOR THE EYES': Extremely high damage, 5%\ chance to hit."
        print "+" * 70

        captain = ship_char.Character(600, 60)
        player = ship_char.Character(300, 30)
        roll = 0.0

        while captain.health > 0 and player.health > 0:

            attack = raw_input('[Attack]> ')

            if "body shot" in attack:
                roll = random()
                if roll <= 0.9:
                    print "+" * 70
                    print "You hit the captain in the body!"
                    print "+" * 70
                    captain.health -= player.attack
                else:
                    print "+" * 70
                    print "You missed! Curse your shitty depth perception!"
                    print "The captain hits you!"
                    print "+" * 70
                    player.health -= captain.attack
            elif "nut shot" in attack:
                roll = random()
                if roll <= 0.45:
                    print "+" * 70
                    print "You hit the captain in his malformed plums!"
                    print "+" * 70
                    captain.health -= player.attack * 5
                else:
                    print "+" * 70
                    print "You missed! Curse his tiny plums!"
                    print "The captain swings his tiny sack into your face!"
                    print "+" * 70
                    player.health -= captain.attack * 2
            elif "headshot" in attack:
                roll = random()
                if roll <= 0.2:
                    print "+" * 70
                    print "HEADSHOT! Got'em!!"
                    print "+" * 70
                    captain.health -= player.attack * 15
                else:
                    print "+" * 70
                    print "You missed! Curse his malformed head!"
                    print "He still manages to headbutt you though!"
                    print "+" * 70
                    player.health -= captain.attack * 3
            elif "GO FOR THE EYES" in attack:
                roll = random()
                if roll <= 0.05:
                    print "+" * 70
                    print "YOU DID IT! YOU GOT HIM IN THE EYES!"
                    print "(Usually, only Boo manages to go for those.)"
                    print "+" * 70
                    captain.health -=  player.attack * 20
                else:
                    print "+" * 70
                    print "You missed! Curse his tiny eyes, like pissholes in the snow!"
                    print "The captain stares into your soul! IT REALLY HURTS!"
                    print "+" * 70
                    player.health -= captain.attack * 4

        if captain.health == 0:
            print "+" * 70
            print "The mass that once was the captain screams a final scream and"
            print "collapses. It is over. You rush to the comms unit and call for"
            print "aid. However, the only aid that is on offer for an infested"
            print "cargo ship is an airstrike. Go figure. You must get to a life"
            print "boat quickly or you'll be blown to pieces."
            print "+" * 70
            return 'deck'
        else:
            print "+" * 70
            print "After a right thrasing by the mass that once was the captain,"
            print "you collapse. The last thing you feel is a little itch on"
            print "your nose as the captain bites into it."
            print "+" * 70
            return 'death'


class Deck(Scene):

    def enter(self):
        print "-" * 70
        print "CARGO DECK"
        print "\n"
        print "You leave the bridge and pass down onto the cargo deck. The rest"
        print "of the crew is not very happy you just killed their master and are,"
        print "slowly as ever, closing in on you, surrounding you. You, being a"
        print "hell of a lot quicker than them, rush to the lifeboat controls."
        print "The terminal seems to be malfunctioning so you have no idea which,"
        print "if any, of the lifeboats still work. Being quite all-in in this"
        print "situation, you decide to guess which of the four lifeboats still"
        print "works."
        print "-" * 70

        boat = "%d" % randint(1,4)
        guesses = 0

        action = raw_input('[Boat]> ')

        while action != boat and guesses < 1:
            print "*" * 40
            print "Guess it's not boat number %s, huh?" % action
            print "*" * 40
            guesses += 1
            action = raw_input('[Boat]> ')

        if action == boat:
            print "-" * 70
            print "Holy smokes, you guessed right! Boat number %s begins to" % action
            print "lower down into the ocean, almost as slowly as the undead"
            print "still closing in (Honestly, does everything move slowly on this"
            print "ship?). You make a run for the lifeboat and jump in."
            print "-" * 70
            return 'lifeboat'
        else:
            print "-" * 70
            print "After guessing wrong 2 times, you feel a little nibble at your"
            print "leg. You look down and see Julius the Chef biting your ankle."
            print "you soon find out since Julius rips out your achilles tendon,"
            print "making it impossible for you to run away. Smart guy, that Julius."
            print "Unable to run away, the rest of the crew quicly descends upon"
            print "you and eats you alive."
            print "-" * 70
            return 'death'


class LifeBoat(Scene):

    def enter(self):
        print "-" * 70
        print "THE LIFEBOAT"
        print "\n"
        print "The lifeboat lowers gently into the inky blackness of the Pacific."
        print "You are however not in the clear yet, as that 'help' you called for"
        print "in the bridge is still on its way to blow shit up. You row as fast"
        print "as you can away from the cargo ship. When you have gotten as far"
        print "as your weak arms can row (probably not far enough), you lie down"
        print "in the boat, turn on your emergency signal, and prepare to watch"
        print "the fireworks."
        print "\n"
        print "You are saved (I seriously did not expect that)."
        print "-" * 70
        exit(1)
