import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
r=w0.workplane(offset=-28/2).moveTo(43,22).cylinder(28,39).union(w0.sketch().push([(-37,-55)]).circle(45).push([(-24,52)]).rect(92,96).rect(76,84,mode='s').push([(-23.5,51.5)]).rect(35,81).finalize().extrude(-23))