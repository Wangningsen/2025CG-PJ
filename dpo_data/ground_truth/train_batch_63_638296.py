import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('YZ',origin=(1,0,0))
r=w0.workplane(offset=-88/2).moveTo(52,39).cylinder(88,9).union(w0.sketch().segment((98,37),(99,37)).segment((99,36)).arc((100,37),(98,37)).assemble().finalize().extrude(-7)).union(w1.sketch().push([(-60,-18.5)]).rect(80,59).reset().face(w1.sketch().segment((-64,-48),(-55,-48)).segment((-55,-39)).arc((-39,-18),(-55,2)).segment((-55,11)).segment((-64,11)).segment((-64,2)).arc((-81,-18),(-64,-39)).close().assemble(),mode='s').finalize().extrude(78))