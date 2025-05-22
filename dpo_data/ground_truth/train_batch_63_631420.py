import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,52,0))
r=w0.sketch().rect(62,200).reset().face(w0.sketch().segment((-18,-1),(-13,-13)).segment((18,1)).segment((13,13)).close().assemble(),mode='s').finalize().extrude(-104)