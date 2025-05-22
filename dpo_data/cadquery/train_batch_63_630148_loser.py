import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,82))
r=w0.workplane(offset=-174/2).moveTo(14,-81).cylinder(174,19).union(w0.sketch().push([(0,10)]).circle(90).reset().face(w0.sketch().segment((-17,-60),(17,-60)).segment((17,-6)).arc((29,10),(17,27)).segment((17,69)).segment((-17,69)).close().assemble(),mode='s').finalize().extrude(10))