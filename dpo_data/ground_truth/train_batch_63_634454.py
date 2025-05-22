import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,67))
w1=cq.Workplane('YZ',origin=(86,0,0))
r=w0.sketch().segment((17,-22),(57,-22)).segment((57,51)).arc((37,46),(17,51)).close().assemble().finalize().extrude(25).union(w1.sketch().segment((-100,-43),(-63,-43)).arc((0,-92),(63,-43)).segment((100,-43)).segment((100,-10)).segment((99,-10)).segment((99,13)).segment((51,13)).arc((0,38),(-51,13)).segment((-96,13)).segment((-96,-10)).segment((-100,-10)).close().assemble().finalize().extrude(-173))