import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
r=w0.workplane(offset=-55/2).moveTo(39.5,22.5).box(5,81,55).union(w0.workplane(offset=-43/2).moveTo(5.5,71.5).box(15,57,43)).union(w0.sketch().segment((-42,-100),(-29,-100)).arc((-29,-58),(2,-45)).segment((2,-44)).segment((4,-44)).arc((13,-48),(22,-55)).segment((22,-13)).segment((-42,-13)).close().assemble().finalize().extrude(77))