import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
w1=cq.Workplane('YZ',origin=(35,0,0))
r=w0.sketch().arc((-72,-56),(-48,-100),(-27,-54)).arc((-49,-60),(-72,-56)).assemble().finalize().extrude(-89).union(w1.sketch().arc((38,83),(51,71),(60,59)).arc((71,67),(76,80)).arc((75,81),(76,82)).arc((57,100),(38,83)).assemble().finalize().extrude(19))