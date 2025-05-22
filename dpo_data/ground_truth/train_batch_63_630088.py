import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
w1=cq.Workplane('XY',origin=(0,0,12))
r=w0.workplane(offset=86/2).moveTo(-96,-72).cylinder(86,4).union(w1.sketch().segment((-3,-36),(38,-36)).segment((38,-50)).arc((94,-13),(85,54)).segment((64,54)).segment((64,59)).segment((80,59)).arc((-10,54),(-3,-36)).assemble().finalize().extrude(-60))