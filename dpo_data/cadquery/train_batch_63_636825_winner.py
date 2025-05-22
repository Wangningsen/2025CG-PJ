import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,66))
r=w0.sketch().segment((-56,74),(24,-100)).segment((56,-85)).segment((56,-20)).segment((0,100)).close().assemble().finalize().extrude(-131)