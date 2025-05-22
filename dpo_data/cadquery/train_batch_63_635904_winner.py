import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.sketch().push([(28,-69.5)]).rect(84,61).push([(28,-69)]).circle(10,mode='s').finalize().extrude(-6).union(w0.sketch().arc((-61,15),(-49,-23),(-11,-10)).arc((44,-5),(2,33)).arc((-40,72),(-61,15)).assemble().push([(-1,97)]).rect(62,6).finalize().extrude(54)).union(w0.workplane(offset=100/2).moveTo(-40,-1).cylinder(100,30))