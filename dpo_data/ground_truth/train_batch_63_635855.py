import cadquery as cq
w0=cq.Workplane('YZ',origin=(3,0,0))
r=w0.sketch().segment((13,87),(59,48)).segment((73,65)).arc((37,67),(24,100)).close().assemble().finalize().extrude(-54).union(w0.workplane(offset=42/2).moveTo(-19,-46).cylinder(42,54)).union(w0.sketch().push([(-18,-27)]).circle(23).push([(-3.5,-27)]).rect(9,16,mode='s').finalize().extrude(47))