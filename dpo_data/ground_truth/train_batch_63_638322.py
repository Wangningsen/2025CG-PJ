import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
r=w0.workplane(offset=32/2).moveTo(0,33).cylinder(32,67).union(w0.sketch().push([(19.5,-41.5)]).rect(41,117).push([(1.5,-67)]).rect(3,2,mode='s').reset().face(w0.sketch().segment((4,-79),(11,-90)).segment((20,-85)).segment((13,-73)).close().assemble(),mode='s').finalize().extrude(76))