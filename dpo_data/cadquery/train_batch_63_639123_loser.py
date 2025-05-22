import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('YZ',origin=(33,0,0))
r=w0.sketch().arc((-54,10),(-99,-14),(-49,-9)).segment((-48,-9)).segment((-48,-6)).arc((-49,-4),(-49,-3)).segment((-48,-3)).segment((-48,9)).segment((2,9)).segment((2,15)).segment((-54,15)).close().assemble().push([(-76,-8.5)]).rect(36,19,mode='s').finalize().extrude(-38).union(w1.sketch().segment((16,8),(49,8)).segment((49,100)).segment((16,100)).segment((16,91)).segment((37,91)).segment((37,34)).segment((16,34)).close().assemble().push([(44,93)]).circle(6,mode='s').finalize().extrude(-64))