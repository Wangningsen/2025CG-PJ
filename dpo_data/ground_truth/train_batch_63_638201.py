import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.workplane(offset=28/2).moveTo(-18,-92).cylinder(28,8).union(w0.sketch().arc((19,89),(-36,-8),(48,65)).segment((48,100)).segment((19,100)).close().assemble().push([(-4.5,79.5)]).rect(47,7,mode='s').push([(0,36)]).circle(13,mode='s').push([(34,49)]).rect(10,20,mode='s').finalize().extrude(95))