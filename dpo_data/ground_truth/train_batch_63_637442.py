import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,87,0))
r=w0.sketch().arc((-82,43),(-41,-87),(92,-54)).segment((-38,-54)).segment((-38,80)).segment((68,80)).arc((14,100),(-41,87)).arc((-74,76),(-82,43)).assemble().finalize().extrude(-175)