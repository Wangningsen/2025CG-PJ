import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
r=w0.workplane(offset=-63/2).moveTo(-62,26).box(76,56,63).union(w0.sketch().arc((62,41),(32,-50),(75,36)).arc((62,23),(62,41)).assemble().push([(79.5,42.5)]).rect(25,7).finalize().extrude(22))