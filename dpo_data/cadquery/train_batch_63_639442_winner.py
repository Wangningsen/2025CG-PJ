import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
r=w0.sketch().rect(200,84).push([(-84.5,-28.5)]).rect(11,5,mode='s').push([(45,29)]).circle(11,mode='s').finalize().extrude(-139).union(w0.workplane(offset=32/2).cylinder(32,4)).union(w0.workplane(offset=32/2).box(122,142,32))