import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().push([(45,-80)]).circle(20).push([(68,74)]).circle(12).finalize().extrude(-55).union(w0.sketch().segment((-80,27),(-33,27)).arc((-6,-17),(41,4)).arc((8,21),(24,55)).arc((15,58),(7,59)).segment((7,100)).segment((-80,100)).close().assemble().finalize().extrude(-5)).union(w0.workplane(offset=-1/2).moveTo(18,-4.5).box(16,23,1))