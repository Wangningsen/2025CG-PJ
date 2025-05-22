import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,12))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.workplane(offset=-67/2).moveTo(-67,-27).cylinder(67,23).union(w0.sketch().segment((-84,49),(-53,33)).arc((-26,-12),(28,-12)).segment((64,-28)).segment((90,23)).segment((59,39)).arc((29,85),(-25,83)).segment((-57,100)).close().assemble().finalize().extrude(43)).union(w1.sketch().segment((-61,-87),(-26,-87)).segment((-26,-100)).arc((-19,-95),(-15,-87)).segment((-15,-67)).segment((-61,-67)).close().assemble().finalize().extrude(-31))