import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((35,-30),(46,-40)).segment((41,-61)).segment((76,-68)).segment((76,-65)).segment((80,-68)).segment((100,-45)).segment((54,-6)).close().assemble().finalize().extrude(-68).union(w0.sketch().push([(-78,47)]).circle(22).push([(-86,52)]).circle(5,mode='s').finalize().extrude(-1))