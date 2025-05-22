import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
r=w0.workplane(offset=-137/2).box(42,182,137).union(w0.workplane(offset=63/2).moveTo(10.5,0).box(19,110,63))