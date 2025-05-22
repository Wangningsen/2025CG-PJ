import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
r=w0.workplane(offset=-68/2).moveTo(-41,11).cylinder(68,59).union(w0.sketch().push([(80,-50)]).circle(20).push([(77,-31)]).circle(2,mode='s').finalize().extrude(-58)).union(w0.workplane(offset=55/2).moveTo(-41,11).cylinder(55,53))