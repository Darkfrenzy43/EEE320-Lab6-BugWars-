"""

    Fode.


Creature Name: Fode.
Group Members: OCdt Velasco


    MAIN STRATEGY: photoglands. That's literally it :/. You become an impenetrable wall with a lot of these.
                To introduce some aggressiveness though, fode is programmed to move around randomly.
                In addition, fode is also programmed to not attack an enemy unless if it has enough strength to do so,
                keeping it as efficient as possible.

                It efficiently wipes out Hunter and SuperPlant, so I'm guessing it works. It made
                for a surprisingly small code solution as well. None of the other organs were of great
                help after some testing, so yeah, we're taking the photoglands approach.



    Notes:

        1 - cls is used when referring to the entire class (static), and self is used in an instance
        of the class (non-static)

        2 - Only way for us to gain strength is to find some of that green grass and eat it.

        3 - Bugs commit suicide when their strength hits 0.


    Status:

        - Clean up the code.




"""


# --- Importing files ---

from abc import ABC

from shared import Creature, Cilia, Propagator, Direction, CreatureTypeSensor, \
    Soil, Plant, PhotoGland;



# --- Class definition ---

class Fode(Creature, ABC):
    """      'Fode is coming.' - Eric Cho (based)     """

    # Creating required class attribute
    __instance_count = 0;

    def __init__(self):

        # Super constructor
        super().__init__()

        # Increment instance count
        Fode.__instance_count += 1;

        # instance vars for the Fode's organs
        self.cilia = None;
        self.sensor = None;
        self.prop = None;
        self.glands = [];


    @classmethod
    def instance_count(cls):
        return Fode.__instance_count;


    @classmethod
    def destroyed(cls):
        Fode.__instance_count -= 1;


    def do_turn(self):
        """ Is called every frame. Every turn we have, grow fode's organs, move fode around randomly,
        and make more fode if we can manage it. """

        self.grow_fode_organs();
        self.move_fode();
        self.make_more_fode();


    def grow_fode_organs(self):
        """ Method grows Fode's organs in order of priority: cilia, then
        creature sensor, then propagator, then finally fill up the rest with photoglands. """


        if not self.cilia and self.strength() > Cilia.CREATION_COST:
            self.cilia = Cilia(self)
        if not self.sensor and self.strength() > CreatureTypeSensor.CREATION_COST:
            self.sensor = CreatureTypeSensor(self)
        if not self.prop and self.strength() > Propagator.CREATION_COST:
            self.prop = FodePropagator(self)

        while self.strength() > PhotoGland.CREATION_COST:
            if len(self.glands) < 7:
                self.glands.append(PhotoGland(self));
            else:
                break;




    def move_fode(self):
        """ Make's fode's cilia move around in a random direction. """

        # Just move around if we have reasonable amount of energy to do so.
        if self.strength() > 0.2 * Creature.MAX_STRENGTH:
            self.cilia.move_in_direction(Direction.random());


    def make_more_fode(self):
        """ We make fode reproduce in a direction where there is soil or a plant, or make it reproduce
        and attack an enemy if fode has enough strength to do so. """

        # If we have at least 200 strength consider making fode reproduce onto soil or a plant
        # (This should make it reproduce really damn fast. Cover as much ground as we can)
        if self.strength() >= 0.1 * Creature.MAX_STRENGTH:

            # Find a direction where there is a plant or soil and repdouce
            for d in Direction:

                surroundings = self.sensor.sense(d)
                if surroundings == Soil or surroundings == Plant:
                    self.prop.give_birth(self.strength()/4, d)
                    break;

                # If we encounter an enemy, don't attack them unless we have enough strength.
                # Give the attacking fode a bit more strength too.
                elif surroundings != Soil and surroundings != Plant and surroundings != Fode:
                    if self.strength() >= 0.9 * Creature.MAX_STRENGTH:
                        self.prop.give_birth(self.strength() / 2, d);
                        break;



class FodePropagator(Propagator):
    """ Class that makes fode reproduce. """

    def make_child(self):
        return Fode();



# It's fode time.