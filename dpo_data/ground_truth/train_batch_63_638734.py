import cadquery as cq
w0=cq.Workplane('YZ',origin=(51,0,0))
r=w0.sketch().segment((-74,-100),(74,-100)).segment((74,-32)).segment((42,-60)).segment((-41,34)).segment((33,100)).segment((-74,100)).close().assemble().push([(-13,-71)]).circle(12,mode='s').finalize().extrude(-102)