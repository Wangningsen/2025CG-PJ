import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-72))
r=w0.workplane(offset=22/2).moveTo(-49.5,-6).box(101,90,22).union(w0.sketch().segment((80,44),(84,35)).segment((100,42)).segment((96,51)).close().assemble().push([(86,43)]).circle(1,mode='s').finalize().extrude(143))