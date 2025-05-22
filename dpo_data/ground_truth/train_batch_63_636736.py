import cadquery as cq
w0=cq.Workplane('YZ',origin=(23,0,0))
r=w0.sketch().arc((-72,-80),(-1,-78),(-40,-19)).arc((-51,-1),(-70,6)).arc((-56,-37),(-72,-80)).assemble().finalize().extrude(-105).union(w0.workplane(offset=60/2).moveTo(47,75).cylinder(60,25))