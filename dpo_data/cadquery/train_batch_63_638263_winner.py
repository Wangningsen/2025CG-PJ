import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((-63,-100),(-40,-100)).segment((-40,-30)).segment((63,-30)).segment((63,100)).segment((-41,100)).segment((-41,5)).segment((-63,5)).close().assemble().finalize().extrude(-69)