import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.workplane(offset=-97/2).moveTo(-72,31).cylinder(97,28).union(w0.sketch().push([(64.5,-8.5)]).rect(71,101).push([(64,-8.5)]).rect(48,99,mode='s').finalize().extrude(-63))