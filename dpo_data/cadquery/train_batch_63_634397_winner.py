import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
r=w0.sketch().push([(-92,-7)]).circle(8).reset().face(w0.sketch().segment((12,2),(51,35)).segment((96,-20)).arc((51,49),(12,-20)).arc((11,-23),(12,-25)).arc((32,-46),(57,-48)).close().assemble()).finalize().extrude(42)