import cadquery as cq
w0=cq.Workplane('YZ',origin=(3,0,0))
r=w0.sketch().push([(50,21)]).circle(11).push([(44,21)]).rect(2,6,mode='s').push([(50,21)]).circle(4,mode='s').finalize().extrude(-103).union(w0.workplane(offset=97/2).moveTo(-13,0).cylinder(97,48))