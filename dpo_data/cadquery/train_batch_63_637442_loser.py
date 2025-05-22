import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-87,0))
r=w0.sketch().arc((-82,43),(-33,-92),(92,-54)).segment((-38,-54)).segment((-38,80)).segment((68,80)).arc((11,100),(-47,86)).arc((-76,74),(-82,43)).assemble().finalize().extrude(174)