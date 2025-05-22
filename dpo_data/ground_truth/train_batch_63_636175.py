import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,59,0))
r=w0.sketch().rect(66,200).reset().face(w0.sketch().segment((-5,-13),(-4,-15)).segment((-4,-11)).close().assemble(),mode='s').reset().face(w0.sketch().segment((31,-18),(33,-16)).segment((31,-15)).close().assemble(),mode='s').finalize().extrude(-118)