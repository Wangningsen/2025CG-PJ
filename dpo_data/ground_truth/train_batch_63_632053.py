import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
r=w0.sketch().arc((-42,-12),(-98,-49),(-32,-37)).segment((-21,-37)).segment((-21,-9)).segment((-42,-9)).close().assemble().push([(-66,-36)]).circle(11,mode='s').finalize().extrude(-88).union(w0.sketch().arc((-3,50),(-57,-2),(9,-38)).arc((99,19),(-3,50)).assemble().push([(-11,4)]).rect(36,28,mode='s').finalize().extrude(69))