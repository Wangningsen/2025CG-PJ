import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-57))
r=w0.sketch().segment((-70,-42),(27,-100)).segment((70,-28)).segment((-5,17)).arc((7,98),(-31,25)).close().assemble().finalize().extrude(114)