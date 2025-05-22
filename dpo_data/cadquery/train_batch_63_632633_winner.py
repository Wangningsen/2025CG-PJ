import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
r=w0.sketch().push([(-60,38)]).circle(40).push([(-53.5,23.5)]).rect(5,13,mode='s').finalize().extrude(-84).union(w0.workplane(offset=-35/2).moveTo(91,-69).cylinder(35,9))