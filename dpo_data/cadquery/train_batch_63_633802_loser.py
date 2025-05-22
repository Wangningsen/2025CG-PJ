import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
w1=cq.Workplane('ZX',origin=(0,18,0))
r=w0.workplane(offset=-52/2).moveTo(71,-17.5).box(56,87,52).union(w0.sketch().push([(60,-47)]).circle(40).push([(47,-43)]).circle(3,mode='s').push([(71,-47)]).circle(4,mode='s').finalize().extrude(29)).union(w1.sketch().segment((-100,15),(-68,15)).arc((-12,-44),(-28,28)).segment((-28,32)).arc((3,38),(-28,44)).segment((-28,87)).segment((-100,87)).close().assemble().push([(-40,-16)]).circle(26,mode='s').finalize().extrude(-55))