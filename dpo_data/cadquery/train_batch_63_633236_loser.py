import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().push([(-63,17)]).circle(37).push([(43.5,-11.5)]).rect(47,97).finalize().extrude(-112).union(w0.sketch().segment((30,50),(58,50)).segment((58,69)).segment((30,68)).close().assemble().finalize().extrude(-27)).union(w0.workplane(offset=56/2).moveTo(43,-11).cylinder(56,57))