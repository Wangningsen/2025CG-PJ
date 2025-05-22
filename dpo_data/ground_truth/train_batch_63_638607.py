import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-17))
r=w0.sketch().segment((-88,12),(6,-76)).segment((88,12)).segment((84,16)).arc((8,9),(10,85)).segment((-6,100)).close().assemble().finalize().extrude(-41).union(w0.sketch().push([(57,-77)]).circle(23).push([(53,-70)]).circle(1,mode='s').finalize().extrude(75))