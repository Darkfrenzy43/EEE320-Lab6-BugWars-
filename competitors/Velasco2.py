"""

OCdt Velasco's Creature (pls god save his soul omg im filling this thign with memes maybe idk it's been a long
semester)

Creature Name: Fode.
Group Members: Literally only OCdt Velasco.


    MAIN STRAT: maybe, we can make ours like an amoeba, and have it circle a bug? Or like an explosion kinda
    deal, where we hold up all the power, and then we explode out and the opponent wouldn't be able to eat us since
    we'd have more stored up? Defensive yet offensive gameplay


    Notes:

        1 - cls is used when referring to the entire class (static), and self is used in an instance
        of the class (non-static)

        2 - Only way for us to gain strength is to find some of that green grass shit and eat it.

        3 - Bugs commit suicide when their strength hits 0.


    Status:

        - Implementing basic version of bug.
        - make cracked up version of Fode.
        - create environment and bug sensor
        - create energy sensor



"""

from abc import ABC


# Import stuff
from shared import Creature, Cilia, Propagator, Direction, CreatureTypeSensor, \
    Soil, Plant, PhotoGland; # Import more here as needed



class Fode2(Creature, ABC):
    """ God someone please help me I'm finally on the last lab like yes this
    is finally happening it's been a really long semester but quick at the same time lmao.

    This bug was named after OCdt Foden, who I asked if I should name my bug "Foden"
    after he came up with a pretty cool name. Then I was like nahh it's gotta
    be more original, so I just took out the n and now we got "Fode". Based.

    """


    # Creating static vars
    __instance_count = 0;


    def __init__(self):

        # Super constructor
        super().__init__()

        # Increment instance count
        Fode2.__instance_count += 1;

        # make an array which contains the organs of a given Fode
        self.cilia = None;
        self.sensor = None;
        self.prop = None;
        self.glands = [];


    def grow_fode_organs(self):


        # First, do the cilia
        if not self.cilia and self.strength() > Cilia.CREATION_COST:
            self.cilia = Cilia(self)

        # Next, sensor
        if not self.sensor and self.strength() > CreatureTypeSensor.CREATION_COST:
            self.sensor = CreatureTypeSensor(self)

        # Create propagator
        if not self.prop and self.strength() > Propagator.CREATION_COST:
            self.prop = FodePropagator(self)


        # Next, fill it up with photoglands to 7
        if len(self.glands) < 7:

            if self.strength() > PhotoGland.CREATION_COST:
                self.glands.append(PhotoGland(self));



    def do_turn(self):


        self.grow_fode_organs();

         # Move fode around randomly
        self.move_fode();

        # alright, let's reproduce the mother fucker
        if self.strength() >= 0.1 * Creature.MAX_STRENGTH:

            for d in Direction:
                surroundings = self.sensor.sense(d)



                if surroundings == Soil or surroundings == Plant:

                    self.prop.give_birth(self.strength()/4, d)
                    break;

                # Only spawn on an enemy if we have enough strength
                elif surroundings != Soil and surroundings != Plant and surroundings != Fode2:

                    if self.strength() >= 0.5 * Creature.MAX_STRENGTH:
                        self.prop.give_birth(self.strength() / 2, d);
                        break;



    def move_fode(self):

        if self.strength() > 0.2 * Creature.MAX_STRENGTH:

            self.cilia.move_in_direction(Direction.random());


    @classmethod
    def instance_count(cls):
        return Fode2.__instance_count;

    @classmethod
    def destroyed(cls):

        Fode2.__instance_count -= 1;



class FodePropagator(Propagator):

    def make_child(self):

        return Fode2();



