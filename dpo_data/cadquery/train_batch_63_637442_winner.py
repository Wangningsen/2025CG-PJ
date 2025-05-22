import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,88,0))
r=w0.sketch().arc((-82,43),(-42,-87),(92,-54)).segment((-38,-54)).segment((-38,80)).segment((68,80)).arc((17,100),(-39,88)).arc((-75,75),(-82,43)).assemble().finalize().extrude(-175)