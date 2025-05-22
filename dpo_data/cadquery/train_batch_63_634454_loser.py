import cadquery as cq
w0=cq.Workplane('YZ',origin=(86,0,0))
w1=cq.Workplane('YZ',origin=(18,0,0))
r=w0.sketch().segment((-100,-43),(-63,-43)).arc((0,-92),(63,-43)).segment((100,-43)).segment((100,-10)).segment((99,-10)).segment((99,13)).segment((51,13)).arc((-2,38),(-54,13)).segment((-96,13)).segment((-96,-10)).segment((-100,-10)).close().assemble().finalize().extrude(-172).union(w1.sketch().segment((-22,67),(51,67)).arc((47,79),(51,92)).segment((-22,92)).close().assemble().finalize().extrude(40))