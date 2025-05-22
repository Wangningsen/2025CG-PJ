import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((35,-30),(46,-39)).segment((41,-61)).segment((75,-68)).segment((76,-65)).segment((80,-68)).segment((100,-45)).segment((54,-6)).close().assemble().finalize().extrude(-69).union(w0.sketch().segment((-65,29),(-65,35)).segment((-61,35)).segment((-61,33)).arc((-94,62),(-65,29)).assemble().finalize().extrude(-1))