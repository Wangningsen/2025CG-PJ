import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
r=w0.workplane(offset=-51/2).moveTo(35,-64).cylinder(51,36).union(w0.sketch().push([(-11.5,17.5)]).rect(119,165).push([(-4,61)]).rect(42,12,mode='s').push([(13,-43)]).circle(10,mode='s').finalize().extrude(25))