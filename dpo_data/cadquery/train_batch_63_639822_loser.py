import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,33))
r=w0.sketch().arc((-36,-41),(14,-51),(35,-92)).segment((100,-92)).segment((100,33)).segment((-36,33)).close().assemble().finalize().extrude(-66).union(w0.workplane(offset=-15/2).moveTo(-81,73).cylinder(15,19))