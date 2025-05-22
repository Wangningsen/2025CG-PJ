import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
w1=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().push([(-15,66)]).rect(74,68).circle(16,mode='s').push([(12,41)]).circle(1,mode='s').finalize().extrude(-28).union(w0.workplane(offset=-3/2).moveTo(34.5,-11).box(35,32,3)).union(w1.workplane(offset=79/2).moveTo(-12,-64.5).box(50,71,79))