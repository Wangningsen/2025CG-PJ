import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.workplane(offset=-85/2).moveTo(-15,-38.5).box(32,15,85).union(w0.sketch().segment((-88,-41),(-57,-41)).segment((-57,-79)).segment((88,-79)).segment((88,54)).segment((59,54)).segment((59,84)).segment((-88,84)).close().assemble().reset().face(w0.sketch().segment((-42,54),(57,54)).arc((8,82),(-42,54)).assemble(),mode='s').finalize().extrude(115)).union(w1.workplane(offset=72/2).moveTo(-60,22).cylinder(72,24))