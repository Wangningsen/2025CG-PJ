import cadquery as cq
w0=cq.Workplane('YZ',origin=(-9,0,0))
w1=cq.Workplane('ZX',origin=(0,-55,0))
r=w0.sketch().segment((-82,-31),(-23,-31)).segment((-23,-46)).segment((42,-46)).segment((42,-35)).arc((98,21),(20,34)).segment((-23,34)).segment((-23,-27)).segment((-82,-27)).close().assemble().push([(56,8)]).circle(5,mode='s').finalize().extrude(-82).union(w0.workplane(offset=101/2).moveTo(-64.5,-37.5).box(71,29,101)).union(w1.sketch().segment((-52,-11),(-32,-11)).arc((-43,4),(-42,23)).segment((-52,23)).close().assemble().finalize().extrude(-24))