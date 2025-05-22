import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,1))
r=w0.sketch().push([(-36,25)]).circle(64).push([(-26.5,57)]).rect(9,36,mode='s').finalize().extrude(-24).union(w0.workplane(offset=22/2).moveTo(77,-66).cylinder(22,23))