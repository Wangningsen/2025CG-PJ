import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-33))
r=w0.sketch().push([(-75,-81)]).circle(19).push([(38.5,38.5)]).rect(7,123).push([(38.5,39)]).rect(1,4,mode='s').finalize().extrude(-22).union(w0.workplane(offset=89/2).moveTo(39,39).cylinder(89,55))