import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-17))
r=w0.sketch().segment((-88,12),(5,-75)).segment((88,12)).segment((80,19)).arc((13,5),(9,86)).segment((-6,100)).close().assemble().finalize().extrude(-41).union(w0.sketch().push([(57,-77)]).circle(23).push([(52,-67)]).circle(3,mode='s').finalize().extrude(75))