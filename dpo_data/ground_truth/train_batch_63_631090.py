import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('XY',origin=(0,0,-28))
r=w0.workplane(offset=87/2).moveTo(15,-48).box(20,104,87).union(w1.sketch().arc((-8,76),(-65,7),(23,-4)).segment((61,-4)).segment((61,24)).arc((68,48),(61,72)).segment((61,100)).segment((-8,100)).close().assemble().finalize().extrude(-45))