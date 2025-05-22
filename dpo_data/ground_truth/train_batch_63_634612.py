import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,62))
r=w0.workplane(offset=-125/2).moveTo(92.5,-38).box(13,124,125).union(w0.sketch().push([(-51.5,67)]).rect(95,66).push([(-13.5,49.5)]).rect(15,9,mode='s').push([(-10,94)]).circle(2,mode='s').finalize().extrude(-3))