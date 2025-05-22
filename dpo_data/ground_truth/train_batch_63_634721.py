import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-7,0))
w1=cq.Workplane('YZ',origin=(-88,0,0))
r=w0.workplane(offset=28/2).moveTo(50,38).cylinder(28,50).union(w1.sketch().segment((-51,-75),(0,-75)).segment((0,-100)).segment((31,-100)).segment((31,-75)).segment((51,-75)).segment((51,-43)).segment((31,-43)).segment((31,-21)).segment((0,-21)).segment((0,-43)).segment((-51,-43)).close().assemble().push([(0,-59)]).rect(16,16,mode='s').finalize().extrude(138))