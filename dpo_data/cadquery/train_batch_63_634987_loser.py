import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.sketch().segment((-100,-65),(23,-65)).segment((23,-15)).arc((100,19),(20,49)).segment((20,45)).segment((-100,45)).close().assemble().finalize().extrude(-96)