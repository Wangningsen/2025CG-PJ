import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,56))
r=w0.sketch().push([(-75,-31)]).circle(12).reset().face(w0.sketch().arc((14,-65),(41,-100),(53,-58)).arc((25,-22),(14,-65)).assemble()).reset().face(w0.sketch().arc((24,-67),(37,-84),(45,-64)).arc((35,-66),(24,-67)).assemble(),mode='s').finalize().extrude(-112).union(w0.workplane(offset=-111/2).moveTo(46,59).cylinder(111,41))