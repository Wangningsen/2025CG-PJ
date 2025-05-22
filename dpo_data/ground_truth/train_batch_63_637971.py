import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-29,65),(-19,-68)).segment((29,-65)).segment((19,68)).close().assemble().reset().face(w0.sketch().segment((-2,13),(-1,-13)).segment((2,-13)).segment((1,13)).close().assemble(),mode='s').finalize().extrude(-200)