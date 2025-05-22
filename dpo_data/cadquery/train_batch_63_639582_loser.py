import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
w1=cq.Workplane('XY',origin=(0,0,55))
r=w0.workplane(offset=-113/2).moveTo(-55.5,-41.5).box(61,41,113).union(w0.sketch().push([(-55,-42)]).circle(28).reset().face(w0.sketch().segment((-15,-15),(-13,-15)).arc((-3,-13),(7,-13)).segment((7,6)).segment((-15,6)).close().assemble()).finalize().extrude(-108)).union(w0.workplane(offset=79/2).moveTo(75.5,62.5).box(21,53,79)).union(w1.sketch().arc((-81,5),(-62,-51),(-9,-29)).arc((0,95),(-81,5)).assemble().finalize().extrude(-138))