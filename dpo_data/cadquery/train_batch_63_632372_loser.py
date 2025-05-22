import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-94,-13),(-23,-13)).arc((-3,-10),(17,-13)).segment((94,-13)).segment((94,13)).segment((-94,13)).close().assemble().push([(33,2)]).circle(6,mode='s').finalize().extrude(-200).union(w0.workplane(offset=-175/2).cylinder(175,89))