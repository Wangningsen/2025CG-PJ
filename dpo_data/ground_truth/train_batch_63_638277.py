import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
w1=cq.Workplane('YZ',origin=(56,0,0))
r=w0.sketch().segment((-29,-56),(-3,-56)).segment((-3,39)).segment((-29,39)).segment((-29,-23)).arc((-100,-37),(-29,-50)).close().assemble().finalize().extrude(-93).union(w1.workplane(offset=44/2).moveTo(12,27.5).box(122,9,44))