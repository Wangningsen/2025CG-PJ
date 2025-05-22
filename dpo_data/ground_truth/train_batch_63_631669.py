import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-33,-15),(4,-15)).arc((5,-10),(7,-15)).segment((33,-15)).segment((33,15)).arc((1,-5),(-33,9)).close().assemble().finalize().extrude(-200)