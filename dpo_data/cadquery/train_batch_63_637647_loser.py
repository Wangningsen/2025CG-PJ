import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-19))
r=w0.sketch().push([(-41.5,15.5)]).rect(37,103).push([(-30,38)]).circle(2,mode='s').finalize().extrude(-81).union(w0.workplane(offset=100/2).moveTo(44,-45).cylinder(100,22)).union(w0.workplane(offset=119/2).moveTo(-41,16).cylinder(119,25))