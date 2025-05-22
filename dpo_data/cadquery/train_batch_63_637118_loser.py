import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,2))
r=w0.workplane(offset=-26/2).moveTo(-67,27).cylinder(26,33).union(w0.sketch().segment((20,14),(31,14)).arc((58,-60),(87,14)).segment((90,14)).segment((90,60)).segment((20,60)).close().assemble().push([(60,-22)]).circle(18,mode='s').finalize().extrude(22))