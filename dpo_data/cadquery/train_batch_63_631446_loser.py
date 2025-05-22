import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-48,-4),(-29,-4)).arc((0,-29),(29,-4)).segment((48,-4)).segment((48,4)).segment((29,4)).arc((0,29),(-29,4)).segment((-48,4)).close().assemble().finalize().extrude(200)