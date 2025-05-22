import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-46,0))
w1=cq.Workplane('YZ',origin=(30,0,0))
r=w0.sketch().arc((-100,-25),(-97,-27),(-95,-30)).segment((-23,-30)).segment((-23,90)).segment((-100,90)).close().assemble().reset().face(w0.sketch().segment((-80,40),(-54,11)).segment((-43,20)).segment((-69,49)).close().assemble(),mode='s').finalize().extrude(78).union(w0.workplane(offset=122/2).moveTo(-2,44).cylinder(122,33)).union(w1.sketch().segment((-56,40),(-14,40)).arc((-75,73),(-6,75)).segment((-56,75)).close().assemble().finalize().extrude(-120))