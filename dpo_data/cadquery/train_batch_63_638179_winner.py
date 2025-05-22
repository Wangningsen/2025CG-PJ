import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,51))
r=w0.sketch().push([(-58,4)]).circle(42).push([(-50,4)]).circle(32,mode='s').finalize().extrude(-102).union(w0.sketch().push([(88,-15.5)]).rect(24,61).push([(88,-9.5)]).rect(20,11,mode='s').finalize().extrude(-42))