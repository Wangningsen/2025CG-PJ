import cadquery as cq
w0=cq.Workplane('YZ',origin=(40,0,0))
r=w0.sketch().segment((-33,-22),(-3,-22)).arc((-19,-9),(-33,2)).close().assemble().finalize().extrude(-140).union(w0.sketch().segment((-20,2),(30,-9)).segment((30,-15)).arc((33,-2),(29,12)).arc((11,15),(-5,22)).arc((-14,15),(-20,5)).close().assemble().finalize().extrude(60))