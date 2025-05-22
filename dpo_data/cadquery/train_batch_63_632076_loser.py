import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.sketch().arc((-71,-55),(-47,-100),(-27,-54)).arc((-49,-60),(-71,-55)).assemble().finalize().extrude(-89).union(w0.sketch().arc((38,83),(49,72),(58,60)).arc((73,92),(38,83)).assemble().finalize().extrude(19))