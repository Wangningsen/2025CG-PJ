import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
w1=cq.Workplane('YZ',origin=(12,0,0))
r=w0.workplane(offset=-17/2).moveTo(32.5,75.5).box(21,15,17).union(w0.workplane(offset=67/2).moveTo(8,89).cylinder(67,11)).union(w1.sketch().segment((-100,-87),(15,-87)).segment((15,-66)).arc((65,-13),(8,38)).segment((8,87)).segment((-77,87)).segment((-77,-16)).segment((-38,-16)).arc((-33,-37),(-16,-56)).segment((-100,-56)).close().assemble().finalize().extrude(-58))