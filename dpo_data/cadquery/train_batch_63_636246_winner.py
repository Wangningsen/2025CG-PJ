import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-55))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((-27,14),(-24,14)).arc((16,-19),(56,14)).segment((100,14)).segment((100,51)).segment((42,51)).arc((16,53),(-10,41)).arc((-18,39),(-24,33)).segment((-27,33)).close().assemble().push([(37,31)]).circle(18,mode='s').finalize().extrude(18).union(w1.workplane(offset=-93/2).moveTo(0,6).box(182,98,93))