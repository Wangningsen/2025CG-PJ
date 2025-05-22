import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
r=w0.sketch().arc((4,9),(0,-99),(49,-6)).arc((52,99),(4,9)).assemble().reset().face(w0.sketch().segment((18,40),(64,47)).segment((64,54)).segment((18,46)).close().assemble(),mode='s').finalize().extrude(-128).union(w0.sketch().arc((10,-87),(25,-82),(37,-73)).arc((-47,65),(10,-87)).assemble().finalize().extrude(64))