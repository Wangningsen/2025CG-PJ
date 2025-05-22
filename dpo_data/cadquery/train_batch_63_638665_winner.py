import cadquery as cq
w0=cq.Workplane('YZ',origin=(-56,0,0))
r=w0.sketch().segment((-13,34),(40,-5)).arc((26,30),(-13,34)).assemble().finalize().extrude(-44).union(w0.sketch().segment((44,22),(52,22)).arc((-52,0),(50,-28)).segment((47,-28)).segment((47,-29)).segment((46,-29)).segment((46,-28)).segment((44,-28)).arc((-45,0),(44,22)).assemble().finalize().extrude(156))