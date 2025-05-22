import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
w1=cq.Workplane('YZ',origin=(-31,0,0))
r=w0.sketch().push([(-42.5,-59)]).rect(73,82).push([(-43,-59)]).circle(5,mode='s').push([(22.5,-50)]).rect(51,10).push([(74,95)]).circle(5).finalize().extrude(-9).union(w0.workplane(offset=73/2).moveTo(12,18).cylinder(73,29)).union(w1.workplane(offset=71/2).moveTo(12,18).cylinder(71,10))