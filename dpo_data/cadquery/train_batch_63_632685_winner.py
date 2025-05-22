import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().segment((-6,26),(-1,26)).arc((47,-14),(95,26)).segment((100,26)).segment((100,47)).segment((95,47)).arc((47,86),(-1,47)).segment((-6,47)).close().assemble().reset().face(w0.sketch().segment((29,-6),(64,-6)).segment((64,11)).arc((77,37),(64,61)).segment((64,79)).segment((29,79)).segment((29,61)).arc((16,37),(29,11)).close().assemble(),mode='s').finalize().extrude(41).union(w1.sketch().push([(-47.5,-77)]).rect(105,18).push([(-37,-84.5)]).rect(4,1,mode='s').finalize().extrude(15))