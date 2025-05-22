import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-14))
w1=cq.Workplane('XY',origin=(0,0,-25))
r=w0.workplane(offset=-43/2).moveTo(87,59).cylinder(43,13).union(w0.sketch().push([(-92,-40.5)]).rect(16,49).push([(-91,-52)]).circle(1,mode='s').finalize().extrude(78)).union(w1.sketch().segment((-20,-53),(-9,-53)).arc((17,-72),(43,-53)).segment((54,-53)).segment((54,-36)).segment((43,-36)).arc((17,-17),(-9,-36)).segment((-20,-36)).close().assemble().finalize().extrude(-39))