import cadquery as cq
w0=cq.Workplane('YZ',origin=(-49,0,0))
w1=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().segment((-57,-37),(-49,-100)).segment((57,-87)).segment((51,-39)).arc((13,-48),(-15,-20)).arc((-29,-23),(-36,-34)).close().assemble().reset().face(w0.sketch().segment((-26,-33),(-12,-31)).segment((-12,-29)).segment((-26,-29)).close().assemble(),mode='s').finalize().extrude(10).union(w1.workplane(offset=-47/2).moveTo(77,26).cylinder(47,23))