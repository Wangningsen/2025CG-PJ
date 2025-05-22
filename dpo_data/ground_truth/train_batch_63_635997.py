import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-71))
r=w0.workplane(offset=22/2).moveTo(-49.5,-6).box(101,90,22).union(w0.sketch().segment((80,44),(84,35)).segment((100,42)).segment((96,51)).segment((90,48)).arc((90,44),(86,47)).close().assemble().finalize().extrude(143))