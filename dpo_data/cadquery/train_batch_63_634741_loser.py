import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,0,0))
w1=cq.Workplane('XY',origin=(0,0,18))
r=w0.sketch().push([(29.5,5)]).rect(89,96).push([(29,-12)]).circle(13,mode='s').finalize().extrude(-56).union(w0.sketch().segment((22,2),(31,2)).arc((35,-2),(41,-6)).arc((43,-4),(43,-6)).arc((46,-4),(48,2)).segment((38,2)).segment((38,33)).segment((22,33)).close().assemble().finalize().extrude(100)).union(w1.workplane(offset=-92/2).moveTo(-20.5,-74).box(65,52,92))