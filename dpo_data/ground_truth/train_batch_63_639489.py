import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.sketch().segment((-39,-91),(-3,-100)).segment((15,-29)).segment((-19,-21)).segment((-22,-24)).close().assemble().finalize().extrude(2).union(w1.sketch().arc((-49,42),(37,17),(3,100)).segment((3,42)).close().assemble().finalize().extrude(21))