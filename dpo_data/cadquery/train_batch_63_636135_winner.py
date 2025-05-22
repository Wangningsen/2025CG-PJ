import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
r=w0.sketch().segment((-56,17),(-51,14)).segment((-51,-100)).segment((56,-100)).segment((56,100)).segment((-51,100)).segment((-51,20)).segment((-54,21)).close().assemble().reset().face(w0.sketch().segment((16,20),(21,18)).segment((26,35)).segment((21,37)).close().assemble(),mode='s').finalize().extrude(8)