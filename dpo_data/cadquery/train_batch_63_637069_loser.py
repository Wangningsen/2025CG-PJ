import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-63))
r=w0.sketch().segment((-70,82),(-27,100)).arc((-50,96),(-70,82)).assemble().reset().face(w0.sketch().segment((12,83),(30,42)).arc((25,64),(12,83)).assemble()).finalize().extrude(96).union(w0.sketch().push([(7,-37)]).circle(63).push([(7,-37.5)]).rect(40,109,mode='s').finalize().extrude(126))