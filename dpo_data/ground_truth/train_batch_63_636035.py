import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('XY',origin=(0,0,61))
r=w0.workplane(offset=33/2).moveTo(30.5,49.5).box(25,101,33).union(w0.sketch().arc((-36,1),(-27,52),(20,72)).arc((-41,62),(-36,1)).assemble().reset().face(w0.sketch().segment((-23,-34),(-20,-49)).segment((-1,-45)).segment((-1,-100)).segment((51,-100)).segment((51,-23)).arc((49,-24),(47,-26)).segment((45,-17)).close().assemble()).finalize().extrude(63)).union(w1.workplane(offset=-11/2).moveTo(-6.5,-28).box(69,24,11))