import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().segment((-100,-22),(-62,-45)).segment((-40,-8)).segment((-77,15)).close().assemble().reset().face(w0.sketch().arc((-16,-21),(-16,-67),(30,-61)).segment((30,-62)).segment((32,-60)).segment((31,-59)).arc((34,-52),(35,-44)).arc((33,-9),(-2,-3)).segment((-7,6)).segment((-9,4)).segment((-4,-4)).arc((-12,-12),(-16,-21)).assemble()).finalize().extrude(68).union(w1.sketch().push([(50.5,-39.5)]).rect(49,41).push([(50,-40)]).rect(34,8,mode='s').finalize().extrude(86))