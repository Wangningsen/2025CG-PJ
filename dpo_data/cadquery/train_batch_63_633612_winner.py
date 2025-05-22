import cadquery as cq
w0=cq.Workplane('YZ',origin=(-7,0,0))
w1=cq.Workplane('YZ',origin=(15,0,0))
r=w0.workplane(offset=-13/2).moveTo(28,45).cylinder(13,55).union(w1.sketch().segment((-83,-80),(-79,-80)).arc((-44,-100),(-10,-80)).segment((-5,-80)).segment((-5,-47)).segment((-10,-47)).arc((-44,-27),(-79,-47)).segment((-83,-47)).close().assemble().push([(-67.5,-64)]).rect(23,28,mode='s').finalize().extrude(5))