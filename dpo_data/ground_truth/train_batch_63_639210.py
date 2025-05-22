import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
r=w0.sketch().push([(13,-54)]).circle(46).circle(24,mode='s').finalize().extrude(-36).union(w0.sketch().arc((-59,88),(-57,94),(-58,100)).close().assemble().finalize().extrude(-15))