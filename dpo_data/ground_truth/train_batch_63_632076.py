import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.sketch().arc((-71,-55),(-47,-100),(-26,-54)).arc((-48,-60),(-71,-55)).assemble().finalize().extrude(-88).union(w0.sketch().arc((38,83),(49,73),(57,61)).arc((71,94),(38,83)).assemble().finalize().extrude(19))