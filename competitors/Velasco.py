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

class Fode(Creature, ABC):
    """ God someone please help me I'm finally on the last lab like yes this
    is finally happening it's been a really long semester but quick at the same time lmao.

    This bug was named after OCdt Foden, who I asked if I should name my bug "Foden"
    after he came up with a pretty cool name. Then I was like nahh it's gotta
    be more original, so I just took out the n and now we got "Fode". Based.

    """

    round_counter = 0;

    # Creating static vars
    __instance_count = 0;

    def __init__(self):

        # Super constructor
        super().__init__()

        # Increment instance count
        Fode.__instance_count += 1;

        # Creating the organ objects?
        self.cilia = None;
        self.photog1 = None;
        self.photog2 = None;
        self.photog3 = None;
        self.photog4 = None;
        self.photog5 = None;
        self.photog6 = None;
        self.photog7 = None;
        self.photog8 = None;
        self.prop = None;
        self.energy_sensor = None;
        self.type_sensor = None;


    def do_turn(self):


        # creating the organs
        if not self.cilia and self.strength() > Cilia.CREATION_COST:
            self.cilia = Cilia(self);
        if not self.prop and self.strength() > Propagator.CREATION_COST:
            self.prop = FodePropagator(self);
        if not self.type_sensor and self.strength() > CreatureTypeSensor.CREATION_COST:
            self.energy_sensor = CreatureTypeSensor(self);
        if not self.photog1 and self.strength() > PhotoGland.CREATION_COST:
            self.photog1 = PhotoGland(self);
        if not self.photog2 and self.strength() > PhotoGland.CREATION_COST:
            self.photog2 = PhotoGland(self);
        if not self.photog3 and self.strength() > PhotoGland.CREATION_COST:
            self.photog3 = PhotoGland(self);
        if not self.photog4 and self.strength() > PhotoGland.CREATION_COST:
            self.photog4 = PhotoGland(self);
        if not self.photog5 and self.strength() > PhotoGland.CREATION_COST:
            self.photog5 = PhotoGland(self);
        if not self.photog6 and self.strength() > PhotoGland.CREATION_COST:
            self.photog6 = PhotoGland(self);
        if not self.photog7 and self.strength() > PhotoGland.CREATION_COST:
            self.photog7 = PhotoGland(self);
        if not self.photog8 and self.strength() > PhotoGland.CREATION_COST:
            self.photog8 = PhotoGland(self);




        # alright, let's reproduce the mother fucker
        if self.strength() >= 0.5 * Creature.MAX_STRENGTH:

            # Let us find grass, and when we do, grow onto it. Or soil
            for d in Direction:
                surroundings = self.energy_sensor.sense(d)
                if surroundings == Soil or surroundings == Plant:

                    self.prop.give_birth(self.strength()/2, d)
                    break;




    @classmethod
    def instance_count(cls):
        return Fode.__instance_count;

    @classmethod
    def destroyed(cls):

        Fode.__instance_count -= 1;

    pass;


class FodePropagator(Propagator):

    def make_child(self):

        return Fode();
