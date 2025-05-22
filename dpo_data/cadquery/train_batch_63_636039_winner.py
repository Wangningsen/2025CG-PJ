import cadquery as cq
w0=cq.Workplane('YZ',origin=(0,0,0))
r=w0.sketch().push([(0,44)]).circle(56).reset().face(w0.sketch().arc((-20,12),(0,8),(20,12)).close().assemble(),mode='s').reset().face(w0.sketch().segment((-20,77),(20,77)).arc((0,82),(-20,77)).assemble(),mode='s').finalize().extrude(-40).union(w0.sketch().push([(9,-70.5)]).rect(48,59).rect(46,31,mode='s').finalize().extrude(40))