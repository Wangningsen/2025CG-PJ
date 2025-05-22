import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().arc((-23,-32),(7,-100),(28,-29)).arc((-2,100),(-23,-32)).assemble().push([(1,-81)]).circle(14,mode='s').finalize().extrude(16)