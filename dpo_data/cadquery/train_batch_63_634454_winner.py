import cadquery as cq
w0=cq.Workplane('YZ',origin=(87,0,0))
w1=cq.Workplane('YZ',origin=(58,0,0))
r=w0.sketch().segment((-100,-43),(-63,-43)).arc((0,-92),(63,-43)).segment((100,-43)).segment((100,-8)).segment((99,-8)).segment((99,13)).segment((51,13)).arc((0,38),(-51,13)).segment((-96,13)).segment((-96,-8)).segment((-100,-8)).close().assemble().finalize().extrude(-173).union(w1.sketch().segment((-22,67),(51,67)).arc((46,79),(47,92)).segment((-22,92)).close().assemble().finalize().extrude(-40))