import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().push([(-55,32)]).circle(45).push([(52,-29.5)]).rect(4,65).finalize().extrude(-43).union(w0.workplane(offset=1/2).moveTo(52,-29).cylinder(1,48))