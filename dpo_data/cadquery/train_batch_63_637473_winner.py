import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,43))
r=w0.workplane(offset=-114/2).moveTo(-13.5,36.5).box(119,127,114).union(w0.sketch().segment((-19,-63),(-11,-100)).segment((20,-94)).arc((22,-67),(43,-88)).segment((45,-87)).segment((45,-90)).segment((73,-85)).segment((66,-48)).close().assemble().finalize().extrude(28))