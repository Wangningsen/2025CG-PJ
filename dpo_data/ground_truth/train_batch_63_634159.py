import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,88))
r=w0.sketch().segment((-57,-100),(57,-100)).segment((57,100)).segment((28,100)).arc((49,43),(-3,12)).segment((-3,-13)).segment((-7,-13)).segment((-7,13)).arc((-43,52),(-21,100)).segment((-57,100)).close().assemble().push([(46,-32)]).circle(2,mode='s').finalize().extrude(-176).union(w0.workplane(offset=-23/2).box(2,150,23))