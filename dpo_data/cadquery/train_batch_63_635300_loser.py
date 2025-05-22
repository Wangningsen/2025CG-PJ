import cadquery as cq
w0=cq.Workplane('YZ',origin=(0,0,0))
w1=cq.Workplane('ZX',origin=(0,-53,0))
r=w0.sketch().segment((-13,31),(71,31)).segment((71,52)).segment((44,52)).segment((44,66)).segment((-13,66)).close().assemble().push([(29,50)]).circle(4,mode='s').finalize().extrude(-100).union(w0.workplane(offset=100/2).moveTo(-22.5,27.5).box(97,55,100)).union(w1.workplane(offset=61/2).moveTo(-24.5,15.5).box(83,95,61))