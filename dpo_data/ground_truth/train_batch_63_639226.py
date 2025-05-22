import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,1,0))
r=w0.workplane(offset=-49/2).moveTo(-33,66).cylinder(49,34).union(w0.sketch().segment((-50,-15),(-47,-92)).segment((-7,-90)).arc((67,-59),(1,-14)).segment((1,-13)).close().assemble().reset().face(w0.sketch().segment((3,-56),(4,-88)).segment((8,-88)).segment((8,-56)).close().assemble(),mode='s').finalize().extrude(47))