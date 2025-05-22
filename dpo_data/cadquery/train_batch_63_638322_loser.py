import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
r=w0.workplane(offset=32/2).moveTo(0,31).cylinder(32,67).union(w0.sketch().push([(19.5,-41.5)]).rect(41,117).push([(10,-78)]).circle(6,mode='s').push([(19,-83)]).circle(3,mode='s').finalize().extrude(76))