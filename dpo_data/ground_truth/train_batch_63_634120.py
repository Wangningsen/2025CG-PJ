import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
w1=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().segment((-14,7),(0,4)).segment((11,48)).segment((-3,52)).close().assemble().finalize().extrude(-21).union(w0.sketch().push([(-68,26.5)]).rect(64,1).push([(63.5,10)]).rect(73,28).finalize().extrude(-13)).union(w1.workplane(offset=-85/2).moveTo(1,-2).cylinder(85,21))