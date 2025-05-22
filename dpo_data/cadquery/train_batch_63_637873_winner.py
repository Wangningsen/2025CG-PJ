import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('XY',origin=(0,0,-72))
r=w0.sketch().segment((5,-45),(81,-75)).segment((100,-27)).segment((24,3)).close().assemble().finalize().extrude(-66).union(w0.sketch().arc((-59,29),(-61,-72),(-15,18)).segment((21,18)).segment((21,75)).segment((-58,75)).segment((-58,65)).segment((-59,65)).close().assemble().finalize().extrude(-37)).union(w1.workplane(offset=6/2).moveTo(26,14).box(64,28,6))