import cadquery as cq
w0=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.sketch().segment((-82,-31),(-23,-31)).segment((-23,-46)).segment((42,-46)).segment((42,-35)).arc((96,25),(19,34)).segment((-23,34)).segment((-23,-27)).segment((-82,-27)).close().assemble().push([(56,8)]).circle(5,mode='s').finalize().extrude(-82).union(w0.workplane(offset=100/2).moveTo(-64.5,-37.5).box(71,29,100))