import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.workplane(offset=-97/2).moveTo(-56,-73).box(24,54,97).union(w0.sketch().segment((-84,6),(-8,-33)).segment((12,8)).arc((84,28),(22,70)).segment((-35,100)).close().assemble().push([(-22,34)]).circle(6,mode='s').reset().face(w0.sketch().segment((17,18),(27,18)).segment((27,35)).close().assemble(),mode='s').finalize().extrude(-81))