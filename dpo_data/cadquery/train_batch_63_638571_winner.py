import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-46,0))
w1=cq.Workplane('YZ',origin=(30,0,0))
r=w0.sketch().segment((-100,-24),(-91,-24)).segment((-91,-30)).segment((-23,-30)).segment((-23,90)).segment((-100,90)).close().assemble().reset().face(w0.sketch().segment((-82,42),(-57,10)).segment((-41,21)).segment((-66,52)).close().assemble(),mode='s').finalize().extrude(78).union(w0.workplane(offset=122/2).moveTo(-2,44).cylinder(122,33)).union(w1.sketch().segment((-56,40),(-14,40)).segment((-14,39)).arc((-76,65),(-6,75)).segment((-56,75)).close().assemble().finalize().extrude(-120))