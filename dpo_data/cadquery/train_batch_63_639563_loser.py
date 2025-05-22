import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
w1=cq.Workplane('YZ',origin=(0,0,0))
r=w0.sketch().segment((31,86),(65,86)).segment((65,100)).segment((31,100)).segment((31,97)).segment((42,97)).segment((42,90)).segment((31,90)).close().assemble().push([(58,95)]).circle(4,mode='s').finalize().extrude(24).union(w1.sketch().push([(-43,0)]).circle(57).push([(4,13)]).circle(7,mode='s').finalize().extrude(-65))