import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((-83,-80),(-76,-80)).arc((-44,-100),(-12,-80)).segment((-5,-80)).segment((-5,-47)).segment((-12,-47)).arc((-44,-27),(-76,-47)).segment((-83,-47)).close().assemble().reset().face(w0.sketch().segment((-79,-78),(-56,-78)).segment((-56,-71)).arc((-54,-64),(-56,-57)).segment((-56,-50)).segment((-79,-50)).segment((-79,-57)).arc((-81,-64),(-79,-71)).close().assemble(),mode='s').finalize().extrude(-5).union(w1.workplane(offset=-13/2).moveTo(28,45).cylinder(13,55))