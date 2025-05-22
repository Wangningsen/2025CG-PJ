import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((35,-30),(46,-39)).segment((41,-61)).segment((75,-68)).segment((76,-65)).segment((80,-68)).segment((100,-45)).segment((54,-7)).close().assemble().finalize().extrude(-68).union(w0.sketch().push([(-78,46)]).circle(22).push([(-74.5,29.5)]).rect(3,3,mode='s').finalize().extrude(-1))