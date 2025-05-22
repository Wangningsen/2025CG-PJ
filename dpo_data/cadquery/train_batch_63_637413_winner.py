import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,45,0))
r=w0.sketch().segment((-100,-92),(100,-92)).segment((100,42)).segment((80,42)).arc((-1,92),(-83,42)).segment((-100,42)).close().assemble().finalize().extrude(-90)