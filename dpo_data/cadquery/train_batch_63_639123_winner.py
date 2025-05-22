import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('YZ',origin=(33,0,0))
r=w0.sketch().arc((-59,14),(-92,-26),(-52,6)).segment((-52,15)).segment((-59,15)).close().assemble().push([(-73,-8.5)]).rect(42,19,mode='s').push([(-23,12)]).rect(48,6).finalize().extrude(-38).union(w1.sketch().segment((16,8),(49,8)).segment((49,100)).segment((16,100)).segment((16,91)).segment((37,91)).segment((37,34)).segment((16,34)).close().assemble().push([(43.5,93)]).rect(9,8,mode='s').finalize().extrude(-64))