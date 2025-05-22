import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
r=w0.workplane(offset=-137/2).box(42,182,137).union(w0.sketch().segment((1,-55),(20,-55)).segment((20,55)).segment((1,55)).segment((1,-11)).arc((3,-12),(1,-13)).close().assemble().finalize().extrude(63))