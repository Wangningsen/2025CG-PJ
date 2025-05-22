import cadquery as cq
w0=cq.Workplane('YZ',origin=(62,0,0))
r=w0.sketch().segment((-93,100),(-82,92)).arc((-88,98),(-93,100)).assemble().push([(42,-49)]).circle(51).circle(14,mode='s').finalize().extrude(-125)