import cadquery as cq
w0=cq.Workplane('YZ',origin=(-49,0,0))
w1=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.sketch().segment((-57,-37),(-49,-100)).segment((57,-87)).segment((51,-43)).segment((47,-43)).arc((21,-50),(0,-40)).segment((-10,-40)).segment((-10,-35)).segment((-3,-35)).arc((-20,-29),(-36,-35)).segment((-47,-35)).segment((-47,-39)).close().assemble().push([(-20,-31)]).circle(6,mode='s').finalize().extrude(10).union(w1.workplane(offset=47/2).moveTo(77,26).cylinder(47,23))