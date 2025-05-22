import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().arc((11,-8),(-51,-58),(27,-30)).arc((51,2),(11,-8)).assemble().push([(27,-9)]).circle(10,mode='s').push([(70,-76)]).circle(24).push([(60,-73.5)]).rect(6,21,mode='s').finalize().extrude(15).union(w0.workplane(offset=73/2).moveTo(-64,70).cylinder(73,30))