import cadquery as cq
w0=cq.Workplane('YZ',origin=(82,0,0))
r=w0.sketch().segment((-85,-53),(-34,-53)).segment((-34,-4)).segment((-24,12)).segment((-34,12)).segment((-34,44)).segment((-85,44)).close().assemble().finalize().extrude(-164).union(w0.sketch().arc((1,-35),(87,-80),(34,2)).arc((-82,73),(1,-35)).assemble().push([(-30.5,26.5)]).rect(33,99,mode='s').finalize().extrude(-100))