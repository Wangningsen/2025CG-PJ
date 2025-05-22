import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.workplane(offset=137/2).box(42,182,137).union(w0.sketch().segment((1,-55),(9,-55)).segment((20,-55)).segment((20,55)).segment((9,55)).segment((1,55)).close().assemble().finalize().extrude(200))