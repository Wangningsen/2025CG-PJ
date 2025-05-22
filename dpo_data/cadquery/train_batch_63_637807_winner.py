import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,63,0))
r=w0.sketch().arc((7,2),(26,3),(39,16)).arc((56,13),(72,28)).segment((4,28)).segment((4,43)).segment((72,43)).arc((54,58),(33,54)).arc((-67,70),(7,2)).assemble().finalize().extrude(-130).union(w0.workplane(offset=4/2).moveTo(24,-89).cylinder(4,11))