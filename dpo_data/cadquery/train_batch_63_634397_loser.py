import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
r=w0.sketch().push([(-92,-7)]).circle(8).reset().face(w0.sketch().segment((10,5),(47,33)).segment((96,-20)).arc((51,49),(10,5)).assemble()).reset().face(w0.sketch().arc((11,-30),(36,-47),(61,-49)).close().assemble()).finalize().extrude(-42)