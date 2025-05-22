import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
w1=cq.Workplane('YZ',origin=(-31,0,0))
r=w0.sketch().push([(-43,-59)]).rect(72,82).circle(7,mode='s').push([(14,-50)]).rect(72,10).push([(74,94)]).circle(6).finalize().extrude(-9).union(w0.workplane(offset=73/2).moveTo(12,18).cylinder(73,29)).union(w1.workplane(offset=72/2).moveTo(12,18).cylinder(72,20))