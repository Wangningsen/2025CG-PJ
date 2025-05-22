import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-28))
w1=cq.Workplane('YZ',origin=(-37,0,0))
r=w0.sketch().push([(-15,66)]).rect(74,68).circle(16,mode='s').push([(14,40)]).circle(3,mode='s').finalize().extrude(-28).union(w0.workplane(offset=-3/2).moveTo(34.5,-11).box(35,32,3)).union(w1.workplane(offset=50/2).moveTo(-64.5,16).box(71,80,50))