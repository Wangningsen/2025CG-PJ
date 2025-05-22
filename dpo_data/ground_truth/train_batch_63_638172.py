import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
w1=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().arc((16,52),(16,14),(35,47)).arc((32,47),(31,50)).arc((26,52),(20,52)).arc((19,49),(16,52)).assemble().finalize().extrude(74).union(w0.workplane(offset=125/2).cylinder(125,60)).union(w1.sketch().arc((-100,1),(-95,-10),(-91,-22)).segment((17,-22)).segment((17,22)).segment((-100,22)).close().assemble().finalize().extrude(-47))