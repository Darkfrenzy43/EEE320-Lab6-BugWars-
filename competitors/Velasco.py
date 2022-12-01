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

        3 - Bugs commit suicide for what reason again?

    Status:

        - Implementing basic version of bug.
        - make cracked up version of Fode.
        - create environment and bug sensor
        - create energy sensor

"""
from abc import ABC

# Import stuff
from shared import Creature, Cilia, Propagator, Direction, CreatureTypeSensor, Soil, Plant; # Import more here as needed

class Fode(Creature, ABC):
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
        Fode.__instance_count += 1;

        # Creating the organ objects?
        self.cilia = None;
        self.prop = None;
        self.energy_sensor = None;
        self.type_sensor = None;

    def do_turn(self):



        # simply create a cilia and womb if none was created yet (wtf is a cilia)
        if not self.cilia and self.strength() > Cilia.CREATION_COST:
            self.cilia = Cilia(self);
        if not self.prop and self.strength() > Propagator.CREATION_COST:
            self.prop = FodePropagator(self);
        if not self.type_sensor and self.strength() > CreatureTypeSensor.CREATION_COST:
            self.energy_sensor = CreatureTypeSensor(self);


        # alright, let's reproduce the mother fucker
        if self.strength() >= 0.5 * Creature.MAX_STRENGTH:

            # Let us find grass, and when we do, grow onto it. Or soil
            for d in Direction:
                surroundings = self.energy_sensor.sense(d)
                if surroundings == Soil or surroundings == Plant:

                    print("Shit was sensed. ");

                    self.prop.give_birth(self.strength()/2, Direction.NE)
                    break;


    @classmethod
    def instance_count(cls):
        return Fode.__instance_count;

    @classmethod
    def destroyed(cls):

        print("SHIT WAS DESTROYED.");

        Fode.__instance_count -= 1;

    pass;


class FodePropagator(Propagator):

    def make_child(self):

        return Fode();
