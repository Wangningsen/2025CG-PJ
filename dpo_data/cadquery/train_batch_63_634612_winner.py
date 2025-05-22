import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,62))
r=w0.workplane(offset=-125/2).moveTo(92.5,-38).box(13,124,125).union(w0.sketch().push([(-51.5,67)]).rect(95,66).push([(-10,91)]).circle(1,mode='s').finalize().extrude(-3))