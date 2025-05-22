import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('YZ',origin=(33,0,0))
r=w0.sketch().arc((-58,13),(-90,-28),(-54,9)).segment((2,9)).segment((2,15)).segment((-58,15)).close().assemble().push([(-73,-8.5)]).rect(42,19,mode='s').finalize().extrude(-38).union(w1.sketch().segment((16,8),(49,8)).segment((49,100)).segment((16,100)).segment((16,91)).segment((37,91)).segment((37,34)).segment((16,34)).close().assemble().push([(44,91)]).circle(4,mode='s').finalize().extrude(-64))