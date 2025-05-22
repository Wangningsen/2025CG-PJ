import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,4))
r=w0.sketch().segment((-88,-73),(-83,-73)).segment((-83,-100)).segment((-67,-100)).segment((-67,-73)).segment((-6,-73)).segment((-6,-72)).segment((-5,-72)).segment((-5,-73)).segment((95,-73)).segment((95,35)).segment((15,35)).arc((-54,98),(-88,16)).close().assemble().push([(16,-52)]).circle(2,mode='s').finalize().extrude(-8)