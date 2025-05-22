import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
r=w0.sketch().segment((4,-43),(81,-75)).segment((100,-27)).segment((24,3)).close().assemble().finalize().extrude(-66).union(w0.sketch().arc((-58,29),(-58,-72),(-14,18)).segment((21,18)).segment((21,75)).segment((-58,75)).close().assemble().finalize().extrude(-37)).union(w0.workplane(offset=50/2).moveTo(14,-69).box(28,6,50))