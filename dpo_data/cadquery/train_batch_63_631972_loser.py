import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,84))
r=w0.sketch().segment((-62,-20),(-59,-23)).segment((-52,-17)).segment((-59,-13)).close().assemble().finalize().extrude(-168).union(w0.sketch().segment((-58,100),(28,-100)).arc((51,32),(-58,100)).assemble().finalize().extrude(-119))