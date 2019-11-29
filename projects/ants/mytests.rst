This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *



    Case container
        >>> hive, layout = Hive(AssaultPlan()), dry_layout
        >>> colony = AntColony(None, hive, ant_types(), layout, (1, 9))
        >>> # Testing bodyguard performs thrower's action
        >>> bodyguard = BodyguardAnt()
        >>> thrower = ThrowerAnt()
        >>> bee = Bee(2)
        >>> # Place bodyguard before thrower
        >>> colony.places["tunnel_0_0"].add_insect(bodyguard)
        >>> colony.places["tunnel_0_0"].ant.can_contain(thrower)
        True

    Case problemec:
        >>> hive, layout = Hive(AssaultPlan()), dry_layout
        >>> dimensions = (1, 9)
        >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
        >>> # Testing Slow
        >>> slow = SlowThrower()
        >>> bee = Bee(3)
        >>> colony.places["tunnel_0_0"].add_insect(slow)
        >>> colony.places["tunnel_0_4"].add_insect(bee)
        >>> slow.action(colony)
        applied effect!
        >>> colony.time = 1
        >>> bee.action(colony)
        new method
        slowed!
        >>> bee.place.name # SlowThrower should cause slowness on odd turns
        'tunnel_0_4'
        >>> colony.time = 2
        >>> bee.action(colony)
        new method
        not slowed!
        >>> bee.place.name
        'tunnel_0_3'
        >>> colony.time = 3