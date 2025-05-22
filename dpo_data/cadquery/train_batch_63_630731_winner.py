import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
r=w0.sketch().segment((-94,-68),(58,-100)).segment((94,68)).segment((-58,100)).close().assemble().push([(-63,-37)]).rect(36,16,mode='s').finalize().extrude(-75)